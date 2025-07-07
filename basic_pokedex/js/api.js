// Pokemon API service with enhanced caching and error handling
class PokemonAPI {
    constructor() {
        this.baseUrl = 'https://pokeapi.co/api/v2';
        this.cache = new Map();
        this.offlineData = this.loadOfflineData();
        this.retryAttempts = 3;
        this.retryDelay = 1000;
    }

    // Enhanced caching with localStorage backup
    loadOfflineData() {
        try {
            const stored = localStorage.getItem('pokemon_cache');
            return stored ? JSON.parse(stored) : {};
        } catch (error) {
            console.warn('Failed to load offline data:', error);
            return {};
        }
    }

    saveOfflineData() {
        try {
            const cacheData = Object.fromEntries(this.cache);
            localStorage.setItem('pokemon_cache', JSON.stringify(cacheData));
        } catch (error) {
            console.warn('Failed to save offline data:', error);
        }
    }

    // Enhanced fetch with retry logic and offline fallback
    async fetchWithRetry(url, options = {}) {
        for (let attempt = 0; attempt < this.retryAttempts; attempt++) {
            try {
                const response = await fetch(url, {
                    ...options,
                    timeout: 10000,
                    signal: AbortSignal.timeout(10000)
                });
                
                if (!response.ok) {
                    if (response.status === 404) {
                        throw new Error('Pokemon not found');
                    }
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                
                return response;
            } catch (error) {
                if (attempt === this.retryAttempts - 1) {
                    throw error;
                }
                
                await this.delay(this.retryDelay * Math.pow(2, attempt));
            }
        }
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async fetchPokemon(pokemonId) {
        try {
            // Check cache first
            const cacheKey = `pokemon_${pokemonId}`;
            if (this.cache.has(cacheKey)) {
                return this.cache.get(cacheKey);
            }

            // Check offline data
            if (this.offlineData[cacheKey]) {
                return this.offlineData[cacheKey];
            }

            const response = await this.fetchWithRetry(`${this.baseUrl}/pokemon/${pokemonId}`);
            const pokemon = await response.json();
            
            // Fetch additional species data with error handling
            let speciesData = null;
            try {
                const speciesResponse = await this.fetchWithRetry(pokemon.species.url);
                speciesData = await speciesResponse.json();
            } catch (error) {
                console.warn('Failed to fetch species data:', error);
                speciesData = { name: pokemon.name, id: pokemon.id };
            }
            
            // Fetch evolution chain with error handling
            let evolutionData = null;
            try {
                if (speciesData?.evolution_chain?.url) {
                    const evolutionResponse = await this.fetchWithRetry(speciesData.evolution_chain.url);
                    evolutionData = await evolutionResponse.json();
                }
            } catch (error) {
                console.warn('Failed to fetch evolution data:', error);
            }

            const pokemonData = {
                ...pokemon,
                species: speciesData,
                evolution: evolutionData,
                cached_at: Date.now()
            };

            // Cache the result
            this.cache.set(cacheKey, pokemonData);
            this.saveOfflineData();
            
            return pokemonData;

        } catch (error) {
            console.error('Error fetching Pokemon:', error);
            
            // Try offline fallback
            const cacheKey = `pokemon_${pokemonId}`;
            if (this.offlineData[cacheKey]) {
                console.log('Using offline data for:', pokemonId);
                return this.offlineData[cacheKey];
            }
            
            throw error;
        }
    }

    async fetchPokemonList(limit = 20, offset = 0) {
        try {
            const cacheKey = `pokemon_list_${limit}_${offset}`;
            if (this.cache.has(cacheKey)) {
                return this.cache.get(cacheKey);
            }

            const response = await this.fetchWithRetry(`${this.baseUrl}/pokemon?limit=${limit}&offset=${offset}`);
            const data = await response.json();
            
            this.cache.set(cacheKey, data);
            this.saveOfflineData();
            
            return data;
        } catch (error) {
            console.error('Error fetching Pokemon list:', error);
            throw error;
        }
    }

    async searchPokemon(query) {
        try {
            const normalizedQuery = query.toLowerCase().trim();
            
            // If it's a number, fetch directly
            if (!isNaN(normalizedQuery)) {
                return await this.fetchPokemon(parseInt(normalizedQuery));
            }
            
            // Otherwise, try to fetch by name
            return await this.fetchPokemon(normalizedQuery);
        } catch (error) {
            throw new Error(`Pokemon "${query}" not found`);
        }
    }

    getPokemonImageUrl(pokemonId) {
        return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${pokemonId}.png`;
    }

    getPokemonSpriteUrl(pokemonId) {
        return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemonId}.png`;
    }

    // Clear cache (useful for development)
    clearCache() {
        this.cache.clear();
        localStorage.removeItem('pokemon_cache');
    }

    // Get cache size
    getCacheSize() {
        return this.cache.size;
    }
}

// Export for use in other modules
window.PokemonAPI = PokemonAPI;
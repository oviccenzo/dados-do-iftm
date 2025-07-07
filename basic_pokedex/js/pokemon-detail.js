// Pokemon Detail View Controller with enhanced features
class PokemonDetailController {
    constructor() {
        this.api = new PokemonAPI();
        this.currentPokemonId = this.getPokemonIdFromUrl() || 25; // Default to Pikachu
        this.favorites = this.loadFavorites();
        this.searchHistory = this.loadSearchHistory();
        this.isLoading = false;
        this.init();
    }

    getPokemonIdFromUrl() {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('id') || urlParams.get('pokemon');
    }

    async init() {
        this.setupEventListeners();
        this.setupAccessibility();
        this.setupKeyboardNavigation();
        await this.loadPokemon(this.currentPokemonId);
        this.updateFavoriteButton();
    }

    setupEventListeners() {
        // Tab navigation
        document.querySelectorAll('.tab-button').forEach(button => {
            button.addEventListener('click', (e) => {
                this.switchTab(e.target.dataset.tab);
            });
        });

        // Navigation arrows
        document.querySelector('.prev-pokemon')?.addEventListener('click', () => {
            this.navigatePokemon(-1);
        });

        document.querySelector('.next-pokemon')?.addEventListener('click', () => {
            this.navigatePokemon(1);
        });

        // Favorite button
        document.querySelector('.favorite-btn')?.addEventListener('click', () => {
            this.toggleFavorite();
        });

        // Enhanced search functionality
        const searchInput = document.querySelector('.search-input');
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.searchPokemon(e.target.value);
                }
            });

            // Search suggestions
            searchInput.addEventListener('input', this.debounce((e) => {
                this.showSearchSuggestions(e.target.value);
            }, 300));
        }

        // Handle browser back/forward
        window.addEventListener('popstate', (e) => {
            if (e.state?.pokemonId) {
                this.loadPokemon(e.state.pokemonId);
            }
        });

        // Handle move filter buttons
        document.querySelectorAll('#moves-tab button').forEach(button => {
            button.addEventListener('click', (e) => {
                this.filterMoves(e.target.textContent.toLowerCase());
            });
        });
    }

    setupAccessibility() {
        // Add ARIA labels and descriptions
        document.querySelectorAll('button').forEach(button => {
            if (!button.hasAttribute('aria-label')) {
                button.setAttribute('aria-label', button.textContent || 'Button');
            }
        });

        // Add keyboard navigation hints
        document.querySelectorAll('.tab-button').forEach(button => {
            button.setAttribute('role', 'tab');
            button.setAttribute('tabindex', '0');
        });

        // Add live region for announcements
        const liveRegion = document.createElement('div');
        liveRegion.id = 'live-region';
        liveRegion.setAttribute('aria-live', 'polite');
        liveRegion.className = 'sr-only';
        document.body.appendChild(liveRegion);
    }

    setupKeyboardNavigation() {
        // Arrow key navigation for tabs
        document.addEventListener('keydown', (e) => {
            if (e.target.classList.contains('tab-button')) {
                const tabs = Array.from(document.querySelectorAll('.tab-button'));
                const currentIndex = tabs.indexOf(e.target);
                
                if (e.key === 'ArrowLeft' && currentIndex > 0) {
                    tabs[currentIndex - 1].focus();
                    tabs[currentIndex - 1].click();
                } else if (e.key === 'ArrowRight' && currentIndex < tabs.length - 1) {
                    tabs[currentIndex + 1].focus();
                    tabs[currentIndex + 1].click();
                }
            }
        });

        // Quick navigation with number keys
        document.addEventListener('keydown', (e) => {
            if (e.target.tagName !== 'INPUT' && e.key >= '1' && e.key <= '4') {
                const tabIndex = parseInt(e.key) - 1;
                const tabs = document.querySelectorAll('.tab-button');
                if (tabs[tabIndex]) {
                    tabs[tabIndex].click();
                }
            }
        });
    }

    async loadPokemon(pokemonId) {
        if (this.isLoading) return;
        
        try {
            this.isLoading = true;
            this.showLoading();
            this.hideError();
            
            const pokemon = await this.api.fetchPokemon(pokemonId);
            this.currentPokemonId = pokemon.id;
            this.renderPokemon(pokemon);
            this.updateUrl(pokemon.id);
            this.announceToScreenReader(`Loaded ${pokemon.name} details`);
            
            // Preload adjacent Pokemon for better UX
            this.preloadAdjacentPokemon(pokemon.id);
            
        } catch (error) {
            this.showError(error.message);
            this.announceToScreenReader(`Error loading Pokemon: ${error.message}`);
        } finally {
            this.isLoading = false;
            this.hideLoading();
        }
    }

    async preloadAdjacentPokemon(pokemonId) {
        // Preload next and previous Pokemon in background
        const preloadPromises = [];
        
        if (pokemonId > 1) {
            preloadPromises.push(this.api.fetchPokemon(pokemonId - 1).catch(() => {}));
        }
        if (pokemonId < 1010) {
            preloadPromises.push(this.api.fetchPokemon(pokemonId + 1).catch(() => {}));
        }
        
        await Promise.all(preloadPromises);
    }

    renderPokemon(pokemon) {
        this.updateBasicInfo(pokemon);
        this.updateStats(pokemon);
        this.updateAbilities(pokemon);
        this.updateEvolution(pokemon);
        this.updateMoves(pokemon);
        this.updateBreedingInfo(pokemon);
        this.updateHabitatInfo(pokemon);
        this.updateFavoriteButton();
        this.updateMetaTags(pokemon);
    }

    updateBasicInfo(pokemon) {
        // Update title and meta tags
        document.title = `${this.capitalize(pokemon.name)} - Pokemon Detail | Basic Pokedex`;
        
        // Update Pokemon name and ID
        document.querySelector('.pokemon-name').textContent = this.capitalize(pokemon.name);
        document.querySelector('.pokemon-id').textContent = `#${pokemon.id.toString().padStart(3, '0')}`;
        document.querySelector('.pokemon-number').textContent = `#${pokemon.id.toString().padStart(3, '0')}`;

        // Update breadcrumb
        document.querySelector('.breadcrumb-pokemon').textContent = this.capitalize(pokemon.name);

        // Update image with loading states
        const pokemonImage = document.querySelector('.pokemon-image');
        pokemonImage.style.opacity = '0.5';
        pokemonImage.src = this.api.getPokemonImageUrl(pokemon.id);
        pokemonImage.alt = `${pokemon.name} official artwork`;
        
        pokemonImage.onload = () => {
            pokemonImage.style.opacity = '1';
        };
        
        pokemonImage.onerror = () => {
            pokemonImage.src = this.api.getPokemonSpriteUrl(pokemon.id);
            pokemonImage.alt = `${pokemon.name} sprite`;
            pokemonImage.style.opacity = '1';
        };

        // Update types with enhanced styling
        const typeContainer = document.querySelector('.type-badges');
        typeContainer.innerHTML = '';
        pokemon.types.forEach(type => {
            const badge = document.createElement('span');
            badge.className = `badge bg-${this.getTypeColor(type.type.name)}-100 text-${this.getTypeColor(type.type.name)}-700 px-4 py-2 rounded-full font-medium`;
            badge.textContent = this.capitalize(type.type.name);
            badge.setAttribute('aria-label', `Type: ${type.type.name}`);
            typeContainer.appendChild(badge);
        });

        // Update height and weight with better formatting
        document.querySelector('.pokemon-height').textContent = `${(pokemon.height / 10).toFixed(1)} m`;
        document.querySelector('.pokemon-weight').textContent = `${(pokemon.weight / 10).toFixed(1)} kg`;
    }

    updateStats(pokemon) {
        const stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed'];
        const statColors = {
            'hp': 'success',
            'attack': 'error',
            'defense': 'primary',
            'special-attack': 'secondary',
            'special-defense': 'accent',
            'speed': 'warning'
        };
        
        stats.forEach((stat, index) => {
            const statData = pokemon.stats.find(s => s.stat.name === stat);
            const statValue = statData?.base_stat || 0;
            const percentage = Math.min((statValue / 255) * 100, 100);
            
            const statBar = document.querySelector(`[data-stat="${stat}"] .stat-bar`);
            const statValueElement = document.querySelector(`[data-stat="${stat}"] .stat-value`);
            
            if (statBar) {
                statBar.style.width = `${percentage}%`;
                statBar.style.transition = 'width 0.8s ease-in-out';
                statBar.className = `stat-bar bg-${statColors[stat]}-500 h-3 rounded-full`;
                statBar.setAttribute('aria-label', `${stat} stat: ${statValue} out of 255`);
            }
            
            if (statValueElement) {
                statValueElement.textContent = statValue;
            }
        });

        // Enhanced CP calculation with level ranges
        const total = pokemon.stats.reduce((sum, stat) => sum + stat.base_stat, 0);
        const level15CP = Math.floor((total * 0.517) + 10);
        const level40CP = Math.floor((total * 0.7903) + 10);
        
        document.querySelector('.min-cp').textContent = level15CP;
        document.querySelector('.max-cp').textContent = level40CP;
        document.querySelector('.total-cp').textContent = total;
    }

    async updateAbilities(pokemon) {
        const abilitiesContainer = document.querySelector('.abilities-list');
        abilitiesContainer.innerHTML = '<div class="text-center text-text-secondary">Loading abilities...</div>';

        try {
            const abilityPromises = pokemon.abilities.map(async (ability) => {
                try {
                    const response = await this.api.fetchWithRetry(ability.ability.url);
                    const abilityData = await response.json();
                    return { ability, abilityData };
                } catch (error) {
                    console.warn('Failed to fetch ability:', ability.ability.name, error);
                    return { ability, abilityData: null };
                }
            });

            const abilities = await Promise.all(abilityPromises);
            abilitiesContainer.innerHTML = '';

            abilities.forEach(({ ability, abilityData }) => {
                const abilityElement = document.createElement('div');
                abilityElement.className = 'p-4 bg-accent-50 rounded-lg border border-accent-200';
                
                const description = abilityData?.effect_entries?.find(entry => entry.language.name === 'en')?.effect || 'No description available';
                
                abilityElement.innerHTML = `
                    <div class="flex items-center justify-between mb-2">
                        <h4 class="font-bold text-text-primary">${this.capitalize(ability.ability.name)}</h4>
                        <span class="badge ${ability.is_hidden ? 'bg-secondary-100 text-secondary-700' : 'bg-primary-100 text-primary-700'} px-3 py-1 rounded-full text-sm">
                            ${ability.is_hidden ? 'Hidden' : 'Normal'}
                        </span>
                    </div>
                    <p class="text-text-secondary text-sm leading-relaxed">${description}</p>
                `;
                
                abilitiesContainer.appendChild(abilityElement);
            });
        } catch (error) {
            abilitiesContainer.innerHTML = '<div class="text-center text-error-500">Failed to load abilities</div>';
        }
    }

    updateEvolution(pokemon) {
        const evolutionContainer = document.querySelector('.evolution-chain');
        evolutionContainer.innerHTML = '';

        if (!pokemon.evolution?.chain) {
            evolutionContainer.innerHTML = '<div class="text-center text-text-secondary">No evolution data available</div>';
            return;
        }

        const evolutionChain = this.parseEvolutionChain(pokemon.evolution.chain);
        
        evolutionChain.forEach((evolution, index) => {
            if (index > 0) {
                // Add evolution trigger info
                const arrow = document.createElement('div');
                arrow.className = 'flex flex-col items-center mx-2';
                arrow.innerHTML = `
                    <svg class="w-6 h-6 text-text-secondary mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                    </svg>
                    <p class="text-xs text-text-secondary text-center">${evolution.trigger || 'Level Up'}</p>
                    ${evolution.min_level ? `<p class="text-xs text-text-secondary">Lv. ${evolution.min_level}</p>` : ''}
                `;
                evolutionContainer.appendChild(arrow);
            }

            // Add Pokemon evolution stage
            const pokemonElement = document.createElement('div');
            pokemonElement.className = 'text-center cursor-pointer hover:bg-accent-50 rounded-lg p-2 transition-smooth';
            
            const isCurrentPokemon = evolution.name === pokemon.name;
            const ringClass = isCurrentPokemon ? 'ring-2 ring-primary-500' : '';
            
            pokemonElement.innerHTML = `
                <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mb-2 mx-auto ${ringClass}">
                    <img src="${this.api.getPokemonSpriteUrl(evolution.id)}" alt="${evolution.name}" class="w-16 h-16 object-cover rounded-full" loading="lazy" />
                </div>
                <p class="text-sm font-medium text-text-primary">${this.capitalize(evolution.name)}</p>
                <p class="text-xs text-text-secondary">#${evolution.id.toString().padStart(3, '0')}</p>
            `;
            
            // Add click handler for evolution navigation
            pokemonElement.addEventListener('click', () => {
                if (evolution.id !== this.currentPokemonId) {
                    this.loadPokemon(evolution.id);
                }
            });
            
            evolutionContainer.appendChild(pokemonElement);
        });
    }

    updateMoves(pokemon) {
        const movesContainer = document.querySelector('.moves-list');
        movesContainer.innerHTML = '<div class="text-center text-text-secondary">Loading moves...</div>';

        try {
            // Get different types of moves
            const levelUpMoves = pokemon.moves
                .filter(move => move.version_group_details.some(detail => detail.move_learn_method.name === 'level-up'))
                .sort((a, b) => {
                    const levelA = a.version_group_details.find(detail => detail.move_learn_method.name === 'level-up')?.level_learned_at || 0;
                    const levelB = b.version_group_details.find(detail => detail.move_learn_method.name === 'level-up')?.level_learned_at || 0;
                    return levelA - levelB;
                });

            const tmMoves = pokemon.moves
                .filter(move => move.version_group_details.some(detail => detail.move_learn_method.name === 'machine'));

            const eggMoves = pokemon.moves
                .filter(move => move.version_group_details.some(detail => detail.move_learn_method.name === 'egg'));

            this.currentMoves = { levelUpMoves, tmMoves, eggMoves };
            this.renderMoves('level-up', levelUpMoves.slice(0, 15)); // Show first 15 moves
        } catch (error) {
            movesContainer.innerHTML = '<div class="text-center text-error-500">Failed to load moves</div>';
        }
    }

    renderMoves(type, moves) {
        const movesContainer = document.querySelector('.moves-list');
        movesContainer.innerHTML = '';

        moves.forEach(move => {
            const moveDetail = move.version_group_details.find(detail => 
                detail.move_learn_method.name === (type === 'level-up' ? 'level-up' : type)
            );
            const level = moveDetail?.level_learned_at || 1;

            const moveElement = document.createElement('div');
            moveElement.className = 'flex items-center justify-between p-3 bg-accent-50 rounded-lg border border-accent-200 hover:bg-accent-100 transition-smooth';
            
            moveElement.innerHTML = `
                <div class="flex items-center space-x-3">
                    ${type === 'level-up' ? `<span class="text-xs font-bold text-text-secondary bg-surface px-2 py-1 rounded">Lv.${level}</span>` : ''}
                    <span class="font-medium text-text-primary">${this.capitalize(move.move.name.replace('-', ' '))}</span>
                </div>
                <div class="flex items-center space-x-2">
                    <span class="badge bg-accent-100 text-accent-700 px-2 py-1 text-xs rounded-full">Normal</span>
                    <span class="text-sm text-text-secondary">— PWR</span>
                </div>
            `;
            
            movesContainer.appendChild(moveElement);
        });
    }

    filterMoves(type) {
        // Update active button
        document.querySelectorAll('#moves-tab button').forEach(btn => {
            btn.classList.remove('btn-primary');
            btn.classList.add('bg-border', 'text-text-secondary');
        });

        event.target.classList.remove('bg-border', 'text-text-secondary');
        event.target.classList.add('btn-primary');

        // Render appropriate moves
        switch (type) {
            case 'level up':
                this.renderMoves('level-up', this.currentMoves.levelUpMoves.slice(0, 15));
                break;
            case 'tm/tr':
                this.renderMoves('machine', this.currentMoves.tmMoves.slice(0, 15));
                break;
            case 'egg moves':
                this.renderMoves('egg', this.currentMoves.eggMoves.slice(0, 15));
                break;
        }
    }

    updateBreedingInfo(pokemon) {
        if (!pokemon.species) return;

        const genderRate = pokemon.species.gender_rate;
        let genderRatio = 'Genderless';
        
        if (genderRate >= 0) {
            const femalePercent = (genderRate / 8) * 100;
            const malePercent = 100 - femalePercent;
            genderRatio = `${malePercent}% ♂ / ${femalePercent}% ♀`;
        }

        document.querySelector('.gender-ratio').textContent = genderRatio;
        document.querySelector('.egg-cycles').textContent = `${pokemon.species.hatch_counter || 0} cycles`;
        document.querySelector('.base-exp').textContent = pokemon.base_experience || 'Unknown';
        
        // Egg groups
        const eggGroups = pokemon.species.egg_groups?.map(group => this.capitalize(group.name)).join(', ') || 'Unknown';
        document.querySelector('.egg-groups').textContent = eggGroups;
    }

    updateHabitatInfo(pokemon) {
        if (!pokemon.species) return;

        document.querySelector('.habitat').textContent = pokemon.species.habitat ? this.capitalize(pokemon.species.habitat.name) : 'Unknown';
        document.querySelector('.generation').textContent = pokemon.species.generation ? this.capitalize(pokemon.species.generation.name) : 'Unknown';
        document.querySelector('.catch-rate').textContent = pokemon.species.capture_rate || 'Unknown';
        document.querySelector('.base-friendship').textContent = pokemon.species.base_happiness || 'Unknown';
    }

    updateMetaTags(pokemon) {
        // Update meta description
        let metaDescription = document.querySelector('meta[name="description"]');
        if (!metaDescription) {
            metaDescription = document.createElement('meta');
            metaDescription.name = 'description';
            document.head.appendChild(metaDescription);
        }
        
        const types = pokemon.types.map(type => type.type.name).join(', ');
        metaDescription.content = `${this.capitalize(pokemon.name)} - ${types} type Pokemon. Height: ${(pokemon.height / 10).toFixed(1)}m, Weight: ${(pokemon.weight / 10).toFixed(1)}kg. View detailed stats, abilities, and evolution chain.`;
    }

    parseEvolutionChain(chain) {
        const evolutions = [];
        
        const addEvolution = (evolution) => {
            const id = this.extractIdFromUrl(evolution.species.url);
            const trigger = evolution.evolution_details?.[0]?.trigger?.name || null;
            const minLevel = evolution.evolution_details?.[0]?.min_level || null;
            
            evolutions.push({
                name: evolution.species.name,
                id: id,
                trigger: trigger,
                min_level: minLevel
            });
            
            evolution.evolves_to.forEach(addEvolution);
        };
        
        addEvolution(chain);
        return evolutions;
    }

    extractIdFromUrl(url) {
        const matches = url.match(/\/(\d+)\/$/);
        return matches ? parseInt(matches[1]) : 1;
    }

    switchTab(tabName) {
        // Remove active class from all buttons
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.classList.remove('border-primary', 'text-primary');
            btn.classList.add('border-transparent', 'text-text-secondary');
            btn.setAttribute('aria-selected', 'false');
        });

        // Add active class to clicked button
        const activeButton = document.querySelector(`[data-tab="${tabName}"]`);
        activeButton.classList.remove('border-transparent', 'text-text-secondary');
        activeButton.classList.add('border-primary', 'text-primary');
        activeButton.setAttribute('aria-selected', 'true');

        // Hide all tab contents
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.add('hidden');
            content.setAttribute('aria-hidden', 'true');
        });

        // Show target tab content
        const targetTab = document.getElementById(`${tabName}-tab`);
        targetTab.classList.remove('hidden');
        targetTab.setAttribute('aria-hidden', 'false');
        
        this.announceToScreenReader(`Switched to ${tabName} tab`);
    }

    async navigatePokemon(direction) {
        const newId = this.currentPokemonId + direction;
        if (newId > 0 && newId <= 1010) {
            await this.loadPokemon(newId);
        }
    }

    loadFavorites() {
        try {
            return JSON.parse(localStorage.getItem('pokemon_favorites') || '[]');
        } catch (error) {
            return [];
        }
    }

    saveFavorites() {
        try {
            localStorage.setItem('pokemon_favorites', JSON.stringify(this.favorites));
        } catch (error) {
            console.warn('Failed to save favorites:', error);
        }
    }

    toggleFavorite() {
        const favoriteBtn = document.querySelector('.favorite-btn svg');
        
        if (this.favorites.includes(this.currentPokemonId)) {
            this.favorites = this.favorites.filter(id => id !== this.currentPokemonId);
            favoriteBtn.classList.remove('text-error-500');
            favoriteBtn.classList.add('text-text-secondary');
            favoriteBtn.setAttribute('fill', 'none');
            this.announceToScreenReader('Removed from favorites');
        } else {
            this.favorites.push(this.currentPokemonId);
            favoriteBtn.classList.remove('text-text-secondary');
            favoriteBtn.classList.add('text-error-500');
            favoriteBtn.setAttribute('fill', 'currentColor');
            this.announceToScreenReader('Added to favorites');
        }
        
        this.saveFavorites();
    }

    updateFavoriteButton() {
        const favoriteBtn = document.querySelector('.favorite-btn svg');
        if (this.favorites.includes(this.currentPokemonId)) {
            favoriteBtn.classList.remove('text-text-secondary');
            favoriteBtn.classList.add('text-error-500');
            favoriteBtn.setAttribute('fill', 'currentColor');
        } else {
            favoriteBtn.classList.remove('text-error-500');
            favoriteBtn.classList.add('text-text-secondary');
            favoriteBtn.setAttribute('fill', 'none');
        }
    }

    loadSearchHistory() {
        try {
            return JSON.parse(localStorage.getItem('pokemon_search_history') || '[]');
        } catch (error) {
            return [];
        }
    }

    saveSearchHistory() {
        try {
            localStorage.setItem('pokemon_search_history', JSON.stringify(this.searchHistory));
        } catch (error) {
            console.warn('Failed to save search history:', error);
        }
    }

    async searchPokemon(query) {
        if (!query.trim()) return;
        
        try {
            const pokemonId = isNaN(query) ? query.toLowerCase() : parseInt(query);
            await this.loadPokemon(pokemonId);
            
            // Add to search history
            if (!this.searchHistory.includes(query)) {
                this.searchHistory.unshift(query);
                this.searchHistory = this.searchHistory.slice(0, 10); // Keep only last 10 searches
                this.saveSearchHistory();
            }
            
            // Clear search input
            document.querySelector('.search-input').value = '';
        } catch (error) {
            this.showError(`Pokemon "${query}" not found! Try a different name or ID.`);
        }
    }

    showSearchSuggestions(query) {
        // This would typically show a dropdown with suggestions
        // For now, we'll just log the search attempt
        if (query.length > 2) {
            console.log('Search suggestions for:', query);
        }
    }

    showLoading() {
        const loadingElement = document.querySelector('.loading-skeleton');
        if (loadingElement) {
            loadingElement.classList.remove('hidden');
        }
    }

    hideLoading() {
        const loadingElement = document.querySelector('.loading-skeleton');
        if (loadingElement) {
            loadingElement.classList.add('hidden');
        }
    }

    showError(message) {
        const errorElement = document.querySelector('.error-message');
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.remove('hidden');
            
            // Auto-hide after 5 seconds
            setTimeout(() => {
                this.hideError();
            }, 5000);
        }
    }

    hideError() {
        const errorElement = document.querySelector('.error-message');
        if (errorElement) {
            errorElement.classList.add('hidden');
        }
    }

    updateUrl(pokemonId) {
        const newUrl = `${window.location.pathname}?id=${pokemonId}`;
        window.history.pushState({ pokemonId }, '', newUrl);
    }

    announceToScreenReader(message) {
        const liveRegion = document.getElementById('live-region');
        if (liveRegion) {
            liveRegion.textContent = message;
            setTimeout(() => {
                liveRegion.textContent = '';
            }, 1000);
        }
    }

    getTypeColor(type) {
        const typeColors = {
            normal: 'gray',
            fire: 'error',
            water: 'primary',
            electric: 'accent',
            grass: 'success',
            ice: 'primary',
            fighting: 'error',
            poison: 'secondary',
            ground: 'accent',
            flying: 'primary',
            psychic: 'secondary',
            bug: 'success',
            rock: 'accent',
            ghost: 'secondary',
            dragon: 'primary',
            dark: 'gray',
            steel: 'gray',
            fairy: 'secondary'
        };
        return typeColors[type] || 'gray';
    }

    capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    // Utility function for debouncing
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PokemonDetailController();
});
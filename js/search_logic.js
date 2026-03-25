/**
 * Electech Site-Wide Search Logic
 * Provides asynchronous client-side search across multiple HTML pages.
 */

const searchInput = document.getElementById('site-search-input');
const searchResults = document.getElementById('search-results');
const resultsList = document.getElementById('results-list');
const resultsCount = document.getElementById('results-count');

if (searchInput) {
    searchInput.addEventListener('input', async (e) => {
        const query = e.target.value.trim().toLowerCase();
        
        if (query.length < 2) {
            searchResults.classList.add('hidden');
            return;
        }

        searchResults.classList.remove('hidden');
        resultsList.innerHTML = '<div class="p-4 text-center"><i class="fas fa-circle-notch animate-spin text-customOrange"></i></div>';
        
        // Use pre-loaded JS data instead of fetch
        if (window.SEARCH_DATA) {
            const results = await performSearch(query);
            renderResults(results);
        } else {
            resultsList.innerHTML = '<div class="p-4 text-center text-red-500 text-[10px]">Index non chargé.</div>';
        }
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.add('hidden');
        }
    });
}

async function performSearch(query) {
    if (!window.SEARCH_DATA) return [];
    
    return window.SEARCH_DATA.filter(page => {
        const titleMatch = page.title.toLowerCase().includes(query);
        const contentMatch = page.content ? page.content.toLowerCase().includes(query) : false;
        return titleMatch || contentMatch;
    }).map(page => {
        // Find a snippet in content if possible
        let snippet = "";
        if (page.content) {
            const index = page.content.toLowerCase().indexOf(query);
            if (index !== -1) {
                snippet = page.content.substring(Math.max(0, index - 40), Math.min(page.content.length, index + 60))
                                      .replace(/\ng/, ' ') + '...';
            }
        }
        
        return {
            title: page.title,
            url: page.url,
            snippet: snippet || "Cliquez pour voir le contenu...",
            source: page.title
        };
    });
}

function renderResults(results) {
    if (!resultsCount) return;
    resultsCount.textContent = `${results.length} trouvés`;
    
    if (results.length === 0) {
        resultsList.innerHTML = '<div class="p-6 text-center text-gray-500 text-xs italic">Aucun résultat trouvé pour votre recherche.</div>';
        return;
    }

    resultsList.innerHTML = results.map(res => {
        // Prepare highlighted URL
        const searchInput = document.getElementById('site-search-input');
        const query = searchInput ? searchInput.value.trim() : "";
        const finalUrl = res.url + (query ? `?highlight=${encodeURIComponent(query)}` : "");
        
        return `
            <a href="${finalUrl}" class="block p-3 hover:bg-white/5 rounded-xl transition-all border border-transparent hover:border-gray-800 group">
                <div class="flex justify-between items-start mb-1">
                    <h5 class="text-[11px] font-bold text-white group-hover:text-customOrange transition-colors">${res.title}</h5>
                    <span class="text-[8px] px-1.5 py-0.5 rounded bg-gray-800 text-gray-400 font-bold uppercase tracking-tighter">Source: ${res.source}</span>
                </div>
                <p class="text-[10px] text-gray-500 line-clamp-2 leading-relaxed">...${res.snippet}</p>
            </a>
        `;
    }).join('');
}

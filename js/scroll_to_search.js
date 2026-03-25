/**
 * Electech Auto-Scroll & Highlighting
 * Reads 'highlight' parameter from URL and scrolls to the first match in the page.
 */

(function () {
    const params = new URLSearchParams(window.location.search);
    const term = params.get('highlight');
    if (!term) return;

    window.addEventListener('load', () => {
        const query = term.toLowerCase();
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function(node) {
                    const parent = node.parentNode;
                    const tag = parent.tagName.toLowerCase();
                    if (['script', 'style', 'nav', 'header', 'footer', 'button', 'a'].includes(tag)) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    return NodeFilter.FILTER_ACCEPT;
                }
            },
            false
        );

        let node;
        while (node = walker.nextNode()) {
            const text = node.nodeValue.toLowerCase();
            if (text.includes(query)) {
                const parent = node.parentNode;
                
                // Clear any existing highlight or flash
                parent.classList.add('search-highlight-focus');
                
                // Add CSS for highlighting
                if (!document.getElementById('search-highlight-css')) {
                    const style = document.createElement('style');
                    style.id = 'search-highlight-css';
                    style.innerHTML = `
                        @keyframes searchPulse {
                            0% { outline: 2px solid transparent; background: transparent; }
                            50% { outline: 2px solid #FF8C00; background: rgba(255, 140, 0, 0.1); }
                            100% { outline: 2px solid transparent; background: transparent; }
                        }
                        .search-highlight-focus {
                            animation: searchPulse 1.5s ease-in-out 3;
                            border-radius: 4px;
                            padding: 2px 4px;
                            scroll-margin-top: 100px;
                        }
                    `;
                    document.head.appendChild(style);
                }

                // Smooth scroll
                setTimeout(() => {
                    parent.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }, 300);
                
                break;
            }
        }
    });
})();

const API_URL = 'http://localhost:3000/api';
const SESSION_KEY = 'electech_session';

const API = {
    async call(endpoint, method = 'GET', data = null) {
        try {
            const options = {
                method,
                headers: { 'Content-Type': 'application/json' },
            };
            if (data) options.body = JSON.stringify(data);

            const res = await fetch(`${API_URL}${endpoint}`, options);
            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.message || 'Erreur inconnue');
            }
            return await res.json();
        } catch (error) {
            console.warn('Backend not reachable, falling back to localStorage logic:', error.message);
            // Fallback to simulated logic if server is down
            return this.fallback(endpoint, method, data);
        }
    },

    // Simulation logic to keep the site working without running Node.js
    fallback(endpoint, method, data) {
        if (endpoint === '/login' && method === 'POST') {
            // Simple mock login
            return { user: { name: 'Expert Simulé', email: data.email, role: 'technicien', profileComplete: false } };
        }
        if (endpoint === '/register' && method === 'POST') {
            // Persist user to electech_users array
            const users = JSON.parse(localStorage.getItem('electech_users') || '[]');
            if (users.find(u => u.email === data.email)) {
                throw new Error('Cet email est déjà utilisé.');
            }
            const newUser = {
                id: 'usr_' + Date.now(),
                name: data.name,
                email: data.email,
                role: data.role || 'Technicien',
                date: new Date().toLocaleDateString('fr-FR'),
                profileComplete: false,
                status: 'actif'
            };
            users.unshift(newUser);
            localStorage.setItem('electech_users', JSON.stringify(users));
            return { user: { ...newUser } };
        }
        if (endpoint.startsWith('/profile')) {
            const profiles = JSON.parse(localStorage.getItem('electech_user_profiles') || '{}');
            if (method === 'GET') {
                const params = new URLSearchParams(endpoint.split('?')[1]);
                const email = params.get('email');
                return profiles[email] || {};
            }
            if (method === 'POST') {
                const { email, profile } = data;
                profiles[email] = profile;
                localStorage.setItem('electech_user_profiles', JSON.stringify(profiles));
                
                // profileComplete si ville, spécialité et expérience sont renseignées
                const isComplete = !!(profile.city && profile.specialty && profile.experience);
                return { message: 'Profil mis à jour', profileComplete: isComplete };
            }
        }
        return { message: 'Action simulée' };
    }
};
// Dynamic Article Rendering for Admin
document.addEventListener('DOMContentLoaded', () => {
    if (typeof renderDynamicArticles === 'function') {
        renderDynamicArticles();
    }
});

function renderDynamicArticles() {
    const container = document.getElementById('dynamic-articles');
    if (!container) return; // Only render if the page has the container

    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    const articles = JSON.parse(localStorage.getItem('electech_articles') || '[]');
    const pageArticles = articles.filter(art => art.target_page === currentFile);
    
    if (pageArticles.length === 0) return;

    let html = '';
    
    const pathPrefix = window.location.pathname.includes('/Tech 1/') ? '' : (window.location.pathname.includes('/admin/') || window.location.pathname.includes('/emploi/') ? '../Tech 1/' : 'Tech 1/');
    
    function truncateWords(str, count) {
        if (!str) return "";
        const words = str.split(/\s+/);
        if (words.length <= count) return str;
        return words.slice(0, count).join(" ") + "...";
    }

    // Sort chronologically reverse (newest first)
    pageArticles.reverse().forEach(art => {
        const d = new Date(art.date);
        const dateStr = d.toLocaleDateString('fr-FR', { day: '2-digit', month: 'short', year: 'numeric' });
        const excerpt = truncateWords(art.content, 40); // 40 mots pour l'extrait

        html += `
            <div class="bg-gray-900 border border-gray-800 rounded-2xl p-8 shadow-lg hover:border-customOrange transition-all duration-300 group flex flex-col md:flex-row gap-8 mb-8">
                <div class="w-full md:w-1/3 flex-shrink-0">
                    <div class="w-full h-48 md:h-full rounded-xl overflow-hidden bg-black border border-gray-800 relative group-hover:border-customOrange/50 transition-colors">
                        <img src="${art.image}" alt="Cover" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-300 group-hover:scale-105">
                        <div class="absolute top-3 right-3 bg-black/80 backdrop-blur-sm px-3 py-1 rounded-full border border-customOrange/30">
                            <span class="text-[10px] font-black tracking-widest text-customOrange uppercase">${art.category}</span>
                        </div>
                    </div>
                </div>
                <div class="w-full md:w-2/3 flex flex-col justify-center">
                    <div class="flex items-center gap-3 mb-3 text-gray-500 text-xs font-bold uppercase tracking-wider">
                        <span><i class="fas fa-calendar-alt mr-1"></i> ${dateStr}</span>
                        <span>&bull;</span>
                        <span class="text-customOrange"><i class="fas fa-user-shield mr-1"></i> ${art.author || 'Mode Admin'}</span>
                    </div>
                    <h2 class="text-2xl md:text-3xl font-black text-white mb-4 leading-tight group-hover:text-customOrange transition-colors">
                        ${art.title}
                    </h2>
                    <div class="prose prose-invert prose-orange max-w-none text-gray-400 overflow-hidden text-sm md:text-base leading-relaxed mb-6 break-words break-all line-clamp-4">
                        ${excerpt}
                    </div>
                    <div class="mt-auto">
                        <a href="${pathPrefix}Article.html?id=${art.id}" class="inline-block bg-customOrange/10 text-customOrange border border-customOrange/30 hover:bg-customOrange hover:text-black font-bold text-xs uppercase tracking-widest py-2 px-6 rounded-lg transition-all shadow-md group-hover:bg-customOrange group-hover:text-black">
                            Continuer la lecture <i class="fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform"></i>
                        </a>
                    </div>
                </div>
            </div>
        `;
    });

    container.innerHTML = `
        <div class="w-full mb-8 pt-8 border-t border-gray-800">
            <h3 class="text-2xl font-black text-white flex items-center mb-2">
                <i class="fas fa-newspaper text-customOrange mr-3"></i> Nouveautés & Mises à jour
            </h3>
            <p class="text-gray-500 text-sm">Publications récentes de l'administration</p>
        </div>
        ${html}
    `;
}

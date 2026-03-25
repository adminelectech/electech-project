import re

filepath = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site\Technique\Technique.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Hero Section
content = content.replace("Hlega - Jeux & QCMs Électriques", "Plongez au coeur de la Technique")
content = re.sub(
    r'<h1 class="text-4xl.*?Section <span class="text-customOrange">Hlega</span>\s*</h1>',
    r'<h1 class="text-4xl md:text-6xl font-black text-white uppercase tracking-tighter mb-4">Rubrique <span class="text-customOrange">Technique</span></h1>',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<p class="text-gray-400 text-lg max-w-2xl mx-auto mb-8">.*?</p>',
    r'<p class="text-gray-400 text-lg max-w-2xl mx-auto mb-8">Découvrez nos articles spécialisés, ressources et outils pratiques dans les 4 piliers technologiques : Électricité, Software, Aéronautique, et Génie Mécanique.</p>',
    content, flags=re.DOTALL
)

# 2. Update Global Internal Menu Buttons
old_menu = r"""            <!-- Global Internal Menu -->
            <div class="flex flex-wrap justify-center gap-4 mt-8">
                <button onclick="switchTab('accueil')" id="btn-accueil" class="tab-btn active px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange transition-all flex items-center gap-2">
                    <i class="fas fa-home"></i> Accueil
                </button>
                <button onclick="switchTab('qcm')" id="btn-qcm" class="tab-btn px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-question-circle"></i> QCMs
                </button>
                <button onclick="switchTab('jeux')" id="btn-jeux" class="tab-btn px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-puzzle-piece"></i> Jeux
                </button>
                <button onclick="switchTab('defis')" id="btn-defis" class="tab-btn px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-trophy text-yellow-500"></i> Défis
                </button>
            </div>"""

new_menu = r"""            <!-- Global Internal Menu -->
            <div class="flex flex-wrap justify-center gap-4 mt-8">
                <button onclick="switchTab('electricite')" id="btn-electricite" class="tab-btn active px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-black bg-customOrange transition-all flex items-center gap-2">
                    <i class="fas fa-bolt"></i> Électricité
                </button>
                <button onclick="switchTab('software')" id="btn-software" class="tab-btn px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-code"></i> Software
                </button>
                <button onclick="switchTab('aeronautique')" id="btn-aeronautique" class="tab-btn px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-plane"></i> Aéronautique
                </button>
                <button onclick="switchTab('mecanique')" id="btn-mecanique" class="tab-btn px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-cogs"></i> Génie Mécanique
                </button>
            </div>"""

content = content.replace(old_menu, new_menu)

# 3. Replace Tabs Content
old_tabs_regex = r'<!-- TAB CONTENT: ACCUEIL -->.*?</main>'
new_tabs = r"""<!-- TAB CONTENT: ELECTRICITE -->
        <div id="tab-electricite" class="tab-content active space-y-12">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-yellow-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-yellow-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-network-wired"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Installations HT/BT</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Tout savoir sur la distribution, les transformateurs et les cellules haute tension.</p>
                </div>
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-blue-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-blue-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-blue-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-microchip"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Électronique de Puissance</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Onduleurs, hacheurs, redresseurs et contrôle commande des moteurs.</p>
                </div>
            </div>
        </div>

        <!-- TAB CONTENT: SOFTWARE -->
        <div id="tab-software" class="tab-content hidden space-y-12">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-green-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-green-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-green-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-terminal"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Algorithmique</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Les bases de la programmation, structures de données et logique computationnelle.</p>
                </div>
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-purple-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-purple-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-purple-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-robot"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Intelligence Artificielle</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Machine Learning, réseaux de neurones et applications industrielles.</p>
                </div>
            </div>
        </div>

        <!-- TAB CONTENT: AERONAUTIQUE -->
        <div id="tab-aeronautique" class="tab-content hidden space-y-12">
             <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-sky-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-sky-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-sky-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-plane-departure"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Aérodynamique</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Étude des flux d'air, portance, traînée et conception des profils d'ailes.</p>
                </div>
            </div>
        </div>

        <!-- TAB CONTENT: MECANIQUE -->
        <div id="tab-mecanique" class="tab-content hidden space-y-12">
             <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-orange-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-orange-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-orange-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-cogs"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Transmission de Puissance</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Engrenages, courroies, arbres de transmission et cinématique des mécanismes.</p>
                </div>
            </div>
        </div>

    </main>"""

content = re.sub(old_tabs_regex, new_tabs, content, flags=re.DOTALL)

# 4. Modify JavaScript
# Replace JS tabs logic and remove all Hlega game logic
old_js_regex = r"const tabs = \['accueil', 'qcm', 'jeux', 'defis'\];.*"
new_js = r"""const tabs = ['electricite', 'software', 'aeronautique', 'mecanique'];
        function switchTab(targetTab) {
            tabs.forEach(tab => {
                const btn = document.getElementById(`btn-${tab}`);
                const content = document.getElementById(`tab-${tab}`);
                
                if (tab === targetTab) {
                    if (btn) {
                        btn.classList.add('bg-customOrange', 'text-black');
                        btn.classList.remove('text-white');
                    }
                    if (content) content.classList.add('active', 'block');
                    if (content) content.classList.remove('hidden');
                } else {
                    if (btn) {
                        btn.classList.remove('bg-customOrange', 'text-black');
                        btn.classList.add('text-white');
                    }
                    if (content) content.classList.remove('active', 'block');
                    if (content) content.classList.add('hidden');
                }
            });
            window.location.hash = targetTab;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    </script>
</body>
</html>"""

content = re.sub(old_js_regex, new_js, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Technique.html customized successfully.")

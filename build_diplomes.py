import re

filepath = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site\Diplomes\diplomes.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Hero Section
content = content.replace("Hlega - Jeux & QCMs Électriques", "Vos Formations et Diplômes")
content = re.sub(
    r'<h1 class="text-4xl.*?Section <span class="text-customOrange">Hlega</span>\s*</h1>',
    r'<h1 class="text-4xl md:text-6xl font-black text-white uppercase tracking-tighter mb-4">Espace <span class="text-customOrange">Diplômes</span></h1>',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<p class="text-gray-400 text-lg max-w-2xl mx-auto mb-8">.*?</p>',
    r'<p class="text-gray-400 text-lg max-w-2xl mx-auto mb-8">Découvrez toutes les formations académiques et professionnelles adaptées à vos objectifs, du BTS jusqu\'au Master et MBA.</p>',
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
                <button onclick="switchTab('bts')" id="btn-bts" class="tab-btn active px-6 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-black bg-customOrange transition-all flex items-center gap-2">
                    <i class="fas fa-graduation-cap"></i> BTS
                </button>
                <button onclick="switchTab('dut')" id="btn-dut" class="tab-btn px-6 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-graduation-cap"></i> DUT
                </button>
                <button onclick="switchTab('licence')" id="btn-licence" class="tab-btn px-6 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-award"></i> Licence
                </button>
                <button onclick="switchTab('master')" id="btn-master" class="tab-btn px-6 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-user-graduate"></i> Master
                </button>
                <button onclick="switchTab('doctorat')" id="btn-doctorat" class="tab-btn px-6 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-microscope"></i> Doctorat
                </button>
                <button onclick="switchTab('mba')" id="btn-mba" class="tab-btn px-6 py-3 rounded-xl font-bold uppercase tracking-widest text-xs border border-gray-800 hover:border-customOrange text-white transition-all flex items-center gap-2">
                    <i class="fas fa-certificate text-yellow-500"></i> MBA
                </button>
            </div>"""

content = content.replace(old_menu, new_menu)

# 3. Replace Tabs Content
old_tabs_regex = r'<!-- TAB CONTENT: ACCUEIL -->.*?</main>'

new_tabs = r"""<!-- TAB CONTENT: BTS -->
        <div id="tab-bts" class="tab-content active space-y-12">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-blue-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-blue-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-blue-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-bolt"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">BTS Électrotechnique</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Formation technicien supérieur spécialisé dans l'étude, la mise en oeuvre, et la maintenance des équipements électriques.</p>
                </div>
            </div>
        </div>

        <!-- TAB CONTENT: DUT -->
        <div id="tab-dut" class="tab-content hidden space-y-12">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-green-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-green-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-green-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-microchip"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">DUT GEII</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Génie Électrique et Informatique Industrielle : automatismes, de l'informatique industrielle et des réseaux.</p>
                </div>
            </div>
        </div>

        <!-- TAB CONTENT: LICENCE -->
        <div id="tab-licence" class="tab-content hidden space-y-12">
             <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-purple-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-purple-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-purple-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-solar-panel"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Licence Énergies Renouvelables</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Formation diplômante Bac+3 pour maîtriser les technologies solaires, éoliennes et la gestion de réseau intelligent (Smart Grids).</p>
                </div>
            </div>
        </div>

        <!-- TAB CONTENT: MASTER -->
        <div id="tab-master" class="tab-content hidden space-y-12">
             <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-orange-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-orange-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-orange-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-laptop-code"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Master Systèmes Embarqués</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Ingénierie des systèmes mécatroniques et développement de logiciels critiques embarqués (Aéronautique, Automobile).</p>
                </div>
            </div>
        </div>
        
        <!-- TAB CONTENT: DOCTORAT -->
        <div id="tab-doctorat" class="tab-content hidden space-y-12">
             <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-red-600/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-red-600/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-red-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-atom"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">Cycle Doctorat (Recherche)</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Explorez la R&D approfondie dans les semi-conducteurs quantiques ou les nouveaux matériaux supraconducteurs.</p>
                </div>
            </div>
        </div>
        
        <!-- TAB CONTENT: MBA -->
        <div id="tab-mba" class="tab-content hidden space-y-12">
             <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bento-card p-8 group cursor-pointer relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-400/10 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:bg-yellow-400/20 transition-colors"></div>
                    <div class="w-14 h-14 bg-gray-900 border border-gray-800 rounded-2xl flex items-center justify-center text-2xl text-yellow-500 mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3 class="text-2xl font-black text-white mb-3">MBA Management de l'Industrie</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-6">Alliez expertise technologique et leadership stratégique pour diriger des usines d'énergie et de grandes firmes industrielles.</p>
                </div>
            </div>
        </div>

    </main>"""

content = re.sub(old_tabs_regex, new_tabs, content, flags=re.DOTALL)

# 4. Modify JavaScript
old_js_regex = r"const tabs = \['accueil', 'qcm', 'jeux', 'defis'\];.*"
new_js = r"""const tabs = ['bts', 'dut', 'licence', 'master', 'doctorat', 'mba'];
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

print("diplomes.html customized successfully.")

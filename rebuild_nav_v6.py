import os
import glob
import re

base_dir = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    if "rebuild_nav" in filepath or "update_nav" in filepath or "README" in filepath or "Diplomes" not in filepath and "emploi" not in filepath and "Tech" not in filepath and "utilisateur" not in filepath and "Hlega" not in filepath and "index.html" not in filepath:
        # We only want to process relevant html files
        pass 
        # Actually let's just process all but python scripts and readme
        
    if "rebuild_nav" in filepath or "update_nav" in filepath or "README" in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    rel_path = os.path.relpath(filepath, base_dir)
    dir_depth = rel_path.count(os.sep)
    prefix = "" if dir_depth == 0 else ("../" * dir_depth)
    
    new_header_block = f"""<div class="container mx-auto flex flex-col md:flex-row justify-between items-center">
            <!-- Logo & Slogan Block -->
            <div class="flex flex-col group mb-6 md:mb-0">
                <a href="{prefix}index.html" class="flex flex-col transition-all duration-300">
                    <div class="text-2xl font-black text-white tracking-widest leading-none flex items-center">
                        <i class="fas fa-bolt text-customOrange mr-2 group-hover:rotate-12 transition-transform"></i>
                        ELEC<span class="text-customOrange">TECH</span>
                    </div>
                    <div class="mt-1.5 py-0.5 px-2 bg-customOrange/10 border border-customOrange/20 rounded-md">
                        <p class="text-[7px] font-black uppercase tracking-[0.3em] text-customOrange whitespace-nowrap">
                            La Tech pour tout le monde
                        </p>
                    </div>
                </a>
            </div>

            <nav class="flex items-center gap-8">
                <ul class="flex flex-wrap justify-center gap-x-5 gap-y-2 text-sm md:text-base font-medium">
                    <!-- HLEGA -->
                    <li class="relative group z-50">
                        <a href="{prefix}Hlega/Hlega.html" class="text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-customOrange pb-1">
                            🎮 Hlega <i class="fas fa-chevron-down text-[10px]"></i>
                        </a>
                        <div class="absolute left-0 mt-3 w-48 bg-gray-900 border border-gray-800 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 overflow-hidden transform origin-top group-hover:scale-100 scale-95 text-left">
                            <ul class="py-2 text-sm font-medium">
                                <li><a href="{prefix}Hlega/Hlega.html#qcm" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-question-circle w-5 text-gray-500"></i> QCMs Éclair</a></li>
                                <li><a href="{prefix}Hlega/Hlega.html#jeux" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-gamepad w-5 text-gray-500"></i> Jeux Interactifs</a></li>
                                <li><a href="{prefix}Hlega/Hlega.html#defis" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-trophy w-5 text-gray-500"></i> Défis & Amis</a></li>
                            </ul>
                        </div>
                    </li>
                    
                    <!-- TECHNIQUE -->
                    <li class="relative group z-40">
                        <a href="{prefix}Technique/Technique.html" class="hover:text-customOrange text-gray-300 font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">
                            ⚙️ Technique <i class="fas fa-chevron-down text-[10px]"></i>
                        </a>
                        <div class="absolute left-0 mt-3 w-64 bg-gray-900 border border-gray-800 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 overflow-hidden transform origin-top group-hover:scale-100 scale-95 text-left">
                            <ul class="py-2 text-sm font-medium">
                                <li class="px-5 py-2 pt-3 text-[10px] font-black text-gray-500 uppercase tracking-widest border-b border-gray-800 mb-1">Notions de base</li>
                                <li><a href="{prefix}Tech 1/electrotechnique.html" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-bolt w-5 text-gray-500"></i> Électrotechnique</a></li>
                                <li><a href="{prefix}Tech 1/electronique.html" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-microchip w-5 text-gray-500"></i> Électronique</a></li>
                                <li><a href="{prefix}Tech 1/energies.html" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-leaf w-5 text-gray-500"></i> Énergies</a></li>
                                <li><a href="{prefix}Tech 1/schemas.html" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-project-diagram w-5 text-gray-500"></i> Schémas</a></li>
                                
                                <li class="px-5 py-2 pt-4 text-[10px] font-black text-gray-500 uppercase tracking-widest border-b border-gray-800 mb-1 mt-2">Spécialisations</li>
                                <li><a href="{prefix}Technique/Technique.html#electricite" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-network-wired w-5 text-gray-500"></i> Électricité</a></li>
                                <li><a href="{prefix}Technique/Technique.html#software" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-code w-5 text-gray-500"></i> Software</a></li>
                                <li><a href="{prefix}Technique/Technique.html#aeronautique" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-plane w-5 text-gray-500"></i> Aéronautique</a></li>
                                <li><a href="{prefix}Technique/Technique.html#mecanique" class="block px-5 py-2 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-cogs w-5 text-gray-500"></i> Génie Mécanique</a></li>
                            </ul>
                        </div>
                    </li>
                    
                    <!-- DIPLOMES -->
                    <li class="relative group z-35">
                        <a href="{prefix}Diplomes/diplomes.html" class="hover:text-customOrange text-gray-300 font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">
                            🎓 Diplômes <i class="fas fa-chevron-down text-[10px]"></i>
                        </a>
                        <div class="absolute left-0 mt-3 w-48 bg-gray-900 border border-gray-800 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 overflow-hidden transform origin-top group-hover:scale-100 scale-95 text-left">
                            <ul class="py-2 text-sm font-medium">
                                <li><a href="{prefix}Diplomes/diplomes.html#bts" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-graduation-cap w-5 text-gray-500"></i> BTS</a></li>
                                <li><a href="{prefix}Diplomes/diplomes.html#dut" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-graduation-cap w-5 text-gray-500"></i> DUT</a></li>
                                <li><a href="{prefix}Diplomes/diplomes.html#licence" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-award w-5 text-gray-500"></i> Licence</a></li>
                                <li><a href="{prefix}Diplomes/diplomes.html#master" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-user-graduate w-5 text-gray-500"></i> Master</a></li>
                                <li><a href="{prefix}Diplomes/diplomes.html#doctorat" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-microscope w-5 text-gray-500"></i> Doctorat</a></li>
                                <li><a href="{prefix}Diplomes/diplomes.html#mba" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-certificate w-5 text-gray-500"></i> MBA</a></li>
                            </ul>
                        </div>
                    </li>
 
                    <!-- COMMUNITY -->
                    <li class="relative group z-30">
                        <a href="{prefix}assets/community/clic.electech.html" class="hover:text-yellow-400 text-gray-300 font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-yellow-400 pb-1">
                            👥 Community <i class="fas fa-chevron-down text-[10px]"></i>
                        </a>
                        <div class="absolute left-0 mt-3 w-48 bg-gray-900 border border-gray-800 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 overflow-hidden transform origin-top group-hover:scale-100 scale-95 text-left">
                            <ul class="py-2 text-sm font-medium">
                                <li><a href="{prefix}assets/community/clic.electech.html" class="block px-5 py-2.5 hover:bg-black hover:text-yellow-400 transition-colors"><i class="fas fa-bolt w-5 text-yellow-400"></i> Clic Electech</a></li>
                                <li><a href="{prefix}utilisateur/forum.html" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-comments w-5 text-gray-500"></i> Forum</a></li>
                            </ul>
                        </div>
                    </li>
 
                    <li><a href="{prefix}Tech 1/bibliotheque.html" class="text-gray-300 hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">📚 Livres</a></li>
                    
                    <!-- EMPLOI -->
                    <li class="relative group z-30">
                        <a href="{prefix}emploi/emploi.html" class="hover:text-customOrange text-gray-300 font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">
                            💼 Emploi <i class="fas fa-chevron-down text-[10px]"></i>
                        </a>
                        <div class="absolute right-0 mt-3 w-56 bg-gray-900 border border-gray-800 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 overflow-hidden transform origin-top group-hover:scale-100 scale-95 text-left">
                            <ul class="py-2 text-sm font-medium">
                                <li><a href="{prefix}emploi/offres.html" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-briefcase w-5 text-gray-500"></i> Offres d'Emploi</a></li>
                                <li><a href="{prefix}emploi/demandes.html" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-user-tie w-5 text-gray-500"></i> Demandes d'Emploi</a></li>
                            </ul>
                        </div>
                    </li>
                </ul>
 
                <!-- Dynamic Auth Zone -->
                <div id="auth-navbar" class="flex items-center gap-3 border-l border-gray-800 pl-8">
                    <!-- Guest -->
                    <div id="guest-zone" class="hidden items-center gap-5">
                        <a href="{prefix}utilisateur/login.html?tab=signup" class="text-[10px] font-black uppercase tracking-[0.2em] text-gray-500 hover:text-white transition-colors">S'inscrire</a>
                        <a href="{prefix}utilisateur/login.html?tab=login" class="bg-customOrange text-black px-5 py-2.5 rounded-xl font-black text-[10px] uppercase tracking-[0.1em] hover:bg-white hover:scale-105 transition-all shadow-xl shadow-customOrange/10">Connexion</a>
                    </div>
                    <!-- Member -->
                    <div id="member-zone" class="hidden items-center gap-4 bg-gray-950 border border-gray-900 px-4 py-2 rounded-2xl">
                        <div class="flex items-center gap-3 group cursor-pointer">
                            <div class="w-8 h-8 bg-customOrange/10 rounded-lg flex items-center justify-center text-customOrange group-hover:bg-customOrange group-hover:text-black transition-all">
                                <i class="fas fa-user-circle text-base"></i>
                            </div>
                            <div class="flex flex-col">
                                <span id="nav-user-name" class="text-[11px] font-black text-white leading-none"></span>
                                <a href="{prefix}utilisateur/profil.html" class="text-[9px] text-gray-600 font-bold uppercase tracking-tighter hover:text-customOrange transition-colors mt-1">Mon Profil</a>
                            </div>
                        </div>
                        <button onclick="handleLogout()" class="text-gray-700 hover:text-red-500 transition-colors ml-2 pt-1" title="Déconnexion">
                            <i class="fas fa-power-off text-xs"></i>
                        </button>
                    </div>
                </div>
            </nav>"""
 
    pattern = re.compile(r'<div class="container mx-auto flex flex-col md:flex-row justify-between items-center">.*?<nav.*?/nav>', re.DOTALL | re.IGNORECASE)
    
    new_content, count = pattern.subn(new_header_block, content)
    
    if count > 0:
        # Update search and scroll scripts
        # Ensure scripts are present at the end of body
        scripts_block = f"""
    <script src="{prefix}js/search_index.js"></script>
    <script src="{prefix}js/search_logic.js"></script>
    <script src="{prefix}js/scroll_to_search.js"></script>
</body>"""
        if "js/search_logic.js" not in new_content: # Check new_content after navbar update
            new_content = new_content.replace("</body>", scripts_block)
        elif "js/scroll_to_search.js" not in new_content: # Check new_content after navbar update
            # Upgrade existing scripts block
            new_content = new_content.replace('<script src="' + prefix + 'js/search_logic.js"></script>', 
                                      '<script src="' + prefix + 'js/search_logic.js"></script>\n    <script src="' + prefix + 'js/scroll_to_search.js"></script>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"SKIPPED {filepath} - Navbar pattern not found")

print("Navbar rebuild v6 completed.")

# Integrate search index synchronization
try:
    from sync_search_index import sync_search
    print("Synchronizing search index...")
    sync_search()
except ImportError:
    print("Could not import sync_search_index.py for automation.")

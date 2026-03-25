import os
import glob
import re

base_dir = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    if "rebuild_nav" in filepath or "update_nav" in filepath or "README" in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    rel_path = os.path.relpath(filepath, base_dir)
    dir_depth = rel_path.count(os.sep)
    prefix = "" if dir_depth == 0 else ("../" * dir_depth)
    
    new_ul = f"""<ul class="flex flex-wrap justify-center gap-x-5 gap-y-2 text-sm md:text-base font-medium">
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

                    <li><a href="{prefix}utilisateur/forum.html" class="text-gray-300 hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">💬 Forum</a></li>
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
                </ul>"""

    pattern = re.compile(r'<ul class="flex flex-wrap justify-center gap-x-5 gap-y-2 text-sm md:text-base font-medium">.*?</ul>', re.DOTALL | re.IGNORECASE)
    
    new_content, count = pattern.subn(new_ul, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"SKIPPED {filepath} - Navbar UL not found")

print("Navbar rebuild v3 completed.")

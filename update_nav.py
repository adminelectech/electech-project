import os
import glob
import re

base_dir = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

snippet_template = """
                    <!-- NEW HLEGA DROPDOWN -->
                    <li class="relative group">
                        <a href="{href}" class="text-customOrange font-bold transition-colors duration-300 flex items-center gap-1">
                            🎮 Hlega <i class="fas fa-chevron-down text-[10px]"></i>
                        </a>
                        <div class="absolute left-0 mt-3 w-48 bg-gray-900 border border-gray-800 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 overflow-hidden transform origin-top group-hover:scale-100 scale-95 text-left">
                            <ul class="py-2 text-sm font-medium">
                                <li><a href="{href}#qcm" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-question-circle w-5 text-gray-500"></i> QCMs Éclair</a></li>
                                <li><a href="{href}#jeux" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-gamepad w-5 text-gray-500"></i> Jeux Interactifs</a></li>
                                <li><a href="{href}#defis" class="block px-5 py-2.5 hover:bg-black hover:text-customOrange transition-colors"><i class="fas fa-trophy w-5 text-gray-500"></i> Défis & Amis</a></li>
                            </ul>
                        </div>
                    </li>
"""

for filepath in html_files:
    if "Hlega.html" in filepath: 
        continue 
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "🎮 Hlega" in content:
        continue # Already updated

    rel_path = os.path.relpath(filepath, base_dir)
    dir_depth = rel_path.count(os.sep)
    
    if dir_depth == 0:
        href = "Hlega/Hlega.html"
    else:
        href = "../" * dir_depth + "Hlega/Hlega.html"
        
    snippet = snippet_template.format(href=href)
    
    # regex matches any <li> containing a link to bibliotheque.html and the text 📚 Livres
    pattern = re.compile(r'([ \t]*)<li>\s*<a[^>]*bibliotheque\.html[^>]*>[^<]*📚\s*Livres[^<]*</a>\s*</li>', re.IGNORECASE | re.DOTALL)
    
    def replacer(match):
        indent = match.group(1)
        indented_snippet = snippet.replace('\n', '\n' + indent)
        return indented_snippet.lstrip('\n') + match.group(0)
    
    new_content, count = pattern.subn(replacer, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {rel_path} ({count} replacements)")
    else:
        print(f"Skipped {rel_path} (Livres link not found)")

print("Done.")

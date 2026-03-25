import os
import glob
import re

base_dir = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    if "update_nav" in filepath or "README" in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The original <a> tags might be split across lines, e.g. <a href="..." \n class="...">
    
    replacements = [
        (r'<a[^>]*href="([^"]*electrotechnique\.html)"[^>]*>\s*Électrotechnique\s*</a>',
         r'<a href="\1" class="hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">⚡ Électrotechnique</a>'),
         
        (r'<a[^>]*href="([^"]*electronique\.html)"[^>]*>\s*Électronique\s*</a>',
         r'<a href="\1" class="hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">🔌 Électronique</a>'),
         
        (r'<a[^>]*href="([^"]*energies\.html)"[^>]*>\s*Énergies\s*</a>',
         r'<a href="\1" class="hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">🔋 Énergies</a>'),
         
        (r'<a[^>]*href="([^"]*schemas\.html)"[^>]*>\s*Schémas\s*</a>',
         r'<a href="\1" class="hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">📐 Schémas</a>'),
         
        (r'<a[^>]*href="([^"]*forum\.html)"[^>]*>\s*Forum\s*</a>',
         r'<a href="\1" class="hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">💬 Forum</a>'),
         
        (r'<a[^>]*href="([^"]*bibliotheque\.html)"[^>]*>\s*(?:📚\s*)?Livres\s*</a>',
         r'<a href="\1" class="hover:text-customOrange font-bold transition-colors duration-300 flex items-center gap-1 border-b-2 border-transparent hover:border-customOrange pb-1">📚 Livres</a>')
    ]

    new_content = content
    modified = False
    
    for old_regex, new_replacement in replacements:
        new_content, count = re.subn(old_regex, new_replacement, new_content, flags=re.IGNORECASE)
        if count > 0:
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Style updated successfully.")

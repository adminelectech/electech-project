import re

filepath = r"c:\Users\mrchi\.gemini\antigravity\scratch\electrical_site\emploi\postale.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("Demandes d'Emploi", "Boîte Postale")
content = content.replace("Dépôt de Candidature Spontanée", "Boîte Postale & Contact")
content = content.replace("Espace Recrutement", "Espace Communication")
content = content.replace("Créez votre profil", "Envoyez-nous vos documents ou vos questions")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("postale.html customized successfully.")

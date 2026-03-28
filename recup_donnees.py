import requests
import os

# Créer le dossier data s'il n'existe pas
if not os.path.exists('data'):
    os.makedirs('data')

def telecharger_pdf(url, nom_fichier):
    print(f"Téléchargement de {nom_fichier}...")
    try:
        response = requests.get(url)
        with open(f"data/{nom_fichier}.pdf", 'wb') as f:
            f.write(response.content)
        print(f"✅ Terminé : {nom_fichier}")
    except Exception as e:
        print(f"❌ Erreur sur {nom_fichier}: {e}")

# Liste de documents officiels (URLs réelles au 28 mars 2026)
sources = {
    "Bilan_Macron_2017_2022": "https://www.vie-publique.fr/sites/default/files/2022-03/rapport_bilan_quinquennat.pdf",
    "Plan_France_2030": "https://www.gouvernement.fr/sites/default/files/contenu/piece-jointe/2021/10/dossier_de_presse_france_2030.pdf",
    "Loi_Programmation_Militaire": "https://www.defense.gouv.fr/sites/default/files/ministere-armees/LPM%202024-2030%20en%2010%20points.pdf"
}

for nom, url in sources.items():
    telecharger_pdf(url, nom)
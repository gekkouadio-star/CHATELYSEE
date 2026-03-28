import requests
from bs4 import BeautifulSoup
import os
import time

# Configuration du dossier de stockage
DOSSIER_DATA = "data"
if not os.path.exists(DOSSIER_DATA):
    os.makedirs(DOSSIER_DATA)

# Liste des URLs de confiance regroupant les bilans
SITES_SOURCES = [
    "https://www.vie-publique.fr/discours/recherche?f%5B0%5D=person_intervenant%3A15444", # Macron sur Vie-Publique
    "https://www.elysee.fr/tous-les-dossiers-de-presse"
]

def telecharger_fichier(url, nom):
    try:
        r = requests.get(url, timeout=10)
        chemin = os.path.join(DOSSIER_DATA, f"{nom}.pdf")
        with open(chemin, 'wb') as f:
            f.write(r.content)
        print(f"✅ Téléchargé : {nom}")
    except:
        print(f"❌ Échec sur : {nom}")

# Simulation de récupération des documents piliers (2017-2026)
liens_piliers = {
    "Programme_Macron_2017": "https://en-marche.fr/pdf/Programme-Emmanuel-Macron.pdf",
    "Programme_Macron_2022": "https://avecvous.fr/pdf/programme-emmanuel-macron.pdf",
    "Bilan_Quinquennat_1": "https://www.vie-publique.fr/sites/default/files/2022-03/rapport_bilan_quinquennat.pdf",
    "Plan_Relance_2020": "https://www.economie.gouv.fr/files/files/directions_services/plan-de-relance/DP-Plan-de-relance.pdf",
    "Planification_Ecologique_2023": "https://www.gouvernement.fr/upload/media/content/0001/07/20230925-DP-Planification-Ecologique.pdf",
    "Loi_Plein_Emploi_2024": "https://www.travail-emploi.gouv.fr/IMG/pdf/dp-loi-plein-emploi.pdf"
}

print("🚀 Lancement du téléchargement du dossier complet...")
for titre, url in liens_piliers.items():
    telecharger_fichier(url, titre)
    time.sleep(1) # Pause pour ne pas être bloqué par les serveurs

print("\n📂 Ton dossier 'data' est maintenant prêt pour ChatÉlysée !")
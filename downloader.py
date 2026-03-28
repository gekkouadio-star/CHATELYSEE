import requests

def download_pdf(url, filename):
    response = requests.get(url)
    with open(f"data/{filename}.pdf", 'wb') as f:
        f.write(response.content)
    print(f"✅ {filename} téléchargé.")

# Liste d'exemples de documents officiels réels
docs_officiels = {
    "Bilan_Industrie_2024": "https://www.institutmontaigne.org/ressources/pdfs/publications/politique-industrielle-quinquennat-macron-le-grand-decryptage.pdf",
    "Rapport_Cour_des_Comptes_2026": "https://www.ccomptes.fr/sites/default/files/2026-02/20260225-rapport-public-annuel-2026.pdf" 
}

for name, url in docs_officiels.items():
    try:
        download_pdf(url, name)
    except:
        print(f"❌ Erreur sur {name}")
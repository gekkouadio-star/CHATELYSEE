# 🤖 MoMoFr — Votre Assistant IA Intelligent 🇫🇷

**MoMoFr** est une application conversationnelle moderne et épurée, propulsée par l'intelligence artificielle de **Groq (Llama 3.1)**. Conçue avec une interface fluide inspirée de Gemini, elle offre une expérience utilisateur premium, rapide et sécurisée.

---

## ✨ Points Forts
* **Vitesse Éclair** : Réponses quasi instantanées grâce à l'infrastructure Groq.
* **Design Premium** : Interface "Gemini-style" avec entête fixe et zone de chat défilante.
* **Élégance à la française** : Un visuel soigné aux couleurs nationales, discret et professionnel.
* **Modèle Avancé** : Utilise `Llama-3.1-8b-instant` pour des échanges pertinents et fluides.
* 🔒 **Sécurisé** : Gestion des clés API via variables d'environnement.

---

## 🛠️ Installation Locale

Pour faire tourner **MoMoFr** sur votre machine :

1.  **Cloner le dépôt** :
    ```bash
    git clone [https://github.com/VOTRE_NOM_UTILISATEUR/MoMoFr.git](https://github.com/VOTRE_NOM_UTILISATEUR/MoMoFr.git)
    cd MoMoFr
    ```

2.  **Créer un environnement virtuel** (Optionnel mais recommandé) :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Mac/Linux
    ```

3.  **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurer la clé API** :
    Créez un fichier `.env` à la racine et ajoutez votre clé Groq :
    ```text
    GROQ_API_KEY=votre_cle_gsk_ici
    ```

5.  **Lancer l'application** :
    ```bash
    streamlit run app.py
    ```

---

## Déploiement
Ce projet est optimisé pour être déployé sur **Streamlit Cloud**. 
* N'oubliez pas d'ajouter votre `GROQ_API_KEY` dans les **Secrets** de l'application sur le dashboard Streamlit.

---

## 📁 Structure du Projet
* `app.py` : Le cœur de l'application (Interface & Logique).
* `.env` : (Ignoré par Git) Vos secrets bien gardés.
* `.gitignore` : Protection contre l'envoi de données sensibles ou lourdes.
* `requirements.txt` : La liste des ingrédients nécessaires.

---

## 🤝 Contact
Développé avec passion pour l'IA et le design moderne.  
*N'hésitez pas à poser vos questions à MoMoFr !*
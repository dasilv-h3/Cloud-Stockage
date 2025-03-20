# 📦 Azure Blob Storage - Gestion des Fichiers en Python  

Ce projet permet de stocker, lister, télécharger et sécuriser des fichiers sur **Azure Blob Storage** en utilisant **Python et le SDK Azure**.  

## 🛠 Prérequis  
- Un compte **Azure** avec un **Stockage Blob** configuré  
- **Python 3.8+** installé sur votre machine  
- **Azure CLI** (optionnel, pour gérer le stockage via la ligne de commande)  

---

## 🚀 Installation et Initialisation  

### 1️⃣ **Créer un environnement virtuel**  
Ouvrez un terminal et exécutez :  
```sh
python3 -m venv venv
```

Activer l'enrironnement virtuel : 

- Sur Windows : 
```sh
venv\Scripts\activate
```

- Sur MacOS / Linux : 
```sh
source venv/bin/activate
```

### 2️⃣ **Installer les dépendances**
Lancer sur le terminal :
```sh
pip install -r requirements.txt
```

### 3️⃣ **Configurer les accès à Azure**
Créez un fichier .env dans le dossier du projet et ajoutez vos informations Azure :
```sh
AZURE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=XYZ123...;EndpointSuffix=core.windows.net"
AZURE_ACCOUNT_KEY="votre_clé_secrète"
AZURE_CONTAINER_NAME="nom_du_conteneur"
```

### 4️⃣ **Lancer le script**
Lancer le script qui va upload, lister, download et générer une URL signée (SAS) pour un téléchargement sécurisé
```sh
python azure-storage.py
```
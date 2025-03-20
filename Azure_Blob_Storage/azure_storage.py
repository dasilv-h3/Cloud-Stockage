from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
CONNECTION_STRING = os.getenv("CONNECTION_STRING")

# Initialisation du client
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Fonction pour uploader un fichier
def upload_file(file_path):
    blob_name = os.path.basename(file_path)
    blob_client = container_client.get_blob_client(blob_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"✅ Fichier {blob_name} uploadé avec succès.")

# Fonction pour lister les fichiers
def list_files():
    print("📂 Fichiers dans le conteneur :")
    blobs = container_client.list_blobs()
    for blob in blobs:
        print(f"- {blob.name}")

# Fonction pour télécharger un fichier
def download_file(blob_name, destination_folder):
    blob_client = container_client.get_blob_client(blob_name)
    download_path = os.path.join(destination_folder, blob_name)

    with open(download_path, "wb") as file:
        file.write(blob_client.download_blob().readall())
    print(f"✅ Fichier {blob_name} téléchargé dans {destination_folder}")

# Générer une URL signée (SAS) pour un téléchargement sécurisé
def generate_sas_url(blob_name, expiry_minutes=60):
    from azure.storage.blob import generate_blob_sas, BlobSasPermissions
    from datetime import datetime, timedelta

    sas_token = generate_blob_sas(
        account_name=STORAGE_ACCOUNT_NAME,
        container_name=CONTAINER_NAME,
        blob_name=blob_name,
        account_key=CONNECTION_STRING,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now() + timedelta(minutes=expiry_minutes)
    )

    sas_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{blob_name}?{sas_token}"
    print(f"🔗 URL signée : {sas_url}")

# Exemple d'utilisation
if __name__ == "__main__":
    upload_file("test.png")  # Remplace par le chemin de ton fichier
    list_files()
    download_file("test.png", ".")
    generate_sas_url("test.png")

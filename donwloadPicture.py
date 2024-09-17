import csv
import requests

# Fonction pour télécharger une image à partir d'une URL
def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
            print(f"Image téléchargée avec succès: {filename}")
    else:
        print(f"Échec du téléchargement de l'image: {filename}")

# Chemin vers votre fichier CSV contenant les URL
csv_file = "informations_poissons.csv"

# Ouvrir le fichier CSV
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Pour sauter l'en-tête si nécessaire

    # Parcourir les lignes du fichier CSV
    for row in reader:
        url = row[0]  # La première colonne contient les URL
        name = row[1]  # La deuxième colonne contient les noms (optionnel)

        # Télécharger l'image à partir de l'URL
        if url:
            download_image(url, name + ".jpg" if name else "image_" + str(reader.line_num) + ".jpg")

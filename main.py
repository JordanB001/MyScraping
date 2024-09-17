from scraping import recuperer_informations_poissons
import csv

url_site_web = "https://www.fishipedia.fr/fr/poissons/list/quels-poissons-pour-un-aquarium-de-300-litres/?pg=1"

if __name__ == "__main__":

    # Appel de la fonction pour récupérer les informations sur les poissons depuis l'URL donnée
    poissons = recuperer_informations_poissons(url_site_web)
    print(poissons)

    if poissons:
        # Définition du chemin du fichier CSV
        fichier_csv = "informations_poissons.csv"

        # Écriture des informations dans le fichier CSV
        with open(fichier_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["image", "nom", "nomSavant", "habitat", "tailleAdulte", "sociabilite", "alimentation"])

            # Écriture de l'en-tête
            writer.writeheader()

            # Écriture des informations de chaque poisson
            for poisson in poissons:
                writer.writerow(poisson)

        print("Les informations ont été enregistrées dans le fichier", fichier_csv)




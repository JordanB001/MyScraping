import requests
from bs4 import BeautifulSoup
from dataWeb import donnes


# Fonction pour récupérer les informations sur les poissons à partir d'une URL donnée
def recuperer_informations_poissons(url):
    # Récupération du contenu HTML de la page web
    donneesWeb = donnes
    soup = BeautifulSoup(donneesWeb, 'html.parser')

    poissons = []
    # Extraction des informations sur les poissons à partir du contenu HTML

    poisson_All = soup.find_all("li", class_="aquarium-detail__card")

    for poisson in poisson_All:

        nom = poisson.find("h5").text
        nomSavant = poisson.find("p", class_="card-subtitle").text
        habitat = poisson.find("i")["data-original-title"]
        tailleAdulte = poisson.find("div", class_="card__medata card__medata--aquarium-item").text
        sociabilite = poisson.find_all("div", class_="card__medata card__medata--aquarium-item")[1].text
        alimentation = poisson.find_all("div", class_="card__medata card__medata--aquarium-item")[2].text

        try:
            image = poisson.find("img")["src"]
        except:
            image = ""

        poissons.append(
            {"image": image, "nom": nom, "nomSavant": nomSavant, "habitat": habitat, "tailleAdulte": tailleAdulte,
             "sociabilite": sociabilite, "alimentation": alimentation})
    return poissons
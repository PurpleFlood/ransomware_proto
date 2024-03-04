import os

def parcourir_dossiers(dossier):
    fichiers_trouves = []

    # Parcourir tous les fichiers et sous-dossiers dans le dossier donné
    for root, dirs, files in os.walk(dossier):
        for fichier in files:
            chemin_fichier = os.path.join(root, fichier)
            fichiers_trouves.append(chemin_fichier)

    return fichiers_trouves

# Exemple d'utilisation
dossier_debut = './test/'
resultat = parcourir_dossiers(dossier_debut)
print(resultat)
print(resultat[1])

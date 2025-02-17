taches = []

def ajouter_tache(tache):
    taches.append(tache)
    print(f"Tâche ajoutée : {tache}")

def afficher_taches():
    if not taches:
        print("Aucune tâche enregistrée.")
    else:
        print("\nListe des tâches :")
        for i, t in enumerate(taches, 1):
            print(f"{i}. {t}")

def supprimer_tache(index):
    try:
        tache = taches.pop(index - 1)
        print(f"Tâche supprimée : {tache}")
    except IndexError:
        print("Numéro de tâche invalide.")

# Test rapide
ajouter_tache("Faire les courses")
ajouter_tache("Réviser Git")
afficher_taches()
supprimer_tache(1)
afficher_taches()

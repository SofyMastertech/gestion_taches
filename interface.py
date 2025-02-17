import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox

FICHIER_TACHES = "taches.json"

class GestionnaireTaches(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestionnaire de Tâches")
        self.setGeometry(200, 200, 400, 300)

        self.layout = QVBoxLayout()

        self.liste_taches = QListWidget()
        self.layout.addWidget(self.liste_taches)

        self.input_tache = QLineEdit()
        self.layout.addWidget(self.input_tache)

        self.bouton_ajouter = QPushButton("Ajouter Tâche")
        self.bouton_ajouter.clicked.connect(self.ajouter_tache)
        self.layout.addWidget(self.bouton_ajouter)

        self.bouton_supprimer = QPushButton("Supprimer Tâche")
        self.bouton_supprimer.clicked.connect(self.supprimer_tache)
        self.layout.addWidget(self.bouton_supprimer)

        self.setLayout(self.layout)

        self.charger_taches()

    def ajouter_tache(self):
        tache = self.input_tache.text()
        if tache:
            self.liste_taches.addItem(tache)
            self.input_tache.clear()
            self.sauvegarder_taches()
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une tâche.")

    def supprimer_tache(self):
        selected_items = self.liste_taches.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Erreur", "Sélectionnez une tâche à supprimer.")
            return

        for item in selected_items:
            self.liste_taches.takeItem(self.liste_taches.row(item))

        self.sauvegarder_taches()

    def sauvegarder_taches(self):
        taches = [self.liste_taches.item(i).text() for i in range(self.liste_taches.count())]
        with open(FICHIER_TACHES, "w") as f:
            json.dump(taches, f)

    def charger_taches(self):
        try:
            with open(FICHIER_TACHES, "r") as f:
                taches = json.load(f)
                self.liste_taches.addItems(taches)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = GestionnaireTaches()
    fenetre.show()
    sys.exit(app.exec())
1
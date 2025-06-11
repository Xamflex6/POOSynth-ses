from abc import ABC, abstractmethod

class InterfacePourEtudiant(ABC):

    @abstractmethod
    def expliquerInterface(self):
        pass

class MaxLeGoat(InterfacePourEtudiant):
    def __init__(self, nom, prenom):
        super().__init__()
        self.nom = nom
        self.prenom = prenom
    
    def expliquerInterface(self):
        return "Une interface est un contrat : elle impose les méthodes à implémenter"
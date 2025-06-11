from abc import ABC, abstractmethod

class Abstraite(ABC):
    def __init__(self, param, nom):
        self.param = param
        self.nom = nom

    @abstractmethod
    def sePresenter(self):
        return f"bonjour je suis {self.nom}"

class EnfantAbstract(Abstraite):
    def __init__(self, param, nom, prenom):
        super().__init__(param, nom)
        self.prenom = prenom
    
    def sePresenter(self):
        return f"{super().sePresenter()} {self.prenom}"


e = EnfantAbstract("dev", "Max", "Le Goat")
print(e.sePresenter())

## 1. Concepts fondamentaux
### Objet
Un objet est une entité autonome regroupant :
- des attributs : variables propres à chaque instance
- des méthodes : fonctions propres à chaque instance, manipulant ses attributs
Chaque objet est une instance d'une classe donnée.
### Classe
Une classe est une structure générique décrivant les attributs et les méthodes communs à tous les objets de ce type. Elle représente le plan de construction des objets.
```class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

```
## 2. Encapsulation
### Définition
Principe fondamental qui consiste à masquer l'implémentation interne d'un objet (données), ne rendant accessibles que ce qui est nécessaire via des méthodes (interfaces).
### Accès contrôlés
- _attribut : usage protégé 
- __attribut : pseudo-privé 

 Obtenir la valeur d'un attribut donnée : Méthode d'accès
	Modifier le valeur d'un ou plusieurs attributs : Méthode d'altération
### Getters / Setters
Ils permettent de contrôler l'accès en lecture/écriture aux attributs.
```class Compte:
    def __init__(self, solde):
        self.__solde = solde
	
	@property
    def solde(self):
        return self.__solde

	@solde.setter
    def solde(self, solde):
        self.__solde = solde

```
#### Status d'accès
Par défaut, les attributs d'une classe sont privés et ses méthodes publiques
Un attribut qui peut être:
- Privé 
- Publique : Il peut directement accéder à l'attribut pour le modifier, lire.
## 3. Interface
l'interface d'une classe correspond aux informations dont on doit pouvoir disposer pour savoir utiliser celle-ci. Il s'agit:
- Du nom de la classe
- De la signature (nom de la fonction et type de paramètres) et du type de résultat éventuel de chacune de ces méthodes.
#### Le contrat d'une classe
Il correspond à son interface et à la définition de ses méthodes

### 3.1 L'implémentation
Cela correspond à l'ensemble des instructions de la classe écrite en vue de réaliser le contrat voulu
## 4. Constructeurs et surcharge
### Un constructeur
C'est une méthode particulière d'une classe, qui porte un nom conventionnel. Il peut:
- Disposer de paramètres
- Être appelé au moment de la création de l'objet, on peut lui fournir un ou plusieurs paramètres
 L'instanciation d'un objet va réaliser 2 opérations:
	- Allocation d'un emplacement mémoire pour notre objet
	- Appel éventuel de constructeurs existants
 Lorsqu'une classe dispose d'au moins un constructeur, il n'est plus possible d'instancier un objet sans qu'il fasse appel à un de ceux-ci.
### __init__
Méthode spéciale appelée automatiquement lors de la création d'une instance. Elle sert à initialiser les attributs de l'objet.
```class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

```
### Surcharge en Python
Python ne supporte pas la surcharge directe des méthodes. 
C'est un concept qui permet d'utiliser le même nom de méthode ou d'opérateur pour effectuer différentes actions selon un contexte. 
## 5. Mode de gestions des objets
### 5.1 Gestion par référence
- La mémoire statique est alloué au moment de la compilation et est utilisée pour les variables globales, les constantes ou les variables locales non dynamiques
- La mémoire dynamique est allouée pendant l'exécution du programme en créant l'objet. 
#### 5.1.1 La différence entre Mémoire dynamique et mémoire statique
La durée de vie:
- Mémoire statique: Dure pendant toute l'exécution du programme.
- Mémoire dynamique: Dure tant que l'objet est utilisé
## 6. Propriétés des objets et des méthodes
### 6.1 Affectation et Comparaison des objets
 Affectation = Donner à une variable la référence d'un objet
 Comparaison = Comparer les références d'un objet
## 7. Méthodes et références
### self
Mot-clé obligatoire pour référencer l'objet appelant dans une méthode d'instance.
### Références et copies
- a = b : a et b référencent le même objet
- Pour copier un objet indépendamment :
```import copy
b = copy.deepcopy(a)

```
## 8. Méthodes de classe et attributs de classe
### Attribut de classe
Variable partagée par toutes les instances de la classe. Définie hors de __init__.
```class Compteur:
    instances = 0

    def __init__(self):
        Compteur.instances += 1

```
### Méthodes de classe
Utilisent le décorateur @classmethod et accèdent à la classe via cls.
```class Point:
    def __init__(self, abs, ord):
        self.abs = abs
        self.ord = ord

    @classmethod
    def coincident(cls, p1, p2):
        return p1.abs == p2.abs and p1.ord == p2.ord

# Test
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 5)

print(Point.coincident(p1, p2))  # True
print(Point.coincident(p1, p3))  # False
```
 Elle sert pour accéder et modifier des attributs de classe, ou créer des objets à partir d'une classe. 
## 9. Tableaux d'objets
### Utilisation
Listes de plusieurs objets (En Python):
```points = [Point(1,2), Point(3,4)]
for p in points:
    p.affiche()

```

## 10. Héritage
### Définition

Une classe peut hériter d'une ou plusieurs autres classes :
- permet la réutilisation de code
- favorise la spécialisation
```class Animal:
    def parler(self):
        print("Je suis un animal")

class Chien(Animal):
    def parler(self):
        print("Ouaf")

```
### super()
Permet d'appeler des méthodes de la classe parente.
```def __init__(self, nom):
    super().__init__()

```
### 10.1 Héritage Multiple
C'est lorsqu'une classe hérite de plus d'une classe parent. Cela permet à une classe d'avoir les attributs et méthodes de plusieurs classes.
```class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_coordonnees(self):
        print(f"Coordonnées : ({self.x}, {self.y})")

class Couleur:
    def __init__(self, couleur):
        self.couleur = couleur

    def afficher_couleur(self):
        print(f"Couleur : {self.couleur}")

# Héritage multiple
class PointColore(Point, Couleur):
    def __init__(self, x, y, couleur):
        Point.__init__(self, x, y)
        Couleur.__init__(self, couleur)

    def afficher(self):
        self.afficher_coordonnees()
        self.afficher_couleur()

pc = PointColore(3, 4, "rouge")
pc.afficher()

```
#### Résultat :
```Coordonnées : (3, 4)
Couleur : rouge
```
## 11. Polymorphisme
### Définition
Capacité à utiliser des objets de classes différentes via une même interface.
```def fait_parler(animal):
    animal.parler()

```
Chaque classe qui définit parler sera compatible, même si elle est différente.
## Surdéfinition et Redéfinition
- Surdéfinition = Plusieurs méthodes accessibles, identifiées par leur signature
- Redéfinition = Une seule méthode accessible à un objet de type donné : Une redéfinition masque une méthode de même nom d'un parent
## 12. Composition
### Définition
Relation de type a un : un objet est composé d'autres objets.
C'est le fait qu'une méthode appelle une autre méthode d'une autre classe
```class Adresse:
    def __init__(self, ville):
        self.ville = ville

class Personne:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

```
## 13. Objets comme paramètres et retours
### Passage par référence
Les objets passés à une fonction peuvent être modifiés, car la référence est transmise.
### Objet en retour
Une méthode peut créer et retourner un objet :
```def symetrie(self):
    return Point(-self.x, -self.y)

```
## 14. Exceptions
### Gestion d'erreurs
Empêche un programme de crasher lorsqu'une situation inattendue se produit.
```try:
    x = int(input("Nombre : "))
except ValueError:
    print("Erreur : entier attendu")

```
Possibilité d'utiliser else et finally.
## 15. Classes abstraites et interfaces
### ABC - Classe abstraite
Permet de définir une structure obligatoire pour les sous-classes.
```from abc import ABC, abstractmethod

class Abstraite(ABC):
    def __init__(self, param, nom):
        self.param = param
        self.nom = nom

    @abstractmethod
    def sePresenter(self):
        return f"bonjour je suis {self.nom}"

class EnfantAbstraite(Abstraite):
    def __init__(self, param, nom, prenom):
        super().__init__(param, nom)
        self.prenom = prenom
    
    def sePresenter(self):
        return f"{super().sePresenter()} {self.prenom}"


e = EnfantAbstraite("dev", "Max", "Le Goat")
print(e.sePresenter())

```
#### ABC - Interface
Une interface est un contrat : elle impose les méthodes à implémenter
```from abc import ABC, abstractmethod

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
```
## 16. Autoréférence (courant)
### self comme référence à l'objet
Utile pour transmettre l'objet courant à une autre méthode ou pour les comparaisons internes.
## 17. Chaînes et classes utilitaires
### Chaînes
Manipulation facile avec la classe str :
```nom = " Bonjour le monde "
print(nom.upper()) #Affiche BONJOUR LE MONDE
print(nom[0]) #Affiche B
print(nom.find("le")) #Affiche 8
print(nom.replace("le", "la")) #Affiche Bonjour la monde
print(nom.split()) #Affiche ['bonour', 'le', 'monde']

```
Fonctions utiles : .find(), .replace(), .split(), etc.
## 
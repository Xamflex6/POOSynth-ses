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
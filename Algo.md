### Définitions fondamentales
Algorithme : Suite finie d'étapes permettant de résoudre un problème.
Spécification d’un problème :
- Entrées : les données décrivant le problème
- Pré-condition : contraintes sur les entrées
- Sorties : résultats attendus
- Post-condition : relation entrée → sortie
### Notion de complexité
Complexité temporelle : mesure du temps d’exécution d’un algorithme en fonction de la taille de l’entrée n. Notée avec la notation grand O O(...).
#### Cas fréquents :
- O(1) – Temps constant : temps fixe, peu importe la taille des données
- O(log n) – Logarithmique : divise les données à chaque étape
- O(n) – Linéaire : dépend directement du nombre d’éléments
- O(n log n) – Quasi-linéaire : typique des bons algorithmes de tri
- O(n²) – Quadratique : deux boucles imbriquées, temps doublement proportionnel
- O(2ⁿ) – Exponentielle : temps explose avec la taille (cas récursifs non optimisés)
#### Remarques :
- Le pire cas est généralement analysé (ex : complexité asymptotique)
- Le meilleur cas ou cas moyen peuvent être différents
- La tendance est ce qui compte (grande taille de données)
## 1. Les listes chaînées
C'est une structure de donnée dynamique composée de noeuds.
Chaque noeuds contient:
1. Une valeur
2. Un lien vers le noeud suivant

## 2. Les piles et Files
### 2.1 Les piles (Stacks)
Last In First Out (LIFO) → Le dernier élément ajouté est le premier à sortir. 

### 2.2 Les files (Queues)
First In First Out (FIFO) → Le premier élément ajouté est le premier à sortir.
## 3. Algorithmes à connaître
### Compression LZW
Permet de réduire la taille d'un fichier sans perte d'aucune informations
- Utilisé pour les .GIF, .PDF
- Regroupement de symboles en chaînes
- convertir chaînes en code
> Comment ça fonctionne? 
	1. On commencer avec un dictionnaire contenant tous les caractères possibles
	2. On lit les données caractères par caractères
	3. On cherche les séquences répétées
	4. à chaque nouvelles séquences on l'ajoute au dictionnaire avec un code numérique
	5. On remplace les séquences par leurs codes

### Codage Huffman statique
Permet de compresser des données en attribuant à chaque symbole un code binaire plus ou moins long selon la fréquence d'apparition
- Compression efficace pour les textes avec beaucoup de répétions
- L'arbre d'Huffman doit être envoyé avec le message compressé pour permettre la décompression
> Comment ça fonctionne? 
	1. Compter les fréquences de chaque caractères dans le texte
	2. Créer un arbre binaire
	3. Attribuer un code binaire à chaque caractère
	4. Remplacer chaque caractère du texte par son code binaire

### RLE
Algorithme de compression sans perte qui remplace les séquences d'un même caractère par le suivi du nombre de répétitions
> Exemple:
	Chaîne originale: BBBBHHDDXXXXKKKKWWZZZZ

	Compression RLE: B4H2D2X4K4W2Z4


### Différence entre chiffrement symétrique et chiffrement asymétrique
- Asymétrique: Utilise deux clé. Une clé privée pour déchiffrer et une clé publique pour chiffrer
- Symétrique: Une seule clé est utilisée pour chiffrer et déchiffrer les données

### RSA
Algorithme de chiffrement asymétrique
Le but de cet algorithme est de multiplier deux grands nombres premiers entre eux et ainsi retrouver p et q qui sont les nombres premiers, à partir de leurs produits.

### Les tours d'Hanoï
> Le principe:
	- 3 tours (A, B, C)
	- Plusieurs disques de tailles différentes empilées sur la tour A (du plus grand au plus petit)
	- Le but est de déplacer tous les disques de la tour A vers la tour C en respectant 2 règles. (Une seul disque à la fois peut être déplacé et un disque ne peut jamais être posé sur un disque plus petit)
 Répétition de processus de manière Récursive
### Problème du drapeau Hollandais
Problème qui consiste à trier une liste contenant trois types d'éléments. 
 Utilisé dans des algo comme le tri rapide

### Le Hachage
Le Hachage consiste à transformer une donnée en une valeur fixe appelée empreinte ou hash à l'aide d'une fonction de hachage
 Il y a les collisions (Exemple avec la probabilité que dans un groupe de 23 personnes. Deux personnes ait leurs anniversaire le même jour)
#### Le salage
Le fait d'ajouter un élément à la donnée pour en modifier la signature

## 4. Algorithmes de tri
### 4.1 Tri à bulles
On compare chaque pair d'éléments voisins et on les échange s'ils sont dans le mauvais ordre. On répète jusqu'à ce que la liste soit triée
### 4.2 Tri par insertion
On construit une liste triée éléments par éléments, en insérant chaque nouvel élément à sa place dans la partie déjà triée. 
### 4.3 Tri par fusion
On divise la liste en deux, et on trie chaque moitié récursivement. Ensuite, on fusionne les deux moitiés triées
### 4.4 Tri rapide
On choisit un pivot, on place les éléments plus petits à gauche, les plus grands à droite et on trie récursivement chaque partie. 
### 4.5 Tri par tas
On construit un tas binaire, ensuite on extrait les éléments un par un pour les placer dans l'ordre. 

## 5. Les arbres
> Qu'est-ce qu'un arbre? 
	Structure de donnée hiérarchique composée de noeuds reliés entre eux(racine, noeuds, leaf,…):
> à quoi ça sert ? 
	- Organiser les données de manière hiérarchique
	- Rechercher efficacement
	- Trier des données
	- Parcourir des structures complexes
	- Optimiser des algorithmes

### 5.1 Les arbres binaires
 Structure de données dans laquelle chaque noeuds peut avoir maximum deux enfants 
> Il existe deux manières de parcourir un arbre binaire:
	1. Parcourir en profondeur
		Préfixe : Racine → Gauche → droite
		Infixe : Gauche → Racine → Droite
		Postfixe : Gauche → Droite → Racine
	2. Parcourir en largeur
		Niveau par niveau, de gauche à droite.

## 6. Le pathfinding

C'est un algorithme qui consiste à trouver le chemin optimal entre deux points dans un espace donné.

### 6.1 La théorie des graphes
Un graphe est un couple G = (V,E) où:
- V est un ensemble de sommets (Noeuds)
- E est un ensemble d'arêtes (liens) reliant les sommets
### 6.2 L'algorithme de Dijkstra
Le concept est de trouver le chemin le plus court entre un sommet de départ et tous les autres sommets d'un graphe, en minimisant la somme des poids des arêtes empruntées ( les poids doivent être positifs)
> Fonctionnement:
	1. On attribue une distance infinie à tous les sommets sauf au sommet de départ et on créé un ensemble de sommets non visités
	2. On séléctionne le sommet courant
	3. On mets à jour les voisins
	4. On marque le sommet comme visité
	5. On répète

### 6.3 L'algorithme de Floyd-Warshall
Le concept est de trouver la distance minimale entre chaque paire de sommets dans un graphe. Même s'il n'y a pas de chemin direct entre eux. (Les poids peuvent être négatifs ou positifs au contraire de l'algo de dijkstra)
> Fonctionnement:
	1. On initialise une matrice de distances D
	2. Pour chaque sommets, on mets à jour la distance ( on compare pour conserver le plus court et on compare pour toutes les paires)

### 6.4 L'algorithme de A*
Le concept est de trouver le chemin le plus court entre deux points dans un graphe ou dans une grille, en minimisant le coût total.
> Fonctionnement:
	1. Le coût réel pour aller du départ jusqu'au point actuel → noté g(n)
	2. Une estimation du coût restant pour aller du point actuel à la destination noté → h(n) ← fonctionne heuristique.
	3. Somme congru f(n) = g(n) + h(n)

### 6.5 Heuristique
Le concept est une estimation de la distance ou le coût restant entre un noeud actuel et le but

> Bonnes propriétés d'une heuristique
	1. Admissible : Elle ne surestime jamais le vrai coût et garanti le chemin optimal
	2. Consistante : Elle respecte une certaine cohérence entre les noeuds voisins

 Exemples:
	- Distance de Manhattan:
		Utilisée sur des grilles où on ne peut se déplacer que horizontalement ou verticalement
	- Distance Euclidienne:
		Utilisée quand on peut se déplacer en diagonale

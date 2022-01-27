#Je crée la class Player, où l'on peut trouver le nom du joueur et 
#la liste des scores qu'il a obtenu en jeu à chaque chanson auquel il a joué
class Player:
    def __init__ (self, name, listscore, icon):
        self.__name = name
        self.__listscore = listscore
        self.__icon = icon

    def getName(self):
        return self.__name
    
    def getIcon(self):
        return self.__icon

#J'accueille le joueur et lui permet de personnaliser son profil en lui demandant son nom et une icone
print ("*~-Bienvenue dans Karaoke-~*")
name = int(input("Créons votre profil Player 1. Quel est votre nom :"))
print = int(input("Choisissez votre icon de profil : 1.👧 2.👦 3.👩 4.👨 5.🐶 6.🐱 = "))

player1 = Player("icon", "name", "listscore")
player2 = Player("icon", "name", "listscore")
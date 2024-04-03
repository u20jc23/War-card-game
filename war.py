from random import shuffle
class Carte:
    coul = ['♠', '♥', '♦', '♣']
    valeurs= [None, None, '2','3','4','5','6','7','8','9','10','Valet', 'Dame', 'Roi', 'As'] 

    def __init__(self, val, coul): #la carte (valeur + couleur) est un int
        self.valeur = val
        self.couleur = coul

    def __lt__(self, c2): # sert a savoir si self<c2 (si une carte est supérieur a une autre ou non)
        if self.valeur < c2.valeur:
            return True
        if self.valeur == c2.valeur: 
            if self.couleur < c2.couleur:
                return True
            else:
                return False
        return False
    
    def __eq__(self, c2):  #pour savoir s'il y a égalitée 
      if self.valeur == c2.valeur: 
        return True 
      else:
        return False
    
    def __gt__(self, c2): #savoir si self>c2
        if self.valeur > c2.valeur: 
            return True
        if self.valeur == c2.valeur:
            if self.couleur > c2.couleur:
              return True 
            else:
                return False
        return False

    def __repr__(self):
        v = self.valeurs[self.valeur] + self.coul[self.couleur]
        return v




class jeuCarte:
    def __init__(self):
        self.cartes = []
        for i in range(2,15): #on va de 2 a 14 vue que le 14 c'est le AS donc la valeur la plus forte
            for j in range(4):
                self.cartes.append(Carte(i,j))

        shuffle(self.cartes)

    def enlever_Carte(self):
        if len(self.cartes) == 0:
            return  #si sa block sa renvoie none 

        return self.cartes.pop()

class Joueur:
    def __init__(self, nom):
        self.nom = nom # nom du joueur
        self.Carte = None # carte en main du joueur 
        self.victoire = 0

class Jeu:
    def __init__(self):
        nom1 = input('nom du joueur 1?')
        nom2 = input('nom du joueur 2?')
        self.jeu = jeuCarte()
        self.j1 = Joueur(nom1)
        self.j2 = Joueur(nom2)

    def victoire(self, gagnant):
        v = "{} a gagner ce tour"
        v = v.format(gagnant)
        print(v)

    def tirer(self, j1n, j1c, j2n, j2c):
        t = "{} a tirer {}, {} a tirer {}"
        t = t.format(j1n, j1c, j2n, j2c)
        print(t)

    def jouer(self):
        cartes = self.jeu.cartes 
        print('la bataille commence!!!')
        while len(cartes) > 2:
            m = 'q pour quitter.' + 'entrer pour continuer.'
            reponse = input(m)
            if reponse == 'q':
                break
            j1c = self.jeu.enlever_Carte() # enleve la premiere carte du joueur 1 
            j2c = self.jeu.enlever_Carte() 
            j1n = self.j1.nom
            j2n = self.j2.nom
            self.tirer(j1n, j1c, j2n, j2c)

            if j1c.valeur > j2c.valeur:
                self.j1.victoire +=1
                self.victoire(self.j1.nom)
            elif j1c == j2c:
                print ('Il y a bataille')
                while j1c == j2c:
                  for i in range (2):
                    j1c = self.jeu.enlever_Carte()
                    j2c = self.jeu.enlever_Carte()
                    j1n = self.j1.nom
                    j2n = self.j2.nom
                    self.tirer(j1n, j1c, j2n, j2c)
                  if j1c > j2c:
                      self.j1.victoire +=1
                      self.victoire(self.j1.nom) 
                  elif j1c < j2c:
                      self.j2.victoire += 1
                      self.victoire(self.j2.nom)

            else:
                self.j2.victoire += 1
                self.victoire(self.j2.nom)

        gagnant = self.gagnant(self.j1, self.j2)
        print("La battaille est terminer. {} a gagner".format(gagnant))

    def gagnant(self, j1, j2):
        if j1.victoire > j2.victoire:
            return j1.nom
        if j1.victoire < j2.victoire:
            return j2.nom
        return 'il y a égalité!'

jeu = Jeu()
jeu.jouer()

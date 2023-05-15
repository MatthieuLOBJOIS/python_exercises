class Voiture : 
    def __init__(self) : 
        self.essence = 100
        
    def afficher_reservoir(self) : 
        print(f"La voiture contient {self.essence if self.essence > 0 else 0} litres d'essence")
        
    def roule(self, km : int) : 
        
        if self.essence <= 0 : 
            print(f"Vous n'avez plus d'essence, faites le plein !")
            return
        
        self.essence -= (km * 5)/100
        
        if self.essence <= 10 and self.essence > 0 : 
            print(f"Vous n'avez bientôt plus d'essence !")
        
        self.afficher_reservoir()

    def faire_le_plein(self) : 
        self.essence = 100

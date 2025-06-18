

class Personaje:
    
    def __init__(self, nombre = "orco"):

        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0


    @property
    def estado(self):
        return  f"el nombre es : {self.nombre} el nivel es : {self.nivel} la exp es : {self.experiencia}"
    
    @estado.setter
    def estado(self, exp):

        tmp_exp = self.experiencia + exp
        #SUBIR NIVEL
        while tmp_exp > 99:
            self.nivel += 1
            tmp_exp -= 100

        #bajar de nivel
        while tmp_exp < 0:
            if self.nivel == 1:
                self.experiencia = 0
                tmp_exp = 0
            else:
                self.nivel -= 1
                tmp_exp += 100
        
        self.experiencia = tmp_exp


    def __lt__(self, oponente):
        # sobrecarga para metodo de menor que implementado para mis instancias
        return self.nivel < oponente.nivel
    
    def __gt__(self , oponente):
        # sobrecarga para metodo de mayor que implementado para mis instancias
        return self.nivel > oponente.nivel
    
    # sobrecarga para metodo de igual que implementado para mis instancias
    def __eq__(self, oponente):
         return self.nivel == oponente.nivel
    

    def probabilidad(self , oponente):
        """
        ○ Si el jugador es menor al orco, tiene un 33% de probabilidades de ganar.
        ○ Si el jugador es mayor al orco, tiene un 66% de probabilidades de ganar.
        ○ Si el jugador es igual al orco, tiene un 50% de probabilidades de ganar.

        """
        if self < oponente:
            return 33
        elif self > oponente:
            return  66
        else:
            return 50


    @staticmethod   
    def mostrar_dialogo(prob):
        return int(input(f"""
¡Oh no!, ¡Ha aparecido un Orco!
Con tu nivel actual, tienes {prob}% de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
¿Qué deseas hacer?
1. Atacar
2. Huir"""))
    






    


    

        



           
    



    def __str__(self):
        return f"{self.nombre}"













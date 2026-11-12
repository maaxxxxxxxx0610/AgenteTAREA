from mesa import Model 
from mesa.space import MultiGrid
from agente import Carro, Semaforo


class ModeloInterseccion(Model): 


    def __init__(self, width = 15, height = 15, num_carros=5):
        super().__init__()
        self.grid = MultiGrid(width, height, torus=True)
        self.centro = width//2
        self.buzon = []
        self.programa_Luces = []

        semHor = Semaforo(self, "H")
        semVer = Semaforo(self, "V")
        self.semaforos = {"H": semHor, "V": semVer}


        self.grid.place_agent(semHor, (self.centro - 1, self.centro + 1))
        self.grid.place_agent(semVer, (self.centro + 1, self.centro - 1))


        posIniciales = [
            ((1, self.centro), "H"),
            ((4, self.centro), "H"),
            ((self.centro, 1), "V"),
            ((self.centro, 2), "V"),
            ((0, self.centro), "H"),


        ]

        for pos, dirCarro in posIniciales[:num_carros]:
            carro = Carro(self, direccionCarro=dirCarro, velocidad=1)
            self.grid.place_agent(carro, pos)




    def step(self): 
        self.buzon = []

        self.agents_by_type[Carro].do("step")

        if len(self.buzon) == 0: 
            self.semaforos["H"].estado = "yellow"
            self.semaforos["V"].estado = "yellow"

            self.programa_Luces =[]
        else: 
            #ordenar por menor tiempo estimado de arriba osea el eta q hice

            mensajes_ordenados = sorted(self.buzon, key=lambda m: m["eta"])
            self.programa_Luces = mensajes_ordenados

            #el mas cerca gana el verde
            ganador = mensajes_ordenados[0]["direccion"]
            perdedor = "V" if ganador == "H" else "H"


            self.semaforos[ganador].estado = "green"
            self.semaforos[perdedor].estado = "red"
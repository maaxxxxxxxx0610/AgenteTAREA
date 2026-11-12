from mesa import Agent

#H == horizontal 
#V == Vertical 

class Semaforo(Agent):
    def __init__ (self, model, direccion):
        super().__init__(model)
        self.direccion = direccion
        self.estado = "yellow"


    def step(self): 
        pass


class Carro(Agent): 
    def __init__(self, model, direccionCarro, velocidad = 1):
        super().__init__(model)
        self.direccionCarro = direccionCarro
        self.velocidad = velocidad

    def step(self):
        x, y = self.pos
        cruce = self.model.centro

        if self.direccionCarro == "H": 
            distancia = (cruce -1) - x if x <= cruce - 1 else -1
        else: 
            distancia = (cruce - 1) - y if y <= cruce - 1 else -1



        if 0 <= distancia <= 5: 
            eta = distancia/ self.velocidad 
            self.model.buzon.append({
                "id": self.unique_id,
                "direccion": self.direccionCarro,
                "eta": eta
            })


        semaforoActual = self.model.semaforos[self.direccionCarro].estado
        avanzar = True


        if distancia == 0 and semaforoActual != "green": 
            avanzar = False


        if avanzar:
            sigX = (x + self.velocidad) % self.model.grid.width if self.direccionCarro == "H" else x  
            sigY = (y + self.velocidad) % self.model.grid.width if self.direccionCarro == "V" else y


            contenido = self.model.grid.get_cell_list_contents([(sigX, sigY)])
            hayCarro = any(isinstance(a, Carro) for a in contenido)


            if not hayCarro:
                self.model.grid.move_agent(self, (sigX, sigY))
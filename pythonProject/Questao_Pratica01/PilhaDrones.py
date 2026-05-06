from Drone import Drone

class PilhaDrones:
    def __init__(self):
        self.topo = None

def printDrone(self):
    print("---------------------------------")
    if self.topo is None:
        print("\nPilha de drones vazia!")
    else:
        print("\nPilha de Drones:")
        aux = self.topo
        while aux:
            print(aux)
            aux = aux.prox
    print("---------------------------------")

def addDrone(self, drone):
    if self.topo is not None:
        drone.prox = self.topo
    self.topo = drone
    self.printDrone()

def remDrone(self):
    if self.topo is not None:
        aux = self.topo
        self.topo = self.topo.prox
        del (aux)
    self.imprimir()
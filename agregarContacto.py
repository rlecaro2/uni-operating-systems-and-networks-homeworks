from proceso import Proceso

class agregarContacto(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        
        self.nombreContacto = args[4]
        self.numeroContacto = args[5]

        #variables especificas de llamadas

    def imprimir(self):
        return self.fecha + " - Contacto agregado. Nombre: " + self.nombreContacto + ", numero: " + self.numeroContacto +"."
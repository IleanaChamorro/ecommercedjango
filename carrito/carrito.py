class Carrito:
     #Almacenar peticion compra
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro=carro


    def agregar(self, productos):
        if(str(productos.id) not in self.carro.keys()):
            self.carro[productos.id]={
                "productos_id":productos.id,
                "nombre":productos.nombre,
                "precio":str(productos.precio),
                "cantidad":1,
                "imagen":productos.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key==str(productos.id):
                    value["cantidad"]=value["cantidad"]+1
                    break 
        self.guardar_items()

    #Actualizar session
    def guardar_items(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar_items(self, productos):
        productos.id=str(productos.id)
        if productos.id in self.carro:
            del self.carro[productos.id]
            self.guardar_carro()

    def quitar_items(self, productos):
        for key, value in self.carro.items():
            if key==str(productos.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar_items(productos)
                break
        self.guardar_items()

    def limpiar_carro(self):
        carro=self.session["carro"]={}
        self.session.modified=True
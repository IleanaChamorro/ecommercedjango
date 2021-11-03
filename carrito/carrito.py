class Carro:
    #Almacenar peticion compra
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")

        if not carrito:
            carrito=self.session["carrito"]={}
        else:
            self.carrito=carrito

    def agregar(self, productos):
        if(str(productos.id) not in self.carrito.keys()):
            self.carrito[productos.id]={
                "productos_id":productos.id,
                "nombre":productos.nombre,
                "precio":str(productos.precio),
                "cantidad":1,
                "imagen":productos.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(productos.id):
                    value["cantidad"]=value["cantidad"]+1
                    break 
        self.guardar_items()

    #Actualizar session
    def guardar_items(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar_items(self, productos):
        productos.id=str(productos.id)
        if productos.id in self.carrito:
            del self.carrito[productos.id]
            self.guardar_items()

    def quitar_items(self, productos):
        for key, value in self.carrito.items():
            if key==str(productos.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar_items(productos)
                break
        self.guardar_items()

    def limpiar_carro(self):
        self.session["carrito"]={}
        self.session.modified=True
class Carrito:
    def __init__(self, request):
        #Almacenar peticion compra
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro=carro


    def agregar(self, producto):
        if(str(productos.id) not in self.carro.keys()):
            self.carro[productos.id]={
                "productos_id":productos.id,
                "nombre":productos.nombre,
                "precio":str(productos.precio),
                "cantidad":1,
                "imagen":productos.imagen.url,
            }

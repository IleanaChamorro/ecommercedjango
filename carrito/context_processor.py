from .carrito import Carro
def importe_total_carro(request):
    carro=Carro(request)
    total=0
    print(request.session)
    if request.user.is_authenticated:
        for key,value in request.session["carrito"].items():
            total=total+(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}

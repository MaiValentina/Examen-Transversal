productos = {"8475HD":["HP",15.6,"8GB","DD","1T","Intel Core i5","Nvidia GTX1050"],
         "2175HD":["Lenovo",14,"4GB","SSD","512GB","Intel Core i5","Nvidia GTX1050"],
         "JjfFHD":["Asus",14,"16GB","SSD","256GB","Intel Core i7","Nvidia RTX2080Ti"],
         "fgdxFHD":["HP",15.6,"8GB","DD","1T","Intel Core i3","integrada"],
         "GF75HD":["Asus",15.6, "8GB","DD","1T","Intel Core i7","Nvidia GTX1050"],
         "123FHD":["lenovo",14, "6GB","DD","1T","AMD Ryzen 5", "integrada"],
         "342FHD":["lenovo",15.6,"8GB","DD","1T", "AMD Ryzen 7", "Nvidia GTX1050"],
         "UWU131HD":["Dell",15.6, "8GB", "DD", "1T","AMD Ryzen 3", "Nvidia GTX 1050"],
}
Stock = {
    "8475HD": {"marca": "HP", "precio": 1500000, "stock": 15},
    "2175HD": {"marca": "Lenovo", "precio": 1000000, "stock": 10},
    "JjfFHD": {"marca": "Asus", "precio": 1650000, "stock": 12},
    "fgdxFHD": {"marca": "HP", "precio": 220000, "stock": 2},
    "GF75HD": {"marca": "Asus", "precio": 125000, "stock": 21},
    "123FHD": {"marca": "lenovo", "precio": 1920000, "stock": 13},
    "342FHD": {"marca": "lenovo", "precio": 2500000, "stock": 11},
    "UWU131HD": {"marca": "Dell", "precio": 330000, "stock": 27},
    }
def stockdemarca(stock):
    print(f"el stock de la marca es {stock}:")

def stock_marca(marca):
    print(f"Modelos de la marca {marca}:")
    found = False
    for modelo, datos in Stock.items():
        if datos["marca"] == marca:
            print(f" - {modelo}")
            found = True
    if not found:
        print("No se encontraron modelos de esa marca.")

def busqueda_precio(precio_min, precio_max):

    resultados = []
    for modelo, datos in Stock.items():
        if datos["stock"] != 0 and precio_min <= datos["precio"] <= precio_max:
            resultados.append(f"{datos['marca']}-{modelo}")
    resultados.sort()
    if resultados:
        print("modelos en rango de precio con stock:")
        for item in resultados:
            print(item)
    else:
        print("No hay notebooks en ese rango de precio")
def actualizar_precio(modelo, p):

    if modelo in Stock:
        Stock[stock_marca]["precio"] = p
        return True
    else:
        return False
def main():
    while True:
        print("menu principal")
        print("1- Mostrar el stock de una marca")
        print("2- Buscar notebooks por un rango de precio")
        print("3- Actualizar el precio de un modelo")
        print("4- Salir")
        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            marca = input("Ingrese la marca a consultar: ")
            stockdemarca(Stock)

        elif opcion == "2":
      
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    precio_max = int(input("Ingrese precio máximo: "))
                    if precio_min > precio_max:
                        print("El precio mínimo no puede ser mayor que el maximo, intente nuevamente")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese valores enteros para los precios.")
            busqueda_precio(precio_min, precio_max)

        elif opcion == "3":
            modelo = input("Ingrese el modelo: ")
            while True:
                try:
                    p = int(input("Ingrese el nuevo precio: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un valor entero para el precio.")
            resultado = actualizar_precio(modelo, p)
            if resultado:
                print("el precio esta actualizado")
            else:
                print("modelo no existe")

            resp = input("¿Desea actualizar otro precio? (si/no): ")
            if resp != "si":
                continue  
        elif opcion == "4":
            print("Programa Finalizado")
            break

        else:
            print("Debe seleccionar una opcion valida")
if __name__ == "__main__":
    main()
# Creación o lectura de la base de datos
try:
    fichero = open("bbdd.txt", "r")
except:
    fichero = open("bbdd.txt", "x")

# Ver los productos del inventario
def ver_productos():
    inventario = puta_funcion_lectura()
    for i in inventario:
        print(i, "\n")
# Añadir un nuevo producto
def nuevo_producto():
    nombre_producto = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
    with open("bbdd.txt","a") as fichero:
        fichero.write(f"{nombre_producto}/{precio}/{cantidad}\n")
    print(f"Se ha creado el producto {nombre_producto}, con un precio de {precio}€ y una cantidad de {cantidad} unidades")

# Actualizar la cantidad de un producto
def modificar_cantidad():
    inventario = []
    try: 
        existe = False
        nombre_producto = input("Introduce el nombre del producto para actualizar: ")
        inventario = puta_funcion_lectura()

        for i in inventario:
            if i["nombre_producto"] == nombre_producto:
                contador = int(input("Introduce cuántas unidades se añadirán: "))
                i["stock"]["cantidad"] += contador
                print(f"Se ha actualizado la cantidad de {contador} unidades del producto {nombre_producto}")
                existe = True
                break
            
        if existe == True:
            puta_funcion_escritura(inventario)
        
        else:
            print(f"El producto {nombre_producto} no se encuentra en el inventario")  

    except ValueError:
        print("Error: Entrada inválida")


# Eliminar un producto
def eliminar_producto():
    inventario = []
    try: 
        existe = False
        nombre_producto = input("Introduce el nombre del producto para eliminar: ")
        inventario = puta_funcion_lectura()

        for i in inventario:
            if i["nombre_producto"] == nombre_producto:
                inventario.remove(i)
                print(f"Se ha eliminado el producto: {nombre_producto}")
                existe = True  
                break
        
        if existe == True:
            puta_funcion_escritura(inventario)
        
        else:
            print(f"El producto {nombre_producto} no se encuentra en el inventario")  

    except ValueError:
        print("Error: Entrada inválida")

# Generar resumen del inventario
def resumen_inventario():
    inventario = puta_funcion_lectura()
    sumatorio_productos = 0
    sumatorio_money = 0.0
    
    for i in inventario:
        cantidad = i["stock"]["cantidad"]
        precio = i["stock"]["precio"]
        sumatorio_productos += cantidad
        sumatorio_money += precio * cantidad
        
    print(f"TOTAL DE PRODUCTOS EN EL INVENTARIO: {sumatorio_productos}\nVALOR TOTAL DEL INVENTARIO: {sumatorio_money}€")

# Cerrar programa
def cierre():
    print("Hasta otra")

# Putas funciones de mierda recurrente
def puta_funcion_lectura():
    inventario = []
    with open("bbdd.txt","r") as fichero:
        for linea in fichero.readlines():
            props = linea.split("/")
            p = {"nombre_producto" : props[0], "stock" : {"precio" : float(props[1]), "cantidad" : int(props[2].removesuffix("\n"))}}
            inventario.append(p)
    return inventario

def puta_funcion_escritura(inventario):
    with open("bbdd.txt","w") as fichero:
        for i in inventario:
            fichero.write(f"{i["nombre_producto"]}/{i["stock"]["precio"]}/{i["stock"]["cantidad"]}\n")
    
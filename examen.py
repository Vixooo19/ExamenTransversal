recorridos = {
'R001': ['santiago', 'valparaiso', 120, 'normal', 'día', True],
'R002': ['santiago', 'concepción', 500, 'cama', 'noche', True],
'R003': ['la serena', 'coquimbo', 15, 'normal', 'día', False],
'R004': ['temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
'R005': ['iquique', 'arica', 310, 'cama', 'noche', False],
'R006': ['santiago', 'Rancagua', 90, 'normal', 'día', True],

}

venta = {
    'R001': [7990, 201],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    'R006': [4990, 12]

}





#coleccion general RutaExpress
def menu():
    print('========== MENÚ PRINCIPAL ==========         ')
    print('1. ASIENTOS POR CIUDAD DE ORIGEN             ')
    print('2. BUSQUEDA DE RECORRIDOS POR RANGO DE PRECIO')
    print('3. actualizar precio de recorrido            ')
    print('4. agregar recorrido                         ')
    print('5. Elimiar recorrido                         ')
    print('6. Salir                                     ')

def leer_opcion():
    while True:
        try:
            opc = int(input('ingrese una opción'))
            if 1 <= opc <= 6:
                return opc
            else:
                print ('la opcion del menu debe ser un valor entero del 1 al 0')
        except ValueError:
            print ('la opcion del menu debe ser un valor entero del 1 al 0 ')

# funciones de validacion


#OPC 1 - Asientos por ciudad de origen
def Asientos_Origen(recorridos, venta):
    Ciudad = input('ingrese el nombre de la ciudad de origen')
    for i in range(recorridos(0)):
        if Ciudad == 'santiago':
            print(f'la cantidad de asientos son{'R001'(1)}{'R002'(1)}{'R006'(1)}')


#OPC 2 - Busqueda de recorridos por rango de precio
def agregar_recorrido(recorridos):   
     p_min = int(input('ingrese un precio minimo'))
     p_max = int(input('ingrese un precio maximo'))           




def busqueda_precio(p_min, p_max):
    if (p_min <= p_max):
        
        if (p_min >= 0 and p_max >= 0):
            print(recorridos in range (p_min and p_max ))
        else:
            ('los valores deben ser mayores o iguales a cero')
    else: ('el valor debe ser precio minimo debe ser menor al precio mayor ')

    




#OPC 4 - actualizar precio de recorrido
def agregar_recorrido(recorrido):
    codigo = input('ingrese el codigo')
    origen = input('ingrese el origen')
    destino = input('ingrese el destino')
    distancia = int(input('ingrese la distancia'))
    tipo_bus = input('ingrese el tipo de bus')
    servicio = input('ingrese el servicio')
    wifi = input('ingrese si tiene wifi ')
    precio = int(input('ingrese el precio'))
    asiento = int(input('ingrese cuantos asientos'))





#opc 5 - eliminar
def eliminar_recorrido(recorrido):
    ELrecorrido = input('ingrese el recorrido que desea eliminar')
    posicion = busqueda_precio(recorrido, 0)

    if posicion == -1
        print('El recorrido{0} no se encuentra registrado')
    else:
        recorrido.pop(posicion)
        print('el recorrido fue eliminado')
    

#ciclo principal
while True:
    menu()
    opc = leer_opcion()
    if opc == 1:
        Asientos_Origen
    elif opc == 2:
        busqueda_precio
    elif opc == 3:
        pass
    elif opc == 4:
        agregar_recorrido
    elif opc == 5:
        eliminar_recorrido
    elif opc == 6:
        print('programa finalizado')
        break



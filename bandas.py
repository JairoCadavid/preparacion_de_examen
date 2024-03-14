"""
realizar un software donde podamos:
-hacer el registro de bandas musicales
-validar el cartel festival
-buscar la banda (consulta)
-modificar una banda

Y en este software se va a poder guardar toda la info relacionada con las bandas, como por ejemplo:
-id
-nombre
-genero
-clasificacion
-costo
-tiempo
"""

#datos de entrada de las bandas
bandas=[]

#ciclo para mostrar un menu
opcion=100 #se le pone cual quier valor o "=None", esto con el fin de poder iniciar la funcion
while(opcion!=5):
    print("****FESTIVAL ALTAVOZ****\n**********************\n(1)Registrar banda\n(2)Ver el cartel del festival\n(3)Buscar una banda\n(4)Modificar una banda\n(5)Finalizar")
    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #se pide o se llena el objeto de banda
        banda["id"]=int(input("Digite el id: "))
        banda["nombre"]=input("nombre: ")
        banda["genero"]=input("genero: ")
        banda["clasificacion"]=input("clasificacion: ")
        banda["costo"]=int(input("costo: "))
        banda["tiempo"]=input("tiempo: ")
        
        #Cómo agrego un diccionario a una lista
        bandas.append(banda)

    elif opcion==2:
        #recorriendo una lista para imprimir sus elementos
        for bandaAuxiliar in bandas:
            print(f'{bandaAuxiliar["id"]}---{bandaAuxiliar["nombre"]}')

    elif opcion==3:
        #buscando un elemento dentro de una lista
        bandaBuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar("nombre")==bandaBuscada:
                print("Banda encontrada en la BD")
            else:
                print("banda no encontrada en la BD")

    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        print("Opción invalida!")




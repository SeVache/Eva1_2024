vlan=int(input("Ingresar ID de Vlan"))
if vlan >= 1 and vlan <= 1005:
    print("Vlan de rango Normal ")
elif  vlan >= 1006 and vlan <= 4095:
    print("Vlan de Rango Extendido")
else:
    print("número de Vlan ingresado es desconocida")    

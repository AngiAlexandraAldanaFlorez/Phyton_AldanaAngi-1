
#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO
print('''Bienvenido, Te ofrecemos los siguientes productos''')
diccionario = {'Zapatos-':200000,'Camisas-':75000,'Pantalones':100000}

for llave , valor in diccionario.items():
    print(llave,valor)


a=str(input('Ingrese producto que quiere comprar '))
b=int(input('Ingrese cantidad del producto '))

if (a=="Zapatos" or a=="zapatos"):
    print('Valor a pagar= ',200000*b)
elif (a=="Camisas" or a=="camisas"):
    print('Valor a pagar= ',75000*b)
elif (a=="Pantalones"or a=="pantalones"):
    print('Valor a pagar= ',100000*b)
else:
    print("No se encuentra el producto")






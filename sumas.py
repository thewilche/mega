num=(float(input('Ingrese un número impar: ')))

while num%1!=0:
    print('Número decimal. Intente nuevamente')
    num= float(input('Ingrese un número impar: '))
while int(num%2==0):
        print('Número par. Intente nuevamente')
        num= float(input('Ingrese un número impar: '))
        while num%1!=0:
            print('Número decimal. Intente nuevamente')
            num= float(input('Ingrese un número impar: '))
else:
    print ('El número impar es', int(num))
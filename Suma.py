def sumar(a,b):
    suma=(a+b)
    return(suma)
ing_ok=True
while ing_ok==True:
    try:
        num1=int(input("Ingrese el primer valor :"))    
        num2=int(input("Ingrese el segundo valor :"))  
        ing_ok=False
    except ValueError:
        print("Por favor solo datos Enteros")
        ing_ok=True
print("Este es el resultado de la suma: ",sumar(num1,num2))        

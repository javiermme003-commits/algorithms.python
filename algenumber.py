import math

def incr(n):
        e=(1+1/n)**n
        return e

def ecalc(m,n,o,x):
        while m<n:
                valor= (1+1/m)**m
                error=abs(math.e - valor)
                print(f"Para {m} tiene valor: {valor}. Error de {error}")
                if o == 0:
                    m=m*x
                elif o == 1:
                    m=m+x


def fact(n):
    resultado=1
    for i in range(1,n+1):
        resultado=resultado*i
    return resultado

def taylor(n):
    resultado=0
    for i in range(0, n):
        resultado=resultado+(1/fact(i))
    return resultado

def empeora_limite(n,m,o,x):
        anterior = None
        e=1
        while n < m:
                valor= (1+1/n)**n
                error=abs(math.e - valor)
                print(f"{e}.número {n}, valor {valor}, error {error}")
                if anterior != None and anterior <= error:
                    print(f"No hay mejora a partir de {n}")
                    break
                anterior = error
                e=e+1
                if o == 0:
                    n=n*x
                elif o == 1:
                    n=n+x


def empeora_taylor(n,m,o,x):
        anterior = None
        e=1
        while n < m:
                valor= taylor(n)
                error=abs(math.e - valor)
                print(f"{e}.número {n}, valor {valor}, error {error}")
                if anterior != None and anterior <= error:
                    print(f"No hay mejora a partir de  {n}")
                    break
                anterior = error
                e=e+1
                if o == 0:
                    n=n*x
                elif o == 1:
                    n=n+x


def comparalimcontay(n,m):
        errl= None
        errt= None
        anteriorlim = None
        l=n
        while l < m:
                valorlim=(1+1/l)**l 
                errorlim=abs(math.e - valorlim)
                if anteriorlim != None and anteriorlim <= errorlim:
                    print(f"Lim no mejora a partir de  {l}, teniendo {errorlim} de error.")
                    errl = errorlim

                    break
                anteriorlim = errorlim
                l=l+1
        anteriortay = None
        while n < m:
                valortay= taylor(n)
                errortay=abs(math.e - valortay)
                if anteriortay != None and anteriortay <= errortay:
                    print(f"Taylor no mejora a partir de  {n}, teniendo {errortay} de error")
                    errt = errortay
                    break
                anteriortay = errortay
                n=n+1
        if errl is None and errt is None:
                print("Ninguno de los métodos ha alcanzado su límite")
        elif errl is None:
                print("Límite no ha alcanzado su límite")
        elif errt is None:
                print("Taylor no ha alcanzado su límite")
        elif errl < errt:
                diferencia= errt-errl
                print(f"Límite es mejor con una diferencia de {diferencia}")         
        elif errorlim > errortay:
                diferencia= errl-errt
                print(f"Taylor es mejor con una diferencia de {diferencia}")
        else:
                print("Los dos son igual de buenos métodos")



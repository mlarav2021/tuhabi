
#----------------------------------------------------------------------------
# Created By  : Marco Antonio Lara Vargas
# Created Date: 2022-06-25
# version ='1.0'
# ---------------------------------------------------------------------------
"""Ejercicio 2 de la prueba para data engineer - Numero de goles conseguidos por dos equipos de futbol"""  
# ---------------------------------------------------------------------------

#Funcion que cuenta los elementos que sean <= a los goles del equipo B

def count_elementos(equipoa,equipob):
    res=[]
    for i in range(len(equipob)):
        contador=0
        for j in range(len(equipoa)):
            if equipoa[j] <= equipob[i]:
                contador += 1
        res.append(contador)
    return res


# Funcion para solicitar los partidos y goles de cada equipo

def ingresa_equipos(partidos):
    while  not(2 <= partidos and partidos <= 105):
        n = int(input('El numero de partidos del equipo debe ser mayor a 2  y menor a 105 para poder continuar:'))
    
    equipo=[]
    for i in range(partidos):
        goles = int(input('Goles del partido {}: '.format(i+1)))
        while  not(1 <= goles and goles <= 109):
            goles = int(input('El numero de goles debe tener un rango de 1 a 109: '))
        equipo.append(goles)
    return equipo

# Funcion principal 

def main ():
    equipoA= ingresa_equipos(int(input('Ingrese el numero de partidos del equipo A: ')))
    equipoB= ingresa_equipos(int(input('Ingrese el numero de partidos del equipo B: ')))
    res = count_elementos(equipoA,equipoB)
    print('Conteno de elementos')
    print(res)

if __name__ == "__main__":
    main()

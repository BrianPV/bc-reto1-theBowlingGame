import random, time
class Bowling():
    
    def welcome(self):
        print("Bienvenidos a The bowling game. Se iniciara el juego con el tablero limpio")
        print("Instrucciones: Debes ingresar numeros del 0 al 10 que son numero permitidos del juego")
        print("2.- El programa te guiara automaticamente, solo tienes que ingresar numeros")
        print("OJO: Ten cuidado y trata de NO ingresar entradas vacias o que no sean un numero, despues de eso todo esta controlado (se supone)")
        print("!Buen juego! \n")

    def validShot(self, tiro):
        self.tiro = tiro
        if self.tiro > 10:
            print("Tu tiro no puede derribar mas de 10 pinos, intenta de nuevo.")
            return False
        
        if self.tiro < 0:
            print("Tu tiro no puede ser negativo, intenta de nuevo.")
            return False

        if self.tiro == 0:
            return None

        if self.tiro >= 0 and self.tiro <= 10:
            return self.tiro

    def shot(self, sets):
        self.set = sets
        printTiros = 0
        turno = 0
        tiro1 = 0
        tiro2 = 0
        for turno in range(0,2):
            printTiros = turno
            print("Ingresa tu tiro " + str(printTiros + 1))
            numero = int(input())

            self.tiro = self.validShot(numero)

            if self.tiro == False:
                self.shot()
            elif self.tiro == None :
                print("Tu tiro fue de 0 derribados")
                self.tiro = 0
            else:
                print("Tu tiro fue de " + str(self.tiro) + " pines derribados")

            if turno == 0:
                if self.tiro == 10:
                    tiro1 = 10
                    tiro2 = 0
                    break
                else:
                    tiro1 = self.tiro 

            if turno == 1:
                sumaPines = tiro1 + self.tiro
                if sumaPines > 10:
                    while True:
                        print("Tu numero rebasa el numero de pines, ingresa otro numero")
                        print(sumaPines)
                        print("Ingresa otro numero")
                        self.tiro = int(input())
                        if (tiro1 + self.tiro):
                            break

                tiro2 = self.tiro
        
        return tiro1, tiro2


    def tablero(self, turno, tiro1, tiro2):
        self.turno = turno
        self.tiro1 = tiro1
        self.tiro2 = tiro2


        grid = [self.turno, self.tiro1, self.tiro2]

        print("En el turno " + str(grid[0]) + " obtuviste: ")
        print("Primer tiro = " + str(grid[1]))
        print("Segundo tiro = " + str(grid[2]))

        return grid

    def getStrike(self, tiro1, tiro2, tiro3):
        self.tiro1 = tiro1
        self.tiro2 = tiro2
        self.tiro3 = tiro3
        addStrike = self.tiro1 + self.tiro2 + self.tiro3

        return addStrike
    
    def getSpare(self, tiro1, tiro2):
        self.tiro1 = tiro1
        self.tiro2 = tiro2
        addSpare = self.tiro1 + self.tiro2

        return addSpare

    def analyzeResults(self, grid):
        finalGrid = []
        self.grid = grid
        for x in range(0, len(self.grid)):
            #print(x)
            if self.grid[x][1] == 10:
                if x == 9:
                    #print("Estoy en el ultimo index del array en strike")
                    strike = self.getStrike(10, self.grid[x+1][1], self.grid[x+1][2])
                    points = [x, strike, self.grid[x][1], self.grid[x][2]]
                    #print(points)
                    finalGrid.append(points)
                    break
                else:
                    if self.grid[x+1][1] == 10:
                        #print("Estoy sumando el strike del if de" + str(x))
                        strike = self.getStrike(10, self.grid[x+1][1], self.grid[x+2][1])
                        points = [x, strike, self.grid[x][1], self.grid[x][2]]
                        #print(points)
                        finalGrid.append(points)
                    else:
                        #print("Estoy sumando el strike normal de " + str(x))
                        strike = self.getStrike(10, self.grid[x+1][1], self.grid[x+1][2])
                        points = [x, strike, self.grid[x][1], self.grid[x][2]]
                        #print(points)
                        finalGrid.append(points)
            elif self.grid[x][1] + self.grid[x][2] == 10:
                if x == 9:
                    #print("Estoy en el ultimo index del array en square")
                    spare = self.getSpare(10, self.grid[x+1][1])
                    points = x, spare, self.grid[x][1], self.grid[x][2]
                    finalGrid.append(points)
                    break
                else:
                    spare = self.getSpare(10, self.grid[x+1][1])
                    points = x, spare, self.grid[x][1], self.grid[x][2]
                    finalGrid.append(points)
                    
            else:
                #print("Todo normal por aqui")
                suma = self.grid[x][1] + self.grid[x][2]
                points = x, suma, self.grid[x][1], self.grid[x][2]
                #print(points)
                finalGrid.append(points)
            
        return finalGrid    

        #print(self.grid[0])
        

generalGrid = []
extraTiro1  = 0
extraTiro2 = 0


jugar = Bowling()
jugar.welcome()

sets = 10
printSets = 0
for x in range(sets):
    printSets = x
    print("Este es el set numero " + str(printSets + 1))
    tirar = jugar.shot(x)
    score = jugar.tablero(x, tirar[0], tirar[1])
    print("\n")
    #print(score)
    generalGrid.append(score)
    #print(generalGrid[0])

#print(generalGrid[-1][1])
#print(generalGrid[-1][2])   

if generalGrid[-1][1] == 10:
    print("Conseguiste un strike en el ultimo tiro, tienes 2 tiros extras")
   
    for x in range(2):
        print("Tiro " + str(x+1))
        numero = int(input())    
        tiro = jugar.validShot(numero)
        if tiro == False:
            while True:
                print("Tiro invalido, por favor ingresa otro")
                numero = int(input())
                if numero.isdigit or numero == None:
                    break
        elif tiro == None:
            print("Tu tiro fue de 0 derribados")
            tiro = 0
        else:
            print("Tu tiro fue de " + str(tiro) + " pines derribados")
        
        if x == 0:
            extraTiro1 = tiro
        if x == 1:
            extraTiro2 = tiro
    
    largo = len(generalGrid)
    extraPoints = [largo, extraTiro1, extraTiro2]
    generalGrid.append(extraPoints)

elif (generalGrid[-1][1] + generalGrid[-1][2]) == 10:
    print("Conseguiste un square en el ultimo tiro, tienes 1 tiro extra")
    numero = int(input())    
    tiro = jugar.validShot(numero)
    if tiro == False:
        while True:
            print("Tiro invalido, por favor ingresa otro")
            numero = int(input())
            if numero.isdigit or numero == None:
                break
    elif tiro == None:
        print("Tu tiro fue de 0 derribados")
        tiro = 0
    else:
        print("Tu tiro fue de " + str(tiro) + " pines derribados")
    
    extraTiro1 = tiro
    largo = len(generalGrid)
    extraPoints = [largo, extraTiro1, 0]
    generalGrid.append(extraPoints)


#print("\n")
#print(generalGrid)
#print("\n")
finalScore = jugar.analyzeResults(generalGrid)
#print(finalScore)

print("Este es tu resultado final")
print("\n")
sumaTotal = 0
setsFinal = 0
for x in range(len(finalScore)):
    sumaTotal += finalScore[x][1]
    setsFinal = finalScore[x][0]
    print("Set numero: " + str(setsFinal + 1))
    print("Total de este set: " + str(finalScore[x][1]))
    print("Total de esta ronda: " +str(sumaTotal))
    print("Tu tiro 1 fue de: " + str(finalScore[x][2]))
    print("Tu tiro 2 fue de: " + str(finalScore[x][3]))
    print("\n")

print("Obtuviste una sumatoria total de: " + str(sumaTotal))
#print(suma)
#for x in range(0,len(generalGrid)):
#    print(generalGrid[x])
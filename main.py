#1.2.1

tempDeg = "24°"
ventVit = "12km/h"
humiTaux = "45%"

meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s' % (tempDeg, ventVit, humiTaux)
print(meteo)


#1.2.2

beau= "beau"
faible = "faible"
correcte = "correcte"

meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s' % (beau, faible, correcte)
print(meteo)


#1.2.3

chaineA = "cette chaine"
chaineB = " contient %s caractères"
chaineC = " par contre"
chaineD = "celle-ci"

value = len(chaineA+chaineB+chaineC+chaineD)

chaineCaractere = chaineA + chaineB % ( len(chaineA+chaineB) )
print(chaineCaractere)

chaineCaractere = chaineD + chaineB % ( len(chaineD + chaineB + chaineC) ) + chaineC 
print(chaineCaractere)


#1.2.4

chaineBnew = chaineB.replace("%s", "{}")

chaineE = chaineA + chaineBnew.format(len(chaineA + chaineBnew))
print("chaineE : " + chaineE)

chaineF = chaineD + chaineBnew.format(len(chaineD + chaineBnew + chaineC)) + chaineC
print("chaineF : " + chaineF)
import math

leiviskä=float(input("Syötä leiviskät: "))
naula=float(input("Syötä naulat: "))
luoti=float(input("Syötä vielä luodit: "))


luodit = luoti*13.3
naulat = naula + 32*luodit
leiviskät = leiviskä + naulat * 20

kokonaispaino = luodit + naulat + leiviskät
kilot = kokonaispaino/1000

def KilogrammoiksijaGrammoiksi(paino):
    kilot = kokonaispaino / 1000
    return int(kilot), kokonaispaino % 1000

print('The amount of pounds you entered is {}. '\
      'Tämä on {} kilogrammaa ja {} grammaa.'.format kilot, kokonaispaino))

print("Syöttämiesi arvojen kokonaispaino nykymittoina on " ,kilot, "kilogrammaa ja " ,kokonaispaino, "grammaa.")




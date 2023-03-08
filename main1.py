import math 

#függvények
def Haromszogkerulete(aa, bb, cc):
    return aa + bb + cc

def Haromszogterulete(aa, bb, cc):
    s = Haromszogkerulete(aa, bb, cc) / 2
    TT = math.sqrt( s(s-aa)*(s-bb)*(s-cc) )
    return TT

#0
print("Háromszög feldolgozása függvények segítségével.")

#1
temp=input("Kérem az oldalakat ';'-el elválasztva: ")
reszletek = temp.split(';')
a = float(reszletek[0].replace(',' , ';'))
b = float(reszletek[1].replace(',' , ';'))
c = float(reszletek[2].replace(',' , ';'))

#2
K = Haromszogkerulete(a, b, c)
T = Haromszogterulete(a, b, c)

#3
print(f"A(z) {a:.2f}cm és {b:.2f}cm és {c:.2f}cm oldal hosszúságú a háromszög kerülete: {K:.2}cm")
print(f"A(z) {a:.2f}cm és {b:.2f}cm és {c:.2f}cm oldal hosszúságú a háromszög területe: {T:.2}cm")
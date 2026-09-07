import random



total = 0

while True:

    summa = 0

    antal = input("Ange antal kast: ")

    if antal == "q":
          break

    num = int(antal)
    
    for n in range(1, num + 1):

            roll = random.randint(1,6)
            print(roll)
            summa += roll   
            total += roll

    print(f"Summan av alla kast var {summa}" "\n")

        
print(f"Totala summan av alla kast var {total}")

if total % 2 == 0:
    print("Totala summan är ett jämnt tal")
else:
    print("Totala summan är ett udda tal")

print("Programmet avslutas...")
exit()
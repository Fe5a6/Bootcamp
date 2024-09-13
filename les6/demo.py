getallen_lijst = []

for i in range(6):
    getal = int(input(f"Voer getal {i+1} in: "))
   
    getallen_lijst.append(getal)

getallen_lijst.sort()

print("De gesorteerde lijst is:", getallen_lijst)
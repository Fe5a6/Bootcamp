fruit_lijst = ['appel', 'banaan', 'kers', 'druif', 'mango', 'peer']


print("Huidige fruitlijst:", fruit_lijst)


index = int(input("Voer een index in (0 t/m 5): "))

if 0 <= index < len(fruit_lijst):
   
    gepakt_fruit = fruit_lijst.pop(index)

    
    print(f"Je hebt '{gepakt_fruit}' gepakt.")

    print("Bijgewerkte fruitlijst:", fruit_lijst)
else:
    print("Ongeldige index, probeer een waarde tussen 0 en 5.")
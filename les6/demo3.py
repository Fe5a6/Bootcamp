kleuren_lijst = ['rood', 'blauw', 'groen', 'geel', 'paars', 'oranje']

naam = input("Wat is je naam? ")

favoriete_kleur = input("Wat is je favoriete kleur? ").lower()  


if favoriete_kleur in kleuren_lijst:
    
    print(f"Hey {naam}, wat een prachtige kleur is {favoriete_kleur}!")
    print(f"De kleur {favoriete_kleur} is net zo levendig en vrolijk als jij!")
else:
   
    print(f"Psst {naam}, deze kleur is niet zo geweldig! als {', '.join(kleuren_lijst)}?")
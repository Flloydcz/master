utocnik = float(input("Útočník si hodí Weapon skill + Agility. Počet hitů? "))
obrance = float(input("Obránce si hodí Reaction + Intuition. Počet hitů? "))
attackrating = float(input("Attack rating útočníkovy zbraně? "))
deffrating = float(input("Defense rating obránce? "))
if (attackrating - deffrating) > 4:
    print("Útočník získá edge")
elif (deffrating - attackrating) > 4:
    print("Obránce získá edge")
else:
    pass 
if utocnik > obrance:
    print("Útočník zasáhnul")
else:
    print("Útočník minul")

# Combat steps:
# Distribute edge
# Attack - roll dice and spend edge
# Soak damage
# Bring the Pain
# Edge - pokud má utočník nebo obránce o 4 vyšší rating než protivník, získává edge
attackrating = float(input("Attack rating útočníka? Zbraň + prostředí + visual"))
deffrating = float(input("Defense rating obránce? Brnění + prostředí + vybavení"))
if (attackrating - deffrating) > 4:
    print("Útočník získá edge")
elif (deffrating - attackrating) > 4:
    print("Obránce získá edge")
else:
    print("Nikdo nezíská edge") 
# Porovná se počet hitů útočníka a obránce. Pokud má útočník více tak zasáhl.
utocnik = float(input("Útočník si hodí Weapon skill + Agility. Počet hitů? "))
obrance = float(input("Obránce si hodí Reaction + Intuition. Počet hitů? "))
if utocnik > obrance:
    print("Útočník zasáhnul")
    print("Počet net hitů je: ", (utocnik - obrance))
else:
    print("Útočník minul")

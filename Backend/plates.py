# this tuple contains all the plates that will be needed to form the earthquake warning system.
plates = (
    "African",
    "Antarctic",
    "Arabian",
    "Australian",
    "Caribbean",
    "Cocos",
    "Eurasian",
    "Indian",
    "Juan de Fuca",
    "Nazca",
    "North American",
    "Pacific",
    "Philippine Sea",
    "Scotia",
    "South American"
)
plate = input("Enter a plate: ")
if plate in plates:
    print("True")
import os
import csv

def lecture_fichier(chemin: str):
    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None



with open("../Projet/Projet1 SAE15 - Copy.txt") as f:
    line = csv.reader(f, delimiter='\t')

    print(list(line))



#file = open('../Projet/Projet1 SAE15 - Copy.txt', "r")
#lines = file.readlines()
#file.close()
#for line in lines:
#    print(line.strip())
            
            
#f = lecture_fichier('../Projet/Projet1 SAE15 - Copy.txt')


#with open('Données.csv', "w", newline='') as csvfile:
#    fieldnames= ['IP destination', 'IP source', 'Flags', 'Length']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()


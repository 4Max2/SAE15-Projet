import os
import csv

def lecture_fichier(chemin: str):
    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None

tab=[]
tab1=([],[],[],[])
f = lecture_fichier('../Projet/Projet1 SAE15 - Copy.txt')
a = f.splitlines()


with open('Données.csv', "w", newline='') as csvfile:
    fieldnames= ['IP destination', 'IP source', 'Flags', 'Length']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in a :
        if i.startswith('\t')==False:
            tab=i.split(' ')
            tab1[0].append(tab[2])
            print(tab1[0]) 
            tab1[1].append(tab[4])
            for j in tab:
                if tab[5] == 'Flags':
                    tab1[2].append(tab[5+1])
                    a = len(tab)
                #print(a)
            for k in tab:
                if a >= 8 :
                    if tab[-2] == 'length':
                            #print(tab[-1])
                       tab1[3].append(tab[-1])
                    elif tab[-3] == 'length':
                            #print(tab[-2])
                        tab1[3].append(tab[-2])
            chaine=str('')
            for l in range(4):
                chaine=chaine+str(tab1[l])+';'
   
            print(chaine)    
#print(tab1[3])
#print(tab1[0],tab1[1],tab1[2],tab1[3])

#with open('Données.csv', "w", newline='') as csvfile:
 #   fieldnames= ['IP destination', 'IP source', 'Flags', 'Length']
 #   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 #   writer.writeheader()
 #   for i in tab1[0] :
        writer.writerow({'IP destination': tab1[0]})
#    for j in tab1[1] :
        writer.writerow({'IP source': tab1[1]})
#    for k in tab1[2] :
        writer.writerow({'Flags': tab1[2]})
    #for l in tab1[3] :
        writer.writerow({'Length': tab1[3]})
 
    



#print(list(tab.strip()))
#print(a)       
#print(tab[3])
#for n in tab :
#    if tab[n] == \ré\ré\ré.\ré\ré\ré.\ré\ré\ré.\ré\ré\ré :
#        tab1.append(n)
        #print(n)
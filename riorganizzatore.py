import random as rd 
import json 

def loadJSON(): #Legge il file JSON e restituisce il contenuto in un dizionario
    with open('C:/Users/andre/Desktop/projects/Python/RiorganizzatoreBanchi/classi.json', 'r+') as file:
        data = json.load(file)
    return data

def readPlacement(classe): #Legge il file JSON e restituisce le disposizioni in un dizionario 
    with open('C:/Users/andre/Desktop/projects/Python/RiorganizzatoreBanchi/disposizioni.json', 'r+') as file: 
        data = json.load(file)
    return data

def seven(cognomi):
    SubArray = [[] for _ in range(7)]
    for i in range(len(SubArray)):
        for j in range(3):
            cognome = rd.choice(cognomi)
            SubArray[i].append(cognome)
            cognomi.remove(cognome)
    return SubArray

def randomize(cognomi, classe):
    disposizione = readPlacement(classe)[classe]
    rd.shuffle(cognomi)
    match disposizione: 
        case 7:
            return seven(cognomi)
        case _:
            return "c'é stato un errore!"

def SelezioneClasse(): #Selezione della classe da Input
    while True:
        classe = input("Scegli la Classe: ").lower()
        classiDisponibili = loadJSON()
        if classe in classiDisponibili:
            cognomi = classiDisponibili[classe]
            nuovaDisposizione = randomize(cognomi, classe)
            print(nuovaDisposizione)
            break
        else: 
            print('Errore')

SelezioneClasse()

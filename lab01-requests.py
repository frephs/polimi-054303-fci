import requests
import matplotlib.pyplot as plt

# ESERCIZIO 1.2
# DATI: una lista di 6 siti e un numero num_iter di GET requests da effettuare
# OUTPUT: il nome del sito con il miglior tempo di risposta medio
# ISTRUZIONI: sono richieste nella soluzione le seguenti:
#   1) definire una funzione media(l: list) che data una lista ritorni la media algebrica
#      dei valori dall'interno della lista
# HINT: data una lista l, l.index(a) ritorna l'indice dell'elemento a
#       Esempio: l = [1, 5, 6, 1]
#                print(l[1]) # stampa 5
#                print(l.index(5)) # stampa 1

def media(l: list):
    return sum(l)/len(l)

if __name__ == '__main__':
    siti = [
        'http://www.google.com',
        'http://www.youtube.com',
        'http://www.polimi.it',
        'http://www.wikipedia.org',
        'http://www.amazon.com',
        'http://www.twitter.com'
    ]
    num_iter = 5

    ritardi_medi = []
    for url in siti:
        ritardi = [requests.get(url).elapsed.microseconds / 1000 for _ in range(num_iter)]
        ritardi_medi.append(media(ritardi))
        # Stampo le coppie sito - ritardo medio per verificare che l'output finale sia corretto
        print(f'Sito: {url}, ritardo medio: {media(ritardi)}')
    miglior_ritardo_medio = min(ritardi_medi)
    miglior_sito = siti[ritardi_medi.index(miglior_ritardo_medio)]
    print(f'Il sito con il miglior ritardo medio è {miglior_sito}')
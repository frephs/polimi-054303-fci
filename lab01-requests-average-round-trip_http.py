import requests

if __name__ == '__main__':
    # ESERCIZIO: dati 3 siti, stampare il nome del sito 
    # con il ritardo medio migliore e il valore del ritardo medio migliore
    siti = ['http://www.polimi.it', 'http://www.google.com', 'http://www.netflix.com']
    num_iter = 10

    migliore_tempo_medio = 10000
    indice_migliore_tempo_medio = 0
    for i, url in enumerate(siti):
        tempi = [requests.get(url).elapsed.microseconds/1000 for _ in range(num_iter)]
        tempo_medio = sum(tempi)/len(tempi)
        print(f"Ritardo medio per {url}: {tempo_medio} ms")
        if tempo_medio < migliore_tempo_medio:
            migliore_tempo_medio = tempo_medio
            indice_migliore_tempo_medio = i
    print(f'{siti[indice_migliore_tempo_medio]} ha il miglior ritardo medio di {migliore_tempo_medio} ms')
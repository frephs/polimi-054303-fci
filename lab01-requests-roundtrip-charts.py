import requests
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # ESERCIZIO: dati due siti web:
    #   1) Creare, per ogni sito, una lista con 10 diverse misure del ritardo
    #   2) Stampare, per ogni sito, ritardo minimo, massimo e medio
    #   3) Graficare i ritardi:
    #       - Con un line graph. Asse x: iterazione, asse y: ritardo
    #       - Con un istogramma. Asse x: ritardo, asse y: frequenza
    #       - Con un boxplot. Asse x: sito, asse y: ritardo

    url_google = 'http://www.google.com'
    url_netflix = 'http://www.netflix.com'
    num_iter = 100

    tempi_google = []
    # Ripeto la misura num_iter volte
    for _ in range(num_iter):
        r = requests.get(url_google)
        tempi_google.append(r.elapsed.microseconds/1000)
    # Calcolo massimo, minimo e media
    max_google = max(tempi_google)
    min_google = min(tempi_google)
    mean_google = sum(tempi_google)/len(tempi_google)
    # Stampo massimo, minimo e media
    print(f'Ritardo massimo di {url_google}: {max_google} ms')
    print(f'Ritardo massimo di {url_google}: {min_google} ms')
    print(f'Ritardo massimo di {url_google}: {mean_google} ms')

    tempi_netflix = []
    for _ in range(num_iter):
        r = requests.get(url_netflix)
        tempi_netflix.append(r.elapsed.microseconds/1000)
    max_netflix = max(tempi_netflix)
    min_netflix = min(tempi_netflix)
    mean_netflix = sum(tempi_netflix)/len(tempi_netflix)
    print(f'Ritardo massimo di {url_netflix}: {max_netflix} ms')
    print(f'Ritardo massimo di {url_netflix}: {min_netflix} ms')
    print(f'Ritardo massimo di {url_netflix}: {mean_netflix} ms')

    # Line graph
    plt.figure()
    plt.plot(tempi_google, label=url_google)
    plt.plot(tempi_netflix, label=url_netflix)
    plt.xlabel('Iterazione')
    plt.ylabel('Ritardo (ms)')
    plt.title('Ritardo a livello applicativo')
    plt.legend()
    plt.show()

    # Istogramma
    plt.figure()
    plt.hist(tempi_google, label=url_google)
    plt.hist(tempi_netflix, label=url_netflix)
    plt.xlabel('Ritardo (ms)')
    plt.ylabel('Occorrenze')
    plt.title('Ritardo a livello applicativo')
    plt.legend()
    plt.show()

    # Boxplot
    # COME LEGGERE UN BOXPLOT:
    # La riga in mezzo rappresenta la mediana
    #   Il 50% dei dati nella lista è minormediana, il restante 50% è sopra
    # Le estremità del box rappresentano il primo quartile (q1) e il terzo quartile (q3)
    # Che cosa sono i quartili?
    #   - il 25% dei dati è inferiore al primo quartile (q1)
    #   - il 75% dei dati è inferiore al terzo quartile (q3)
    #   - N.B.: il secondo quartile (q2) è la mediana!
    # Il "baffo" superiore è calcolato come q3 + 1.5 * Inter-Quartile-Range (IQR)
    # Il "baffo" inferiore è calcolat come q1 - 1.5 * Inter-Quartile-Range (IQR)
    # IQR = q3 - q1 (l'altezza del box)
    # I punti che sono fuori i "baffi" vengono considerati "outliers" e rappresentati come cerchi
    plt.figure()
    plt.boxplot([tempi_google, tempi_netflix])
    # Al posto di "1" e "2", metto sull'asse x i nomi dei siti
    plt.xticks([1, 2], [url_google, url_netflix])
    plt.ylabel('Ritardo (ms)')
    plt.title('Ritardo a livello applicativo')
    plt.show()
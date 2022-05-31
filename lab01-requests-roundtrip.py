import requests

if __name__ == '__main__':
    # ESERCIZIO: mandare una HTTP GET Request a Google, stampare lo status code
    #            e il ritardo della HTTP GET Response
    url = 'http://www.google.com'
    # 1) Mando una GET request
    # 2) Metto la GET response in una variabile "r"
    r = requests.get(url)
    # Stampo l'HTTP Status Code
    print(r)
    # Altro modo per stampare l'HTTP status code
    print(f'HTTP Status Code: {r.status_code}')
    # Stampo il ritardo in millisecondi
    print(f'Ritardo: {r.elapsed.microseconds/1000} ms')

    # Stampo il contenuto della GET Response
    # print(r.text)

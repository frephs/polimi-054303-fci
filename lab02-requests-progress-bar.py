import requests
import numpy
from alive_progress import alive_bar

def best(urls, reps): 
    tempi = []
    for i, url in enumerate(urls):
        tempi_url = []
        with alive_bar(reps) as bar:
            for j in range(reps):
                r = requests.get(url)
                bar()
                tempi_url.append(r.elapsed.microseconds / 1000)
        tempi.append(tempi_url)
    
    best_time_index = 0
    best_time = numpy.mean(tempi[best_time_index])


    for i, url in enumerate(urls[1:]):
        time = numpy.mean(tempi[i])
        if time < best_time:
            best_time = time
            best_time_index = i;

    print(f"{best_time}ms by {urls[best_time_index][11:-5].capitalize()}")

if __name__ == '__main__':
    urls = ["http://www.google.com/", "http://youtube.com"]
    reps = 5

    best(urls, reps)
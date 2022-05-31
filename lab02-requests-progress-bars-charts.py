import requests
import matplotlib
import matplotlib.pyplot as plt
from alive_progress import alive_bar

def linegraph(tempi, url):
    plt.subplot(2,2,1)
    title = "" 
    for i in range(len(tempi)):
        plt.plot(tempi[i])
        title += url[i][11:].capitalize() + ", "
    plt.xlabel("ID richiesta")
    plt.ylabel("[ms]")
    plt.title(title)
    plt.grid()
    # plt.ylim([0, max(tempi)])

def histogram(tempi, urls):
    plt.subplot(2,2,2)
    title = "" 
    # list comprehension
    urls = [url[11:].capitalize() for i,url in enumerate(urls)]
    for i in range(len(tempi)):
        plt.hist(tempi[i])
        title += urls[i]
    plt.legend(urls)
    plt.ylabel("N volte")
    plt.xlabel("[ms]")
    plt.title(title)
    plt.grid()
    # plt.ylim([0, max(tempi)])

def boxplot(tempi, url):
    plt.subplot(2,2,3)
    title = "" 
    plt.boxplot(tempi)
    plt.xlabel("ID richiesta")
    plt.ylabel("[ms]")
    plt.title(title)
    plt.grid()
    # plt.ylim([0, max(tempi)])

def main():
    times = 20
    ritardi = []
    urls = ["http://www.google.com", "http://www.netflix.com","http://www.wikipedia.org", "http://www.github.com", "http://www.amazon.it", "http://www.polimi.it"]; # protocollo http
    # misuriamo il ritardo a livello applicativo
    # Elapsed: amount of time passed between sending the first byte of 
    #          the request and receiving the last byte of the response
    for url in urls: 
        ritardo_url = []
        with alive_bar(times) as bar:
            for _ in range(times):
                    r = requests.get(url);
                    ritardo_url.append(r.elapsed.microseconds / 1000 )
                    bar()
        ritardi.append(ritardo_url)
                
    # print(f"Avg: {sum(ritardi)/len(ritardi)}")
    # print(f"Min: {min(ritardi)}")
    # print(f"Max: {max(ritardi)}")
    
    plt.figure()
    linegraph(ritardi, urls)
    histogram(ritardi, urls)
    boxplot(ritardi, urls)
    plt.show()

if __name__ == "__main__":
    main()
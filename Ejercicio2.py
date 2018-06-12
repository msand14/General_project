#Dado un archivo que contiene en cada línea una palabra
# o conjunto de palabras seguido de un valor numérico
# denominado “sentimiento” y un conjunto de tweets, se
# pide calcular el sentimiento de aquellas palabras o
# conjunto de palabras que no tienen un valor asociado
# en el archivo de “sentimientos”. Se pueden seguir distintas
# estrategias para asignar un valor. Por ejemplo, se podría
# asignar como valor el valor del “sentimiento” del tweet
# en que se encuentra la palabra o conjunto de palabras
# sin valor, o el valor medio del “sentimiento” del tweet.

import json


# CONVIERTO LOS SENTIMIENTOS DEL ARCHIVO, EN UN DICCIONARIO
def feelings2dict():
    rows = []
    with open("/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/Sentimientos.txt") as file:
        for line in file:
            line= line.replace('\n','')
            if(line==''):
                continue
            rows.append(line.split('\t'))
        #print(rows)
        dic=dict(rows)
        #print(dic)
    return dic


# CONVIERTO LOS TWEETS EN UNA LISTA
def tweets2list():
    lista_tweets=[]
    with open( "/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/SalidaTweets.txt") as f:
        for i,elemento in enumerate(f):
            lista = json.loads(elemento)
            if lista.get('text'):
                lista_tweets.append(lista.get('text'))
    return lista_tweets


def feeling_of_tweet (lista_tweet, dic_feel):
    lista_palabras=[]
    for i,tweet in enumerate(lista_tweet):
        print("TWEET :" ,i,"")
        valor = 0
        for sentimiento in dic_feel:
            if sentimiento in tweet:
                valor = valor + int(dic_feel[sentimiento])
        print(len(tweet.split()))
        lista_palabras =tweet.split()
        for i in lista_palabras:
            print(i,":",(valor/len(tweet.split())))
        print(tweet)


def main():
    lista_tweets = tweets2list()
    diccionario_sentimientos = feelings2dict()
    feeling_of_tweet(lista_tweets,diccionario_sentimientos)



main()


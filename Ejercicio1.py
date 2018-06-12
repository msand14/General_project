# Dado un archivo que contiene en cada línea una palabra o
# conjunto de palabras seguido de un valor numérico, denominado
# “sentimiento”, y un conjunto de tweets, se pide calcular para
# cada tweet un valor denominado “sentimiento del tweet”, que se
# obtiene como la suma de los “sentimientos” de los términos que aparecen en el tweet.

import csv
import json

# CONVIERTO LOS TWEETS EN UNA LISTA
def tweets2list():
    lista_tweets=[]
    with open( "/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/SalidaTweets.txt") as f:
        for i,elemento in enumerate(f):
            lista = json.loads(elemento)
            if lista.get('text'):
                lista_tweets.append(lista.get('text'))
    return lista_tweets



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



def printer( str, val):
    print("EL SIGUIENTE TWEET:",str ," TIENE UN SENTIMIENTO ASOCIADO DE:",val,"\n")


def feeling_of_tweet (lista_tweet, dic_feel):
    for tweet in lista_tweet:
        valor = 0
        for sentimiento in dic_feel:
            if sentimiento in tweet:
                #print("\n","//////",sentimiento,"",int(dic_feel[sentimiento]),"\n")
                valor = valor + int(dic_feel[sentimiento])
        printer(tweet,valor)

def main():
    lista_tweets = tweets2list()
    diccionario_sentimientos = feelings2dict()
    feeling_of_tweet(lista_tweets,diccionario_sentimientos)


main()


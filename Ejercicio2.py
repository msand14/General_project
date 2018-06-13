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
    word_felt = False
    for i,tweet in enumerate(lista_tweet):
        print("TWEET :" ,i,":",tweet,"")
        valor = 0
        for sentimiento in dic_feel:
            if sentimiento in tweet:
                valor = valor + int(dic_feel[sentimiento])
        print(len(tweet.split()))
        lista_palabras =tweet.split()
        for palabra in lista_palabras:
            for sentimiento in dic_feel:
                if  sentimiento in palabra:
                    word_felt = True
                    break
                else:
                    word_felt = False
            if word_felt == False:
                print(palabra,":",(valor/len(tweet.split())))
            elif word_felt == True:
                print(palabra,":","No se muestra, ya tiene su valor asociado")
        print(" \n")


def main():
    lista_tweets = tweets2list()
    diccionario_sentimientos = feelings2dict()
    feeling_of_tweet(lista_tweets,diccionario_sentimientos)



main()


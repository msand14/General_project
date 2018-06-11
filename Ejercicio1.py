# Dado un archivo que contiene en cada línea una palabra o
# conjunto de palabras seguido de un valor numérico, denominado
# “sentimiento”, y un conjunto de tweets, se pide calcular para
# cada tweet un valor denominado “sentimiento del tweet”, que se
# obtiene como la suma de los “sentimientos” de los términos que aparecen en el tweet.

import csv
import json

#def tweet_analysis( ):
file = open("/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/SalidaTweets.txt")
file_reader=csv.reader(file)
datos=[]

# Reading each element of the file and appending it to  datos list
for i,linea in enumerate(file_reader):
    palabra = linea
    datos.append(json.dumps(linea))






import csv

def write_map(mapa):

    file=open("/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/AcumAnnos.csv",'w')
    writer=csv.writer(file)

    for key in mapa:
        writer.writerow([key,mapa.get(key)])
    file.close()
    print('Archivo'+' AcumAnnos.csv'+ ' Creado con éxito')


def sort_map():

    file = open("/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/PitchingPost.csv")
    reader=csv.reader(file)
    lista=[]
    for line in reader:
        lista.append(line)
    lista.sort()
    file.close()

    file_write=open("/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/Ordenados.csv",'w')
    writer = csv.writer(file_write)

    for linea in lista:
        writer.writerow(linea)

    file_write.close()


def frequency( columna,file_name):

    file=open(file_name)
    reader=csv.reader(file)
    data=list(reader)
    map={}
    for i in range(1,len(data)):
        key=str(data[i][columna])
        if(key in map):
            map[key]=map[key]+1
        else:
            map[key] = 1
    file.close()
    write_map(map)


frequency(1,"/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/PitchingPost.csv")
frequency(0,"/home/mescalonilla/bin/pycharm-community-2018.1.3/Documentos/PitchingPost.csv")
sort_map()
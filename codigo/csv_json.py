"""
Conversor de CSV <-> json

python csv_json ciudades.csv
/documentos/ciudades.csv -> /documentos/ciudades.json
"""
import json

def nombreFich(path, ext):
    t = path.rpartition('.')
    return t[0]+"."+ext 

def csvToDict(txt,sepRow='\n', sepCol=';'):
    lista = []
    L = txt.split(sepRow)
    cabs = L[0].split(sepCol)
    for i in L[1:]:
        linea = i.split(sepCol)
        d = dict(zip(cabs, linea))
        lista.append(d)
    return lista

def dictToCSV(lista, sepRow='\n', sepCol=';'):
    cabs = sepCol.join(lista[0].keys())
    L = [cabs]
    for d in lista:
        linea = sepCol.join(d.values())
        L.append(linea)
    return sepRow.join(L)

def csvToJson(ficheroCSV, ficheroJSON=None):
    f = None
    try:
        if ficheroJSON == None:
            ficheroJSON = nombreFich(ficheroCSV, 'json')
        print(f'Generando fichero:{ficheroJSON}')

        # Leer fichero origen: CSV
        f = open(ficheroCSV, "r")
        txt = f.read()
        d = csvToDict(txt)
        print(d)

    except Exception as e:
        print(e)
    finally:
        if f: f.close()

def jsonToCSV(ficheroJson, ficheroCSV=None):
    fcsv = None
    f = None
    try:
        if not ficheroCSV:
            ficheroCSV = nombreFich(ficheroJson, 'csv')
        print(f'Generando fichero:{ficheroCSV}')
        
        f = open(ficheroJson,"r")
        d = json.load(f)
        txt = dictToCSV(d)
        fcsv = open(ficheroCSV, "w")
        fcsv.write(txt)

    except Exception as e:
        print(e)

    finally:
        if f: f.close()
        if fcsv: fcsv.close()



if __name__=='__main__':
    csvToJson('ciudades.csv')
    jsonToCSV('/home/user/nombres.json')


from os import listdir
from os.path import isfile, isdir
import json

def carga(arbol, path):
    if isdir(path):
        arbol[path] = []

        for f in listdir(path):
            if isdir(path+"/"+f):
                carga(arbol, path + "/" + f)
            else:
                arbol[path].append(f)


if __name__ == "__main__":
    arbol = dict()
    carga(arbol, "xml_json")    
    print(json.dumps(arbol, indent=4))

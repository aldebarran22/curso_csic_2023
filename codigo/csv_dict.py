"""
Cargar un CSV en un dict
"""

txt = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

def csvToDict(sepRow='\n', sepCol=';'):
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

if __name__=='__main__':
    lista = csvToDict()
    txt2 = dictToCSV(lista)
    print(txt == txt2)

    d = {"k1": {"nombre":"Pepe","tno":777788}}
    print(d.keys())
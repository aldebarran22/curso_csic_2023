"""
Leer y escribir un fichero en Python
"""
def leerLineas(path):
    f=None
    try:       
        f = open(path, 'r')
        for linea in f:
            linea=linea.rstrip()
            print(linea)       
    except Exception as e:
        print(e)
    finally:
        if f: f.close()


def leer(path):
    f=None
    try:       
        f = open(path, 'r')
        txt = f.read()     
        print(txt)       
    except Exception as e:
        print(e)
    finally:
        if f: f.close()

if __name__=='__main__':
    #leer(r'C:\Users\profesor02\Desktop\curso_csic_2023-main\practicas\pandas\merge\Pedidos.txt')
    leerLineas(r'C:\Users\profesor02\Desktop\curso_csic_2023-main\practicas\pandas\merge\Pedidos.txt')
# listar los archivos de un directorio:

from os import walk

def ls(ruta = "."):
	dir, subdirs, archivos = next(walk(ruta))
	print("Actual: ", dir)
	print("Subdirectorios: ", subdirs)
	print("Archivos: ", archivos)
	
	
	
if __name__ == '__main__':
	ls()

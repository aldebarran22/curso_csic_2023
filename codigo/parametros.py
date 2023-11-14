"""
Tipos de parametros y 
formas de llamar a una funcion:
1) posicional
2) nominal
3) tupla / lista
4) dict
"""
def sumar(a,b):
    return a+b

print(sumar(1,3)) # posicional
print(sumar(b=3, a=1)) # nominal
t = (1,3)
print(sumar(*t))
L = [1,3]
print(sumar(*L))
d = {"a":1, "b":3}
print(sumar(**d))

def parametros(ob1, ob2, op1=1, op2=2, *args, **kwargs):
    print('obligatorios:', ob1,ob2)
    print('opcionales: ', op1,op2)
    print('args:',args, end=' ')
    print('kwargs:',kwargs)
    print()

parametros(1,2)
parametros(1,2, op2=100)
parametros(1,2,3,4,5,6,7)
parametros(1,2,3,4,5,6,7, x=1, y=2)




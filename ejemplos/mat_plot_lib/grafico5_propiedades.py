import matplotlib.pyplot as plt 

def main():
    X = list(range(10))
    Y1 = [x**0.5 for x in X]
    Y2 = [x for x in X]
    Y3 = [x**1.5 for x in X]
    Y4 = [x**2 for x in X]

    plt.suptitle("Ejemplo de funciones simultáneas", fontsize=24)
    plt.subplot2grid((2,2),(0,0), colspan=2)
    plt.title("4 funciones", fontsize=10)
    plt.plot(X, Y1)
    plt.plot(X, Y2)
    plt.plot(X, Y3)
    plt.plot(X, Y4)
    plt.grid(True, ls='-', color='0.5')
    plt.text(4.2,30,"y= x ** 2")

    plt.subplot2grid((2,2),(1,0), colspan=2)
    plt.title("Dos funciones", fontsize=10)
    plt.plot(X, Y1, label='Curva 1')
    plt.plot(X, Y2, label='Curva 2')
    plt.grid()
    plt.legend()
    plt.annotate("y = x", xytext=(1.5, 7), xy=(5.5, 5.6), ha='right',va='bottom',arrowprops={'color':'blue','shrink':0.02})
    plt.annotate("y = x ** 0.5", xytext=(7, 5), xy=(6, 2.6), ha='center',va='center',arrowprops={'arrowstyle':'->','color':'red'})
    plt.show()

if __name__ == "__main__":
    main()
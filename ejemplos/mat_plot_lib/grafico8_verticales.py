import matplotlib.pyplot as plt 

from random import randint

def main():
    Y = list(range(10))
   
    X1 = [randint(5,50) for x in Y]
    X2 = [randint(-50,-5) for x in X1]
     
    plt.barh(Y, X1, color='r',align='center')
    plt.barh(Y, X2, color='blue',align='center')
     
    plt.show()


if __name__ == "__main__":
    main()
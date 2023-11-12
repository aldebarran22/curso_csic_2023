
import matplotlib.pyplot as plt 

def main():
    X = list(range(10))
    X1 = [x+1/3 for x in X]
    X2 = [x+2/3 for x in X]

    Y1 = [x**0.5 for x in X]
    Y2 = [x for x in X]
    Y3 = [x**1.5 for x in X]
    Y4 = [x**2 for x in X]

    plt.grid(True)
    plt.bar(X, Y1, color='red', width=1/3, align='center')
    plt.bar(X1, Y2, color='blue', width=1/3, align='center')
    plt.bar(X2, Y3, color='orange', width=1/3, align='center')
   

    plt.show()


if __name__ == "__main__":
    main()
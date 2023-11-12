
import matplotlib.pyplot as plt 

def main():
    X = list(range(10))
    Y1 = [x**0.5 for x in X]
    Y2 = [x for x in X]
    Y3 = [x**1.5 for x in X]
    Y4 = [x**2 for x in X]

    plt.grid(True)
    plt.bar(X, Y1, color='red')
    plt.bar(X, Y2, color='blue', bottom=Y1)
    plt.bar(X, Y3, color='orange', bottom=Y2)
    plt.bar(X, Y4, color='green', bottom=Y3)

    plt.show()


if __name__ == "__main__":
    main()

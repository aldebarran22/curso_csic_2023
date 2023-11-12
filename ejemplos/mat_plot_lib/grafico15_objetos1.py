
import matplotlib.pyplot as plt 

from random import randint

def main():
    X = list(range(10))
    Y1 = [randint(1,10) for x in X]
    Y2 = [randint(1,10) for x in X]

    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    ax1.plot(X,Y1)
    ax1.set_ylim(0,10)

    ax2 = fig.add_subplot(122)
    ax2.plot(X,Y2)
    ax2.set_ylim(0,10)

    plt.show()


if __name__ == "__main__":
    main()
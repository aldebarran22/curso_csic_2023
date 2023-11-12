import matplotlib.pyplot as plt 

def prueba():
    d = {"Ana":43, "jorge":45, "Raul":12}
    plt.pie(d.values(), labels = list(d.keys()))
    plt.show()

def main():
    L = [23,6,7,44,1]
    plt.pie(L, labels=["Ana","Jorge","Maria","Miguel","Raul"], labeldistance=0.9)
    plt.show()

if __name__ == "__main__":
    main()
    #prueba()
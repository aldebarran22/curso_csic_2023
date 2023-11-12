import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(-2, 2, 11) # inicio, f
    y = np.linspace(-2, 2, 11)

    xmesh, ymesh = np.meshgrid(x,y)
    zmesh = np.sin((xmesh**2+ymesh**2)*0.5)

    #plt.scatter(xmesh, ymesh)
    #plt.contour(xmesh, ymesh, zmesh)
    con = plt.contourf(xmesh, ymesh, zmesh)
    plt.colorbar(con)
    plt.show()



if __name__ == "__main__":
    main()
import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fp = open('nodes.csv')
TArray = []
SArray = []
QArray = []

line = ""

for l in fp:
    count = 1
    line = l
    lineArray = line.split('\t')
    TArray.append(float(lineArray[0]))
    ##TArray.append(np.intc(lineArray[0]))
    SArray.append(float(lineArray[1]))
    ##SArray.append(np.float64(lineArray[1]))
    QArray.append(float(lineArray[2]))
    
    

fig = plt.figure()
ax = fig.gca(projection='3d')
##Day
X = TArray
##Size
Y = SArray
X, Y = np.meshgrid(X, Y)
##Feed
Z = QArray
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_zlim(-1, 225);

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

mpl.rcParams['legend.fontsize'] = 10

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
##z = np.linspace(0, 200, 100)
##r = z/2 + 1
##x = r * np.sin(theta) + 300
##y = r * np.cos(theta) + 350
##ax.plot(x, y, z, label='parametric curve')
##ax.legend()

plt.show()


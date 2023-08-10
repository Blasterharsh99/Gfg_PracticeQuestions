import matplotlib.pyplot as plt
import numpy as np

x=np.array((1,2,3,4,5))
y=np.array((1,4,9,16,25))
z=np.array((1,8,27,64,125))
#plt.plot(x,y)
plt.subplot(1,2,1)
#plt.scatter(x,y)
plt.bar(x,y)
plt.title("Squares")
plt.subplot(1,2,2)
#plt.scatter(x,z)
plt.title("Cubes")
plt.suptitle("Squares vs Cubes")
plt.bar(x,z)
plt.show()
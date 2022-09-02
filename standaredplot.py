import matplotlib.pyplot as plt 
import numpy as np 


# create a list of evenly spaced number
x = np.linspace(0, 20, 100);
#plot sign on each x point 
plt.plot(x, np.sin(x));

plt.show();
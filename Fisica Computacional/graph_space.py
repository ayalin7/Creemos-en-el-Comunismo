import numpy as np
import matplotlib.pyplot as plt
mu = 1
t = np.arange(0, 100, 0.1)
h = 0.01

pi = np.zeros(len(t))
delta = np.zeros(len(t))

for Delta0 in np.arange(1, 20, 0.1):
   pi[0] = 1.0
   delta[0] = Delta0
   for n in range(len(t)-1):
      pi[n+1] = pi[n] + h*pi[n]*(1-delta[n])
      delta[n+1] = delta[n] + h*mu*delta[n]*(pi[n+1]-1)
      plt.plot(delta, pi)


plt.show()

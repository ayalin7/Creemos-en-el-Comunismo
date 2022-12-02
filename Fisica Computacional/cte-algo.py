import numpy as np
import matplotlib.pyplot as plt

mu = 1
t = np.arange(0, 100, 0.1)
h = 0.1 
pi = np.zeros(len(t))
delta = np.zeros(len(t))
pi[0] = 0.3
delta[0] = 0.5

for n in range(len(t)-1):
    pi[n+1] = pi[n] + h*pi[n]*(1-delta[n])
    delta[n+1] = delta[n] + h*mu*delta[n]*(pi[n+1]-1)
 
C = np.log(delta) - delta + mu*(np.log(pi) - pi)

plt.plot(t, C)
plt.ylim(-10, 10)
plt.show()


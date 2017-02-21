import numpy
import matplotlib
from scipy import integrate
import matplotlib.pyplot as plt

def Blasius(f,t):
    return [f[1], f[2], -f[0]*f[2]/2]

def Pohl(x):
    return (2/5.8356)*x-(2/5.8356**3)*x**3+(1/5.8356**4)*x**4

AA = 0.;
BB = 1.;
tol = 1e-8
maxiter = 100
#z = numpy.linspace(0,5.8356,100)
z = numpy.linspace(0,10,1000)

CC = (AA+BB)/2.0
iter = 0

while (BB-AA)/2.0>tol and iter<maxiter:
      iter += 1
      Ainit=[0., 0., CC]
      Aprime = integrate.odeint(Blasius,Ainit,z)
      ODEC = 1-Aprime[-1,1]
      
      Ainit=[0., 0., AA]
      Aprime = integrate.odeint(Blasius,Ainit,z)
      ODEA = 1-Aprime[-1,1]      

      if ODEC==0:
           print(CC)
           break
      elif ODEC*ODEA<=0:
           BB = CC
      else:
           AA = CC
      
      CC = (AA+BB)/2.0


print("iterations needed=",iter)
print("best initial value=",CC)	 

Ainit=[0., 0., CC]
Aprime = integrate.odeint(Blasius,Ainit,z)


plt.figure(figsize=(5,5)) 
plt.plot(Aprime[:,1],z,label='Blasius')
plt.plot(Pohl(z),z,label='Pohlhausen')
plt.xlim([0., 1.])
plt.xlabel("u/U")
plt.ylabel("z")
plt.legend()
plt.savefig('Blasius_profile.png')




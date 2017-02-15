import numpy
import matplotlib
from scipy import integrate
import matplotlib.pyplot as plt

def Blasius(f,t):
    return [f[1], f[2], -f[0]*f[2]/2]

def derivative(f, x, h):
    deriv = (1.0/(2*h))*(f(x+h)-f(x-h))
    return deriv

AA = 0.;
BB = 1.;
tol = 0.00001
maxiter = 100
z = numpy.linspace(0,7,200)

CC = (AA+BB)/2.0
iter = 1

while (BB-AA)/2.0>tol and iter<maxiter:
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
      iter = iter+1

print("iterations needed=",iter)
print("best initial value=",CC)	 
         
plt.plot(Aprime[:,1],z)
plt.savefig('Blasius_profile.png')




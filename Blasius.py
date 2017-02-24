# Preamble, importing packages
import numpy
from scipy import integrate
import matplotlib.pyplot as plt

# Numerical solver of Blasius equation using odeint() and implementing bisection method to
# determine the correct value of the unknown initial condition f''(0). It prints the value 
# of the ratio u/U at predefined z and saves a figure of the profile. 


# Definition of generalised system of ODEs as a function
def Blasius(f,t):
    return [f[1], f[2], -f[0]*f[2]/2]


# Initialise the bisection method in terms of boundaries, tolerance and maximum number of 
# iterations.
AA = 0. # initial lower limit
BB = 1. # initial upper limit
tol = 1e-8 # tolerance
maxiter = 100 # max number of iterations

# Initialise array of z
z = numpy.linspace(0,6,6000)

# First guess of the value of the unknown Initial Condition
CC = (AA+BB)/2.0
iter = 0 # counting variable

# Bisection loop
while (BB-AA)/2.0>tol and iter<maxiter:
      iter += 1
      # Numerical calculation #1
      Ainit=[0., 0., AA]
      Aprime = integrate.odeint(Blasius,Ainit,z)
      ODEA = 1-Aprime[-1,1]
      
      # Numerical calculation #2
      Ainit=[0., 0., CC]
      Aprime = integrate.odeint(Blasius,Ainit,z)
      ODEC = 1-Aprime[-1,1]
            
      
      # Results check and preparation of next iteration
      if ODEC==0:
           break
      elif ODEC*ODEA<=0:
           BB = CC
      else:
           AA = CC
      # Next guess of the value of the unknown IC
      CC = (AA+BB)/2.0

# Information output
print("Iterations needed = ",iter)
print("Best guess for initial condition f''(0) = ",CC)


for ij in range(7):
    idx = (numpy.abs(z - ij)).argmin()
    print("At z = ",ij,"    u/U =  ",Aprime[idx,1])

	 




import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import math

'''
This script allows you to plot a slope field for a given first order differential equation of the form dy/dx = f(x,y)
'''
def differentialEquation(x,y): #input any differential equation of the form dy/dx = f(x,y)
    if(x != 0):
        slope = y/x**3
    else:
        slope = "undefined"
    return slope

lineLength = 0.25
minX = -10
maxX = 10
minY = -10
maxY = 10
step = 0.5


lines = []
i = minX

while i <= maxX:
    j = minY
    while j <= maxY:
        slope = differentialEquation(i,j)
        if slope != "undefined":
            print("Slope at ("+str(i)+","+str(j)+") =  "+str(slope))
            
            displacementX=(lineLength/(math.sqrt(1+(slope**2))))/2
            
            lowerX = i-displacementX
            lowerY = j+((slope*-1)*displacementX)
            
            upperX = i+displacementX
            upperY = j+(slope*displacementX)
                        
            lines.append([(lowerX,lowerY),(upperX,upperY)])
            
        else:
            print("Slope at ("+str(i)+","+str(j)+") is not defined")
        
        j += step 
    i += step                

lc = mc.LineCollection(lines)

fig, ax = plt.subplots()
plt.grid()
ax.add_collection(lc)
ax.margins(0.1)
plt.show()


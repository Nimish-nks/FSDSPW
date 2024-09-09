from sensor_read_class import ReadSensor
from matplotlib import pyplot as plt
#Additional libraries that may be used (try not use so many libraries) only what is required to ensure the program has minimum requirements
import math
#Refer to previous lab tasks to understand how Methods are called. Also check the class defined in sensor_read_class.py file
  

#maximum no of terations plotting should happen
max_iter=10

#Minimum and maximum distances to define workspace
#xyrange=[0, 1, -1, 1]

#define object
lscan=ReadSensor()
#define figure for plotting
fig = plt.figure()

#initialize iterat
iterat=1
icr_theta=0.017501922324299812
c=0
x=[]
y=[]
x_mean=[]
y_mean=[]
while (iterat<max_iter):
  #Obtain the data to be plotted after filtering within ranges
  a= list(lscan.get_laser_full())
  for i in a:
    theta = c*icr_theta
    x_c=i*math.cos(theta)
    y_c=i*math.sin(theta)
    if not math.isnan(i) and not math.isinf(i):
      x.append(x_c)
      y.append(y_c)
    c+=1
  plt.plot(x,y,color='red')
  plt.xlim(-3.5,3.5)
  plt.ylim(-3.5,3.5)  
  x_mean.append(sum(x)/len(x))
  y_mean.append(sum(y)/len(y))
  
print(x_mean)  
print(y_mean)
  
  	
  #Plot filtered values using  plt.plot(<xvalues>,<yvalues>,color=<color>,ls='None',marker=<marker>)
  #plot mean using plt.plot(<xvalues>,<yvalues>,color=<color>,marker=<marker>)
  #Set x and y limits plt.xlim(<xlimitmin>,<xlimitmax>) using xyrange
  #Set x and y limits plt.ylim(<ylimitmin>,<ylimitmax>) using xyrange
  #set label for axis plt.xlabel(<xlabel>)
  #set label for axis plt.ylabel(<ylabel>)    
plt.close('all')  

 

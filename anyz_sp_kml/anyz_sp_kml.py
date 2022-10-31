import os
import math
from math import radians,cos,sin,asin,sqrt
open_kml=open("E172B_SP_down.kml","r")
read_kml=open_kml.readlines()
kml_array=[]
def getDegree(latA, lonA, latB, lonB):  #Calculate the angle.
        latA=float(latA)
        lonA=float(lonA)
        latB=float(latB)
        lonB=float(lonB)
        radLatA = radians(latA)  
        radLonA = radians(lonA)  
        radLatB = radians(latB)  
        radLonB = radians(lonB)  
        dLon = radLonB - radLonA  
        y = sin(dLon) * cos(radLatB)  
        x = cos(radLatA) * sin(radLatB) - sin(radLatA) * cos(radLatB) * cos(dLon)  
        brng = math.degrees(math.atan2(y, x))  
        brng = (brng + 360) % 360  
        return brng
def split_data(data,count):
    for i in range(0,len(data),count):
        yield data[i:i+count]
#test_array=[1,2,3,4,5,6]
#a=list(split_data(test_array,2))
#print(a)


for i in read_kml:
    i=str(i).strip()
    if "coordinates" in i:
        kml_array.append(i)
WeNeedData=kml_array[-2]
Coverage_data=WeNeedData.split("<coordinates>")
not_clear_data=Coverage_data[1]
Coverage_data2=str(not_clear_data).split("</coordinates>")
Coverage_data3=Coverage_data2[0]#clear data
#print(Coverage_data3)
Coverage_data4=str(Coverage_data3).split(" ")
final_array=[]
for i in Coverage_data4:
    i=str(i)
    i_spl=i.split(",")
    final_array.append(float(i_spl[1]))
    final_array.append(float(i_spl[0]))
#print(final_array)
real_final_array=list(split_data(final_array,2))
print(real_final_array)
lat_array=[]
lon_array=[]
for i in real_final_array:
    lat_array.append(i[0])
    lon_array.append(i[1])
lat_init=0
lon_init=0

for i in range(0,len(lat_array),1):
    lat_init=lat_init+lat_array[i]
    lon_init=lon_init+lon_array[i]
lat_avrg=lat_init/len(lat_array)
lon_avrg=lon_init/len(lon_array)


print("----------------")
print(lat_avrg)
print(lon_avrg)
print("----------------")
degree_array=[]
for i in real_final_array:
    lat=i[0]
    lon=i[1]
    degree=getDegree(lat_avrg,lon_avrg,lat,lon)
    degree_array.append(lat)
    degree_array.append(lon)
    degree_array.append(degree)
    

#print(degree_array)
spl_degree_array=list(split_data(degree_array,3))
print(spl_degree_array)
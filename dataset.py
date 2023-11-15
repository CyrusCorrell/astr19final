import numpy as np


a = np.loadtxt('ASTR19_S22_group_project_data.txt', dtype='str')
i=0

date=[]
timetemp=[]
time=[]
height=[]

for arr in a:
	date.append(int(arr[0]))
	timetemp.append(arr[1])
	height.append(float(arr[2]))

for elem in timetemp:
	splitelem=elem.split(':')
	abstime = (int(splitelem[0])*60+int(splitelem[1]))
	time.append(abstime)
print(date,time,height)
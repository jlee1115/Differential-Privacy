import numpy as np
import dp_stats as dps
from matplotlib import pyplot as plt


NUM_BINS = 3

filename = "ozone.data"
#data = np.loadtxt(filename, delimiter = ",", skiprows = 2, usecols = [1])
data = np.genfromtxt(filename, delimiter = ",", usecols = [1],filling_values=99)

newData = []

print len(data)
for i in range(len(data)):
	if data[i] == 99:
		print 'Missing value'
	else:
		newData.append(data[i])


print(newData)
m = (max(newData))
print(m)

newData = newData/m


for i in range(len(newData)):
	if newData[i] >= 1 or newData[i] <=0:
		print(i, newData[i])
sum = 0
for i in range(len(newData)):
	sum = sum + newData[i]

dataMean = sum / len(newData)
#
#i = 0
#while i < len(data):
#	if data[i] >= 1 or data[i] <=0:
#		print(i, data[i])
#
#	i = i + 1




### example of mean and variance
# x = np.random.rand(10)
# sum = 0

# #print (sum / 10.0)


histogram = plt.figure()

# #print(x)
x_mu = dps.dp_mean(newData, 1.0, 0.1 )
#print(x_mu)
#print(dataMean)

hist = dps.dp_hist ( newData, num_bins=NUM_BINS, epsilon=1.0, delta=0.1, histtype = 'continuous' )


fakeData = np.zeros(len(newData))
print fakeData

j = 0
offset = 0
for j in range(NUM_BINS):
	i = 0
	val = (hist[1][j] + hist[1][j+1])/2.0
	while i < hist[0][j]:
		if (i + offset) < len(fakeData):
			fakeData[i + offset] = val
		i = i + 1
	offset = offset + int(round(hist[0][j]))


print fakeData


plt.hist([fakeData, newData], bins = hist[1], color = ['blue', 'green'])
plt.title("New vs. Fake Data")


plt.show()
#plt.show()

print(hist)

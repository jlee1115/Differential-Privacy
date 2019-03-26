import dp_stats as dps
from matplotlib import pyplot as plt


file = "AT_W27.csv"
pewData = np.loadtxt(file, delimiter = ",", usecols = [29], skiprows = 2)
d = []
for i in range(len(pewData)):
	if pewData[i] == 1:
		d.append(pewData[i])

print (len(d))
print (len(pewData))

print (float(len(d)) / len(pewData) ) #should be 40%

#Column 30
#Question: Do you think society generally treats men and women equally, or does it favor women over men, or
#men over women?
#1 - equally
#3 - favor women
#9 - favor men

NUM_BINS = 10

filename = "winequality-red.csv"
data = np.loadtxt(filename, delimiter = ";", skiprows = 2, usecols = [1])
residualSugar = np.loadtxt(filename, delimiter = ";", skiprows = 2, usecols = [3])
quality = np.loadtxt(filename, delimiter = ";", skiprows = 2, usecols = [11])

#print len(data)
#print(data)
m = (max(data))
#print(m)
ms = (max(residualSugar))
mq = (max(quality))


newData = data/m
newResidualSugar = residualSugar/ms
newQuality = quality/mq
sumData = newResidualSugar + newQuality
mm = max(sumData)
#print(m)
#How many wines high quality and high residual sugar

sugarsum = 0
for i in range(len(newResidualSugar)):
	sugarsum = sugarsum + newResidualSugar[i]

qualitysum = 0
for i in range(len(newQuality)):
	qualitysum = qualitysum + newQuality[i]

sum = 0
for i in range(len(newData)):
	sum = sum + newData[i]

dataMean = sum / len(newData)
residualSugarMean = sugarsum / len(newResidualSugar)
qualityMean = qualitysum / len(newQuality)


s = []

for i in range(len(newResidualSugar)):
	if newResidualSugar[i] > residualSugarMean and newQuality[i] > qualityMean:
		s.append(newResidualSugar[i])

#print(len(s))
#print(len(newResidualSugar))
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



# #print(x)
#x_mu = dps.dp_mean(newData, 1.0, 0.1 )
#print(x_mu)
#print(dataMean)

hist = dps.dp_hist ( s, num_bins=NUM_BINS, epsilon=0.1, delta=0.1, histtype = 'continuous' )

#histogram = plt.figure(1)

#plt.hist(newData, bins = hist[1])

#plt.title("new Data")



fakeData = np.zeros(len(newResidualSugar))
#print fakeData

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


#print newData
#print fakeData

#histogram2 = plt.figure(2)

#plt.hist([fakeData, newResidualSugar], bins = hist[1], color = ['blue', 'green'])
#plt.title("fake data (blue) and new data (green)")
#plt.legend("fakeDat", "real data")

#plt.show()



#print fakeData
################################################################
fakeData = np.zeros(len(newResidualSugar))
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


#print newData
#print fakeData

#histogram2 = plt.figure(2)

#plt.hist([fakeData, newData], bins = hist[1], color = ['blue', 'green'])
#plt.title("fake data (blue) and new data (green)")


#plt.show()

def createHistogram(data, bins, eps, figure):
	m = max(data)
	newData = data/m
	hist = dps.dp_hist (newData, num_bins=bins, epsilon=eps, delta=0.1, histtype = 'continuous' )


	fakeData = np.zeros(len(newData))
	j = 0
	offset = 0
	for j in range(bins):
		i = 0
		val = (hist[1][j] + hist[1][j+1])/2.0
		while i < hist[0][j]:
			if (i + offset) < len(fakeData):
				fakeData[i + offset] = val
			i = i + 1
		offset = offset + int(round(hist[0][j]))


	histogram2 = plt.figure(figure)
	plt.hist([fakeData, newData], bins = hist[1], color = ['blue', 'green'])
	plt.title("fake data (blue) and new data (green)")
	plt.show()


#createHistogram(s, 7, 0.1, 1)

epsilon = 0.01
fig = 1
while (epsilon <= 1):
	#createHistogram(s, NUM_BINS, epsilon, fig)
	epsilon = epsilon * 10
	fig = fig + 1

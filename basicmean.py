import numpy as np
import dp_stats as dps

x = np.random.rand(5)
print(x)

sum = 0
for i in range(5):
    sum = sum + x[i]

print "Actual mean is %f" % (sum/5.0)

x_mu = dps.dp_mean(x, 1.0, 0.1)
print "Noised mean is %f" % (x_mu)


print(dps.dp_hist (x, num_bins=3, epsilon=10, delta=0.1, histtype = 'discrete' ))

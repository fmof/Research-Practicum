import random
from matplotlib import pyplot as plt
import scipy.stats as stats
import math

def H():
	if random.randint(0,9) < 3:
		return random.gauss(-3, 1)
	else:
		return random.gauss(3,1)

vals = [H() for i in range(2000)]

F = 0
H = 0
I = 0
for i in vals:
	f = stats.norm.pdf(i, -3, 1)
	h = stats.norm.pdf(i, 3, 1)
	F += math.log(f)
	H += math.log(h)
	I += math.log(f * .3 + h * .7)
F /= len(vals)
H /= len(vals)
I /= len(vals)

print("F Score: {}".format(F))
print("G Score: {}".format(H))
print("Interpolated Score: {}".format(I))

plt.hist(vals, 20, facecolor='white')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.axis([-6,6, 0,400])
plt.show()
from matplotlib import pyplot as plt
import sys
import pickle

sys.path.append('/Users/puzzel/Documents/Git/twitter-kov')

with open('/Users/puzzel/Documents/Git/twitter-kov/TwitterKov/chaindata/twitter1T2O3V.pl', 'rb') as f:
	chain = pickle.load(f)
chain.margins.pop('')
vals = sorted(chain.margins.values(),reverse=True)
plt.plot(vals, 'ko')
plt.ylabel("Frequency")
plt.xlabel("Vocabulary Word")
plt.title("Frequency of Vocabulary Words in Twitter Data")
plt.xscale('log')
plt.yscale('log')
plt.xlim(xmin=0.8)
plt.ylim(ymin=0.8)
plt.show()

tons = {}
for val in vals:
	if val in tons:
		tons[val] += 1
	else:
		tons[val] = 1

temp = list(zip(*tons.items()))
x = temp[0]
y = temp[1]

plt.plot(x,y, 'ko')
plt.ylabel("Number of Distinct X-tons")
plt.xlabel("X, representing X-tons, a vocabulary word appearing X times")
plt.title("Number of Distinct X-tons in Twitter Data")
plt.xscale('log')
plt.yscale('log')
plt.xlim(xmin=0.8)
plt.ylim(ymin=0.8)
plt.show()
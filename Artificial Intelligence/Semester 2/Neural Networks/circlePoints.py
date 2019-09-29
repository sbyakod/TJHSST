import sys, random, math

training = []
result = []
for i in range(5):
	for j in range(1000):
		k = random.random() + i
		l = random.random() + i
		k = str(k)[0:6]
		k = float(k)
		l = str(l)[0:6]
		l = float(l)
		if(math.sqrt(k*k + l*l) < 1): result.append([1])
		else: result.append([0])
		training.append([k, l, 1])

print(training)
print(result)


import json

t1 = 0
t2 = 1
sigT = 0

res = []
obj = {}

terminos = int(input("Términos en serie: "))

print("Serie de Fibonacci:")

res.append(0)
res.append(1)

obj[0] = res[0]
obj[1] = res[1]

for i in range(2, terminos):

	sigT = t1 + t2

	t1 = t2
	t2 = sigT

	res.append(sigT)
	obj[i] = res[i]

json = json.dumps(obj)

print(json)
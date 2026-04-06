import numpy as np

def fa(z):
	return 1 if z >= 0 else 0

def predict(X,w,b):
	z=np.dot(X,w)+b
	return fa(z)

def train(X,y,train_pas=0.1,epochs=100):
	w = np.zeros(X.shape[1])
	b = 0

	for epoch in range(epochs):
		for i in range(len(X)):
			a=predict(X[i],w,b)

			error=y[i]-a

			b += error*train_pas*X[i]
			w += error*train_pas
	return w,b


X=np.array([[0,0],[1,1],[0,1],[1,0]])
y=np.array([0,1,0,0])

weight,bias=train(X,y)

for i in range(len(X)):

	print(f"for {X[i]} resultat predicted est { predict(X[i],weight,bias) } vrai resultat{y[i]}")

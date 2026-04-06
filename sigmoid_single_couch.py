def sigmoid(z):
	return 1/(1+np.exp(-z))

def predict(X,w,b):
	z=np.dot(X,w)+b
	return fa(z)
	

def derive_sigmoid(z):
	a=sigmoid(z)
	return a*(1-a)


def train(X,learn_rate=0.1,epochs=10):
	b=0
	w=np.zeros(X.shape[1])

	for epoch in range(epochs):

		for i in range(len(X))

			z=predict(X[i],w,b)
			a=sigmoid(z)

			error=y[i]-a
			
			gradient=error*derive_sigmoid(z)
			
			w+=learn_rate*X[i]*gradient

			b+=learn_rate*gradient
			
	return w,b

X=nparra([])
y=np.array



weight,bias=train(X,y)

for i in range(len(X))

    	print(f"for {X[i]} resultat predicted est { predict(X[i],weight,bias) } vrai resultat{y[i]}")
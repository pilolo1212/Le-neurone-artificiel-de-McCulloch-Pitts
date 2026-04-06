import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [1]])

np.random.seed(42)
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

weights_input_hidden = np.random.uniform(-1, 1, (input_neurons, hidden_neurons))
bias_hidden = np.zeros((1, hidden_neurons))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))
bias_output = np.zeros((1, output_neurons))

learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    error = y - predicted_output
    
    if epoch % 2000 == 0:
        loss = np.mean(np.square(error))
        print(f"Époque {epoch} - Erreur Quadratique Moyenne : {loss:.6f}")

    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

print("Entraînement terminé.")
print("--- Résultats des tests ---")

for i in range(len(X)):
    hidden_act = sigmoid(np.dot(X[i], weights_input_hidden) + bias_hidden)
    final_out = sigmoid(np.dot(hidden_act, weights_hidden_output) + bias_output)
    valeur_predite = final_out[0][0]
    resultat_arrondi = int(np.round(valeur_predite))
    print(f"Entrée : {X[i]} | Attendue : {y[i][0]} | Prédite : {valeur_predite:.4f} -> Résultat : {resultat_arrondi}")
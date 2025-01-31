import numpy as np

class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1):
        self.weights = np.zeros(n_inputs)
        self.bias = 0
        self.learning_rate = learning_rate

    def train(self, X, y, epochs=100):
        for _ in range(epochs):
            for x_i, target in zip(X, y):
                prediction = self.predict(x_i)
                update = self.learning_rate * (target - prediction)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_function(linear_output)

    def activation_function(self, x):
        return np.where(x >= 0, 1, 0)
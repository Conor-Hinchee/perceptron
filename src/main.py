import numpy as np
from perceptron import Perceptron

# Create perceptron with 2 input features
p = Perceptron(n_inputs=2)

# Example training data (OR gate)
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 1, 1, 1])

# Train
p.train(X, y)

# Test
print(p.predict([1, 0]))  # Should output 1
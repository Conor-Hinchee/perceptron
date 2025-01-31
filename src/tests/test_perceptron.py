import unittest
from src.perceptron import Perceptron
from src.data import load_data

class TestPerceptron(unittest.TestCase):

    def setUp(self):
        self.X, self.y = load_data('data/dataset.csv')
        self.perceptron = Perceptron(learning_rate=0.01, n_iter=1000)

    def test_fit(self):
        self.perceptron.fit(self.X, self.y)
        self.assertIsNotNone(self.perceptron.weights)

    def test_predict(self):
        self.perceptron.fit(self.X, self.y)
        predictions = self.perceptron.predict(self.X)
        self.assertEqual(len(predictions), len(self.y))

if __name__ == '__main__':
    unittest.main()
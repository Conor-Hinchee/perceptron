# README.md

# Perceptron Project

In machine learning, the perceptron is an algorithm for supervised learning of binary classifiers. A binary classifier is a function which can decide whether or not an input, represented by a vector of numbers, belongs to some specific class.[1] It is a type of linear classifier, i.e. a classification algorithm that makes its predictions based on a linear predictor function combining a set of weights with the feature vector. 

https://en.wikipedia.org/wiki/Perceptron

https://en.wikipedia.org/wiki/A_Logical_Calculus_of_the_Ideas_Immanent_in_Nervous_Activity

## Training a logical gate

Logical Gate Being Trained: OR Gate

OR gate truth table:

```
Input1  Input2  |  Output
  0       0    |    0
  0       1    |    1
  1       0    |    1
  1       1    |    1
```

Code Structure:

Training data X represents input pairs: [[0,0], [0,1], [1,0], [1,1]]
Labels y represent expected outputs: [0, 1, 1, 1]

1. Create perceptron with 2 inputs
2. Initialize training data for OR gate
3. Train perceptron
4. Test with input [1,1] (should output 1)


```python
[Input1]─┐
        [Perceptron]──>[Output (0 or 1)]
[Input2]─┘
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd perceptron-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   
3. Run the code:
   ```
   python main.py
   ```
# perceptron

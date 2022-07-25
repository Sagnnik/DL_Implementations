import numpy as np

class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward(self, input):
        pass

    def backward(self, output):
        pass

class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size)
        self.bias =  np.random.randn(output_size, 1)

    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input)+self.bias

    '''In backward propagation by gradient descent
       the gradient of the error = dE/dy
       the gradient of the weights = dE/dW = dE/dy.dy/dW = dE/dy.W(transpose)
       the gradient of the bias = dE/dB
       the gradient of that layer = W(transpose).dE/dy'''

    def backward(self, output_grad, learning_rate):
        weights_grad = np.dot(output_grad, np.transpose(self.input))
        self.weights -= learning_rate * weights_grad
        self.bias -= learning_rate * output_grad
        return np.dot(np.transpose(self.weights), output_grad)

class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward(self, input):
        self.input = input
        return self.activation(self.input)

    '''In Activation Layer
       the gradient of the layer = dE/dx = dE/dy.(element-wise multiply)f'(x) '''

    def backward(self, output_grad, learning_rate):
        return np.multiply(output_grad, self.activation_prime(self.input))

class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x)
        tanh_prime = lambda x: 1 - np.tanh(x)**2
        super.__init__(tanh, tanh_prime)


def mse(y_hat, y_pred):
    return np.mean(np.power((y_hat - y_pred), 2))

def mse_prime(y_hat, y_pred):
    return 2 * (y_pred - y_hat) / np.size(y_hat)
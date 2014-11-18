from core.learning.supervised_learning import SupervisedLearning
from impl.learning.error_functions.rms import RMS

__author__ = 'Douglas Eric Fonseca Rodrigues'


class LeastMeanSquare(SupervisedLearning):
    def __init__(self, neural_network, learning_rate, max_error, max_iterations=None, error_function=RMS()):
        """
        :type neural_network: core.neural_network.NeuralNetwork
        :type learning_rate: float
        :type max_error: float
        :type max_iterations: int
        :type error_function: core.learning.error_functions.error_function.ErrorFunction
        """
        SupervisedLearning.__init__(self, neural_network, learning_rate, max_error, max_iterations, error_function)

    def update_network_weights(self, output_error):
        for neuron, error in zip(self.neural_network.output_neurons, output_error):
            self.update_neuron_weights(neuron, error)

    def update_neuron_weights(self, neuron, error):
        """
        :type neuron: core.neuron.Neuron
        :type error: float
        """
        for connection in neuron.input_connections.values():
            connection.weight += connection.origin.output * error * self.learning_rate

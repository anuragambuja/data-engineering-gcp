
> ## Neural Networks

- ANN (artificial neural networks)
  - An ANN has three layers: an input layer, a hidden layer, and an output layer. Each node represents a neuron.
  - The lines between neurons stimulate synopses, which is how information is transmitted in a human brain.
  - The weights retain information that a neural network learned through the training process and are the mysteries that a neural network aims to discover.
  - An activation function is used to prevent linearity or add non-linearity. Without activation functions, the predicted result `y` will always be a linear function of the input `x`, regardless of the number of layers between input and output. you don’t need to have the same activation function across different layers.
    - rectified linear unit (or ReLU) function turns an input value to zero if it’s negative, or keeps the original value if it’s positive.
    - sigmoid function turns the input to a value between 0 and 1. It is used for binary class classification. eg. can be used to classify if email is smap or not.
    - hyperbolic tangent (Tanh) function shifts the sigmoid curve and generates a value between -1 and +1.
    - softmax is the activation function for multi-class classification. It maps each output to a [0,1] range in a way that the total adds up to 1. The output of softmax is a probability distribution. eg can be used in article classification: Github, NYTimes and TechCrunch
- Loss function is used to calculate errors for a single training instance, whereas cost function is used to calculate errors from the entire training set.

- DNN (deep neural networks)
- CNN (convolutional neural networks)
- RNN (recurrent neural networks)
- LLM (large language models)

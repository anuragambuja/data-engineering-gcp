
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

- Deep Leaning models:
1. Discriminative model: used to classify or predict labels for data. These models are typically trainied on the data set of labeled data points and they learn the relationship between the features of the data points and the labels. Once it is tranined, it can be used to predict the label for new data points. 
2. Generative Model: generated new data instances based on a leaned probability distribution of existing data. Generative models generate new contents. 



> ## Attention Mechanism
- Attention Mechanism is a technique which allows a neural network to focus on specific parts of an input sequence. This is done by assigning weights to different parts of the input sequence with the most important parts receiving the highest weights. The weighted sum of the input is then used as the input to the next layer of the neural network
- The attention mechanism lets the decoder focus on specific parts of the input sequence, which can improve the accuracy of the translation.
- The two main steps of the attention mechanism
	- Calculating the attention weights
 	- Generating the context vector
	  
- Traditional RNN encoder-decoder

	![image](https://github.com/user-attachments/assets/f2de56bd-d135-4b1b-938b-84152de6c2f2)

- Attention model differs from a traditional model in 2 main ways:
	- Encoder passes more data to decoder.

		![image](https://github.com/user-attachments/assets/8f62a9bd-c4da-4620-a1e9-876190597ad6)

	- Decoder Takes extra step before producing the output

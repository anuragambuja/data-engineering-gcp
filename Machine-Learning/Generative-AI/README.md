# Generative AI

- Gen AI is subset of deep learning which means it uses artificial neural networks, can process both labeled and unlabeled data using supervised, unsupervised and semi-supervised methods. 
LLM are also a subset of deep learning.
- It’s a type of artificial intelligence that generates content for you. The generated content can be multi-modal, including text, code, images, speech, video, and even 3D.

![image](https://github.com/user-attachments/assets/0a6d1d38-b7ab-4c86-87e0-4001a2b3db86)

- Gen AI workflow:

![image](https://github.com/user-attachments/assets/378479b8-ac31-4527-a50a-af31882ebc59)

1. Input prompt: Via the Vertex AI Studio UI, input a prompt—a natural language request to gen AI models.
2. Responsible AI and safety measures: The prompt undergoes responsible AI and safety checks, configurable through the UI or code.
3. Foundation models: The screened prompt proceeds to foundation models like Gemini multimodal or other gen AI models like Imagen and Codey based on your choices.
4. Model customization: Optionally, customize gen AI models to fit your data and use cases by further tuning them.
5. Results grounding: Gen AI models return results that undergo grounding (optional) and citation checks to prevent hallucinations.
6. Final response: The final response appears on the Vertex AI Studio UI after a final check through responsible AI and safety measures.

- lingos
	
	- multimodal model: It’s a large foundation model that is capable of processing information from multiple modalities, including text, image, and video. The generated content can also be in multiple modalities.
	- prompt: a prompt is a natural language request submitted to a model in order to receive a response.
 	- Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that expect a true or correct response, while higher temperatures can lead to more diverse, unexpected, or potentially biased results. With a temperature of 0 the highest probability token is always selected.temperature is a number used to tune the degree of randomness. Low temperature: Means to narrow the range of possible words to those that have high possibilities and are more typical. High temperature: It means to extend the range of possible words to include those that have low possibility and are more unusual. This setting is good if you want to generate more “creative” or unexpected content like an advertisement slogan.
  	- top K lets the model randomly return a word from the top K number of words in terms of possibility. For example, top 2 means you get a random word from the top 2 possible words including flowers and trees. Top P allows the model to return a random word from the smallest subset with the sum of the likelihoods that exceeds or equals to P. For instance, P of 0.75 means you sample from a set of words that have a cumulative probability greater than 0.75.
  	- Metaprompting is about creating prompts that guide the AI to generate, modify, or interpret other prompts.

- Zero-shot prompting is a method where the model is given a prompt that describes the task without additional examples. For example, if you want the LLM to answer a question, you just prompt "What is prompt design?"
- One-shot prompting is a method where the LLM is given a single example of the task that it is being asked to perform. For example, if you want the LLM to write a poem, you might provide a single example poem.
- Few-shot prompting is a method where the model is given a small number of examples of the task that it is being asked to perform.
- Role prompting: Role prompting is a technique used to guide the behavior of LLMs by assigning them a specific role or persona. This can be anything from a business analyst or Shakespearean actor to a helpful customer service agent.
- Prompt chaining: Continuing a conversation with the AI, maintaining context.
- Saved info: Storing persistent information for all your Gemini interactions, avoiding repetition and potential inconsistencies.
- Gem: Creating a personalized AI assistant with specific instructions and resources.

- Model Tuning

  ![image](https://github.com/user-attachments/assets/b3002888-d0b6-4ae3-b8a6-20aa08a7dc14)

	- Adapter tuning, which is supervised tuning. It lets you use as few as one hundred examples to improve model performance.
	- Reinforcement tuning, which is unsupervised reinforcement learning with human feedback.
	- Distillation, a more technical tuning technique, enables training smaller task-specific models with less training data, and lower serving costs and latency than the original model. This technology transfers knowledge from a larger model to a smaller model to optimize performance, latency, and cost. The rationale is to use a larger teacher model that trains smaller student models to perform specific tasks better and with improved reasoning capabilities. Rationales are like asking the model to explain why examples are labeled the way they are.

- Model Garden is like a model library, where you can search, discover, and interact with Google’s, third-parties’, and open-source gen AI models.
	- Categories of models:
 		- foundation models: Foundation models are pretrained, multitask, large models that can be tuned or customized for specific tasks by using Vertex AI Studio, Vertex AI APIs and SDKs. Some of these models are Gemini for multimodal processing, Embeddings for creating text and multimodal embeddings, Imagen for image, Chirp for speech, and Codey for code generation.
   		- task-specific solutions: Task-specific solutions are pre-trained models which are optimized to solve a specific problem. These include some tasks you practiced in the previous section by using Natural Language APIs, like entity analysis, sentiment analysis, and syntax analysis.
     		- fine-tunable or open-source models.  

- Vertex AI Studio: A tool that lets you quickly test and customize generative AI models so you can leverage their capabilities in your applications.
- categories of AI solutions provided by Google Cloud:
	- Vertical solutions, which focus on specific industries
 	- horizontal solutions, which solve problems across industries 

- Deep Leaning models:
1. Discriminative model: used to classify or predict labels for data. These models are typically trainied on the data set of labeled data points and they learn the relationship between the features of the data points and the labels. Once it is tranined, it can be used to predict the label for new data points. 
2. Generative Model: generated new data instances based on a leaned probability distribution of existing data. Generative models generate new contents. 

Not Gen AI when output is: number, discrete, class, probability.
Is Gen AI when Y is: natural language, Image, Audio.
So, Gen AI is a type of AI that creates new content based on what it has learned from existing content. The power of Gen AI comes from Transformers. Hallucinations make the output text difficult to understand and make the model more likely to generate incorrect or misleading information. 

A foundation model is a large AI model pre-trained on a vast quantity of data that is "designed to be adapted” (or fine-tuned) to a wide range of downstream tasks, such as sentiment analysis, image captioning, and object recognition.

A prompt is a short piece of text that is given to the large language model as input, and it can be used to control the output of the model in many ways.

Large Language Models(LLMs) are a subset of Deep Learning. It refer to large, general purpose language models that can be pre-trained and then fine-tuned for specific purposes. 
- Large: Large training dataset and large number of parameters (basicaly the memories and knowledge the machine learned from the model training). Parameters define the skill of the model in solving a problem such as predicting text. 
- General Purpose: model is sufficient to solve common problems. In ML few shot refers to training a model with minimal data nd zero shot implies that a model can recognize things that have not explicitly been taught in the training before. 

Pathways Language Model: In Apr'22, Google release PaLM
- has 540 billion parametera
- is a dense decoder only Transformer model (consists of Encoder(encodes the input sequence and passes to decoder) and decoder (learns how to decode the representations for a relevant task). 


Generative Language Model: LaMDA, PaLM, GPT etc
Kinds of LLMs:
1. Genric LM: predicts the next word(technically, token) based on the language in the training data. Think of it like autocomplete search.
2. Instruction tuned LM: Trainined to predict a response to the instructions given in the input. eg. generate a poem in the style of x, or give me a list of keywords based on semantic similarity for x.
3. Dialogue tuned LM: Trainined to have a dialogue by predicting the next response. These model are a special case of instruction tuned where requests are typically framed as a question to a chat box. 

Some of the challenges of using LLMs are that they can be expensive to train, they can be biased, and they can be used to generate harmful content.


There are three main concerns on large language models, hallucinations, factuality, and anthropomorphization.
1. In generative AI, hallucinations refer to instances where the AI model generates content that is the AI model generates content that is unrealistic, fictional, or completely fabricated.
2. Factuality relates to the accuracy or truthfulness of the information generated by a generative AI model.
3. Anthropomorphization refers to the attribution of human-like qualities, characteristics, or behaviors to non-human entities, such as machines or AI models.



 Google has also outlined the four areas of AI applications we will not pursue.Those AI applications that are likely to cause overall harm, weapons or other technologies whose principal purpose is to cause injury to people, surveillance violating internationally accepted norms, and those whose purpose contravenes international law and human rights.



	https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_python.ipynb



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


> ## History of AI

![image](https://github.com/user-attachments/assets/24559216-7ed8-42ad-915f-8a2a9ff9bd29)

- Types of AI Models:
  - Predictive AI: Used to make predictions or classifications based on input data
  - Generative AI: Creates new data based on the patterns it has learned from training data
-   






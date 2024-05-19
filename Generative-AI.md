
Gen AI is subset of deep learning which means it uses artificial neural networks, can process both labeled and unlabeled data using supervised, unsupervised and semi-supervised methods. 
LLM are also a subset of deep learning.

Deep Leaning models:
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

responsible AI: AI should 
1. be socially beneficial
2. avoid creating or reinforcing unfair bais
3. be built and tested for safety -  seeks to promote the safety—both bodily integrity and overall health of people and communities, as well as the security of places, systems, properties, and infrastructures from attack or disruption.
4. be accountable to people -  aims to respect people’s rights and independence. The principle aims to promote informed user consent, and it seeks to ensure that there is a path to report and redress misuse, unjust use, or malfunction.
5. incorporate privacy design principles - the aim is to protect the privacy and safety of both individuals and groups. It is also the goal of the principle to ensure that users have clear expectations of how data will be used, and that they feel informed and have the ability to give consent to that use.
6. uphold high standards of scienctific excellence - seeks to advance the state of knowledge in AI. This means to follow scientifically rigorous approaches and ensure that feature claims are scientifically credible.
7. be made available for uses that accord with these principles - The principle aims for the widest availability and impact of our beneficial AI technologies, while discouraging harmful or abusive AI applications.




There are three main concerns on large language models, hallucinations, factuality, and anthropomorphization.
1. In generative AI, hallucinations refer to instances where the AI model generates content that is the AI model generates content that is unrealistic, fictional, or completely fabricated.
2. Factuality relates to the accuracy or truthfulness of the information generated by a generative AI model.
3. Anthropomorphization refers to the attribution of human-like qualities, characteristics, or behaviors to non-human entities, such as machines or AI models.



 Google has also outlined the four areas of AI applications we will not pursue.Those AI applications that are likely to cause overall harm, weapons or other technologies whose principal purpose is to cause injury to people, surveillance violating internationally accepted norms, and those whose purpose contravenes international law and human rights.



	https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_python.ipynb



















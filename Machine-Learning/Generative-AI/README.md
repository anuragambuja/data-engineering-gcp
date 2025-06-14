# Generative AI

> ## Overview
- Gen AI is subset of deep learning which means it uses artificial neural networks, can process both labeled and unlabeled data using supervised, unsupervised and semi-supervised methods. 
LLM are also a subset of deep learning.
- It’s a type of artificial intelligence that generates content for you. The generated content can be multi-modal, including text, code, images, speech, video, and even 3D.
- History of Gen AI

  	<div align="center"> <img src="https://github.com/user-attachments/assets/24559216-7ed8-42ad-915f-8a2a9ff9bd29" alt="Alt Text" width="500" height="300"> </div>
	<div align="center"> <img src="https://github.com/user-attachments/assets/0a6d1d38-b7ab-4c86-87e0-4001a2b3db86" alt="Alt Text" width="800" height="300"> </div>

- Gen AI workflow:
	1. Input prompt: Via the Vertex AI Studio UI, input a prompt—a natural language request to gen AI models.
	2. Responsible AI and safety measures: The prompt undergoes responsible AI and safety checks, configurable through the UI or code.
	3. Foundation models: The screened prompt proceeds to foundation models like Gemini multimodal or other gen AI models like Imagen and Codey based on your choices.
	4. Model customization: Optionally, customize gen AI models to fit your data and use cases by further tuning them.
	5. Results grounding: Gen AI models return results that undergo grounding (optional) and citation checks to prevent hallucinations.
	6. Final response: The final response appears on the Vertex AI Studio UI after a final check through responsible AI and safety measures.
	
 	<div align="center"> <img src="https://github.com/user-attachments/assets/378479b8-ac31-4527-a50a-af31882ebc59" width="700" height="300"> </div>

- Gemini is a Google gen AI model that powers many different solutions.
	- Gemini app: The Gemini app is Google’s generative AI chatbot, where you can get help with writing, planning, learning, and more.
	- Gemini for Workspace: Gemini for Google Workspace integrates gen AI into familiar Workspace apps, allowing you to do things like compose emails in Gmail, generate images in Slides, and summarize notes in Meet.
	- Gemini for Google Cloud: Gemini for Google Cloud is your AI assistant for Google Cloud. It can help you write and debug code, manage and optimize cloud applications, analyze data in BigQuery, and strengthen your security posture.
 	- NotebookLM allows you to upload your files and then acts as a research assistant, summarizing key points, answering questions, and generating ideas, all while staying grounded in your source material. 

- Terms
	- Multimodal model: It’s a large foundation model that is capable of processing information from multiple modalities, including text, image, and video. The generated content can also be in multiple modalities.
	- Foundation models: Large AI models trained on massive datasets, allowing them to be adapted to many tasks. They are the basis of gen AI. Key Features of Foundation Models:
		- Trained on diverse data.
		- Flexible to a wide range of use cases.
		- Adaptable to specialized domains through additional, targeted training.
	- Prompt: A prompt is a natural language request submitted to a model in order to receive a response.
		- Zero-shot prompting is a method where the model is given a prompt that describes the task without additional examples. For example, if you want the LLM to answer a question, you just prompt "What is prompt design?"
		- One-shot prompting is a method where the LLM is given a single example of the task that it is being asked to perform. For example, if you want the LLM to write a poem, you might provide a single example poem.
		- Few-shot prompting is a method where the model is given a small number of examples of the task that it is being asked to perform.
		- Role prompting: Role prompting is a technique used to guide the behavior of LLMs by assigning them a specific role or persona. This can be anything from a business analyst or Shakespearean actor to a helpful customer service agent.
		- Prompt chaining: Continuing a conversation with the AI, maintaining context. Engaging in a back and forth conversation with the AI.
	- Large language models (LLMs): A type of foundation model that is designed to understand and generate human language.

- Google AI Studio and Vertex AI Studio
	- Both Google AI Studio and Vertex AI Studio allow you to experiment with and utilize Google's Gemini API, but they cater to different needs and levels of expertise.

  		<div align="center"> <img src="https://github.com/user-attachments/assets/9effa349-a5a9-4967-bc7e-0c37f383b252" width="700" height="300"> </div>


> ## Layers of Gen AI
<div align="center"> <img src="https://github.com/user-attachments/assets/1284c20d-d811-45ea-9d37-0d5e37902d44" width="600" height="200"> </div>

- Gen AI powered application: This is the layer that delivers the AI capability to users through interfaces.
- Agent: This layer utilizes the capabilities of the model layer to perform more complex actions. This layer interacts with the environment, gathers information and makes decisions and executes actions based on the information received. Think of agents as the intelligent pieces within a larger GenAI powered application.
	<div align="center"> <img src="https://github.com/user-attachments/assets/ee625c05-59ad-47f1-992a-589696565731" width="500" height="200"> </div>

 	- Evolution of Agents:
		- Deterministic agents (oldest): Agents that are built with predefined paths and actions. Same input will always produce same output.
			<div align="center"><img src="https://github.com/user-attachments/assets/75b9497e-0e12-4858-8479-da0db11344eb" width="500" height="200"> </div>	

	  	- Generative agents:Agents that are defined with natural language using LLMs to give a real conversational feel to your chatbot. These can be without RAG and with RAG(Newest)
			<div align="center"><img src="https://github.com/user-attachments/assets/8d1606f2-c324-4517-8c67-26e066045354" width="500" height="200"> </div>

   		- Hybrid Agents: These agents combine both deterministic and generative capabilities, and this combination makes them very powerful.

	- Key components of an agent:
   		<div align="center"> <img src="https://github.com/user-attachments/assets/1e3fb09a-c04a-473f-9908-552ae796217d" width="700" height="300"> </div>
     
		1. Reasoning loop: The reasoning loop is the agent's "thinking process." It's a continuous cycle of observing, interpreting, planning, and acting. This iterative process enables agents to analyze situations, plan actions, and adapt based on outcomes. The reasoning loop often utilizes advanced prompt engineering frameworks to guide its decision-making process. Examples of such Prompt engineering techniques include ReAct, chain-of-thought (CoT) prompting, Metaprompting.

  			- ReAct (Reason and Act) is a prompting framework that allows the language model to reason and take action on a user query, with or without in-context examples. ReAct, which stands for "reasoning and acting," is like giving an LLM a brain and a pair of hands. It allows the LLM to not only think about a problem but also take actions to solve it. Imagine you're asking an LLM to find you a good Italian restaurant nearby. ReAct can be used in Question-answering, Fact verification, Decision making etc.With ReAct, the LLM can:

				<div align="center"><img src="https://github.com/user-attachments/assets/5f024de9-f1ab-493d-8ad6-42b15c370da0" width="500" height="500"> </div>
    
				- Key components of ReAct:
					- Think: The LLM generates a thought about the problem, similar to CoT.
					- Act: The LLM decides what action to take, such as searching the web, accessing a database, or using a specific tool; the LLM specifies the input for the action, like a search query or database command.
					- Observe: The LLM receives feedback from the action, such as search results or database entries.
					- Respond: The LLM generates a response, which could involve providing an answer to the user, taking further actions, or formulating a new thought for the next iteration.
	
				- Why is ReAct important?
					- Dynamic problem solving: ReAct allows LLMs to tackle complex tasks that require interacting with external resources and adapting to new information.
					- Reduced hallucination: By grounding the LLM's reasoning in real-world data, ReAct can help reduce the risk of generating incorrect or nonsensical information.
					- Increased trustworthiness: The ability to see the LLM's reasoning process and how it interacts with external sources makes its responses more transparent and trustworthy.
			
			- Chain-of-thought (CoT) prompting is a technique where you guide a language model through a problem-solving process by providing examples with intermediate reasoning steps, helping it learn to approach new problems in a more structured and logical way.

				- Key components of CoT:
					- Self-consistency: Encouraging the LLM to generate multiple solutions and choose the most consistent one.
					- Active-prompting: Allowing the LLM to ask clarifying questions or request additional information.
					- Multimodal CoT: Combining text with other forms of data, like images or videos, to enhance reasoning.
	
				- CoT in action:
					- Complex reasoning tasks: LLMs can use CoT to break down complex problems into smaller, more manageable steps, leading to more accurate solutions in tasks like math word problems or logical reasoning puzzles.
					  - Explanation generation: LLMs can use CoT to generate step-by-step explanations for their answers, making their reasoning process transparent and understandable, which is crucial for building trust and identifying potential errors.
					  - Multi-step planning: LLMs can use CoT to plan and execute complex tasks that require multiple steps, such as writing a story, planning a trip, or debugging code.
	
				- while both ReAct and CoT enhance LLM reasoning, they have different strengths:
					- CoT focuses on internal reasoning, guiding the LLM through a chain of thought.
					- ReAct focuses on external interaction, allowing the LLM to gather information and take actions in the real world. 
 
    			- Metaprompting:
      				- Use prompting to guide the AI model to generate, modify, or interpret other prompts.

		3. Tools: Tools are functionalities that allow the agent to interact with its environment. Tools can be anything from accessing and processing data to interacting with software applications or even physical robots. This empowers agents to connect with real-world information and services, much like apps on our phones.
			- Types of agent tools:
				1. Extensions (APIs): Extensions provide a standardized way for agents to use APIs, regardless of the API's specific design. This simplifies API interaction, making it easier for agents to access external services and data. Example: An agent designed to book travel might use an extension to interact with a travel company’s API.
				2. Functions: Functions represent specific actions the agent can perform. An agent's reasoning system selects the appropriate function based on the task at hand. Example: A "calculate_price" function might take flight details and passenger information as input and return the total cost.
				3. Data stores: Data stores provide agents with access to information. This can include real-time data, historical data, or knowledge bases. Data stores ensure that the agent's responses are accurate, relevant, and up-to-date. Example: An agent might use a data store to access current weather conditions, stock prices, or a database of customer information.
				4. Plugins: Plugins extend the agent's capabilities by adding new skills or integrations. They can connect the agent to specific services, provide access to specialized tools, or enable interaction with particular platforms. Example: A plugin could enable an agent to interact with a calendar application, allowing it to schedule appointments. 
    
  - Examples of Agents:
	-  Conversational agents: Conversational agents are designed to understand what you mean, not just what you say, and respond in a way that makes sense. eg. Answering questions, Casual conversation etc.
	 
   		```
		You provide input >
		The agent understands >
			The agent calls a tool to gather additional information >
				The agent generates a response >
					The agent delivers the response
		```

	- Workflow agents: Workflow agents are designed to streamline your work and make sure things get done efficiently and correctly by automating tasks or going through complex processes. e.g. Ecommerce order fulfillment: An agent automatically processes orders, updates inventory, sends shipping notifications, and handles returns.

- Platform: This is the layer that consists of tools and services that help with building and deploying AI models. This includes model training platforms like Vertex AI and data management tools.
	- Vertex AI:
		- Vertex AI is Google Cloud's unified machine learning (ML) platform designed to streamline the entire ML workflow.
		- It provides the infrastructure, tools, and pre-trained models you need to build, deploy, and manage your ML and generative AI solutions.
		- Vertex AI gives you options for how to handle AI models for your project.
			- Model Garden: Pick from existing Google, third-party, or open-source models.
			- Model Builder: Train and use your own models. Go fully custom and create and train models at scale using an ML framework. Or use AutoML to create and train models with minimal technical knowledge and effort.

- Model: The model is where the brains of the AI system reside. It comprises various algorithms that learn patterns from data and can make predictions or generate new content. Examples are large language models (LLMs) like Gemini, image recognition models, and recommendation systems.

- Infrastructure: The foundation of any AI system, comprising the hardware (physical servers, cloud computing resources, specialized chips like GPUs and TPUs) and software (operating systems, networking) that provide the necessary computing power, storage, and connectivity to train, deploy, and scale AI models.
	- `AI on the edge`: You can run AI solutions on infrastructure (devices or servers) closer to where the action is happening.
	- Google provides tools like `Lite Runtime (LiteRT)` to help developers deploy AI models on edge devices.
	- `Gemini Nano` is Google's most efficient and compact AI model, specifically designed to run on devices.


> ## Data Quality
- There are five factors to focus on when thinking about data quality.
  - Accuracy
  - Completeness: Completeness refers to the size of a dataset as well as representation within the dataset. The size of the dataset is important because the model needs enough to make an accurate prediction. 
  - Representative: Data needs to be representative and inclusive, otherwise it can lead to skewed samples and biased outcomes. 
  - Consistency: The data must be relevant to the task the AI is designed to perform.
  - Relevance: 
- Secure AI Framework (SAIF) is used to establish security standards for building and deploying AI responsibly, addressing the unique challenges and threats in the AI landscape.


> ## Pricing for using models
- Tiers:
	- Usage-based: You pay for the amount you use, often measured in tokens or characters processed. This is common for APIs like Google’s PaLM & Gemini APIs.
	- Subscription-based: You pay a recurring fee for access to the model, often with tiers based on usage limits or features.
	- Licensing fees: One-time or recurring fees for using a model, especially for commercial purposes or embedding in products.
	- Free tiers: Some providers offer free access with limited usage for experimentation or non-commercial purposes.
- Factors affecting cost:
	- Larger, more capable models generally cost more.
	- A larger context window (the amount of text the model can consider) can increase costs.
	- Specialized features like fine-tuning or embedding can have separate pricing.
	- Depending on where you deploy your model and application, you may have compute based costs.


> ## NotebookLM
- NotebookLM is an AI-first notebook, grounded in your own documents, designed to help you gain insights faster.
- You can "ground" NotebookLM in specific sources like documents, presentations, or even audio and video files. This means your AI assistant will only use information from those sources to answer your questions and generate summaries.
- NotebookLM Plus: For users who want to take their research to the next level, there's NotebookLM Plus, a subscription plan that offers benefits like increased capacity, customization of response length and style, and usage analytics.
- NotebookLM Enterprise: NotebookLM Enterprise takes NotebookLM Plus to the next level by adding compliance and administrative features necessary for enterprise environments. This includes extra privacy and security features to give you enhanced control over your data. Your notebook information is only shared with your chosen collaborators, and you can manage access using predefined identity and access management (IAM) roles.
- NotebookLM versus Gems
  - Hyper-focused knowledge: Instead of drawing from a broad knowledge base, NotebookLM focuses solely on the sources you provide. This could be anything from research papers and articles to meeting notes and presentations.
  - Interactive learning: NotebookLM goes beyond simply summarizing information. It encourages active learning by allowing you to ask questions, generate different types of summaries, and even create quizzes to test your understanding.
  - Source-based answers: Every answer and insight provided by NotebookLM is directly grounded in your uploaded sources. This ensures accuracy and allows you to easily trace back to the original information. If you ask NotebookLM a question that isn't covered in the materials you've provided, it will honestly tell you that it can't answer. It won't invent information or speculate. This ensures that the information you get is always grounded in your sources and reliable.


> ## Vertex AI Search
- Vertex AI Search offers both search and recommendation solutions.
- Search allows you to create a powerful search experience for your public website. It can index and search across a variety of data types, including structured data in BigQuery and unstructured documents stored in Google Cloud Storage. This ensures your users can easily find the information they need on your website, regardless of how it's stored. Some specific forms of search includes Document search, Media search, Healthcare search, Search for commerce
- The general purpose recommendation engine can be used to recommend similar content within websites, documents, and other structured content. It analyzes user behavior and content attributes to provide personalized recommendations, increasing user engagement and content discovery. Some specific forms of recommendations are Media recommendations, Retail recommendations
- Vertex AI seamlessly connects to your existing data stores, whether they are structured databases, unstructured document repositories, or a combination of both. This connection is crucial as it allows Vertex AI Search to act as an agent, observing the user's query or context (the environment) and acting by retrieving relevant information or suggesting relevant items (using the data stores as tools) to achieve the goal of providing the right information or recommendation at the right time. Vertex AI Search also gives you the options of adding extra generative AI features to your search functionality such as Search summaries, Answers and follow ups. Vertex AI Search is built for enterprise and offers granular access controls to help ensure data security. It also provides advanced analytics to understand search trends and user behavior and scalable infrastructure to handle large volumes of data and search requests.


> ## Google’s Customer Engagement Suite
- Tools to support your company in engaging with customers effectively, which can be built on top of Google’s Contact Center as a Service (CCaaS), an enterprise-grade contact center solution that is native to the cloud.
- Conversational Agents
	- Conversational Agents to act as effective chatbots communicating with your customers. 
- Agent Assist
	- Agent Assist to support your live human contact center agents. Using AI and generative AI, Agent Assist can recommend agent responses to customers, suggest the appropriate knowledge base content to solve a customer’s issue, transcribe or translate calls in real time, summarize conversations and more.
	- Not all human agents are the same and they have different levels of experience. There can be a lot of training needed, especially when a new agent starts.
- Conversational Insights
	- Conversational Insights to gain insights into all your communications with customers (through chatbot agents or human agents).
	- This tool uses machine learning analytics to provide you with information such as agent and caller sentiment, entity identification, and call topics.
	- Contact center as a service (CCaaS)
	- CCaaS provides a complete contact center solution. It manages the infrastructure, integrates with CRMs, and offers omnichannel support (consistent experience across all channels, like websites, apps, phone, and text).
	- CCaaS seamlessly integrates with other Customer Engagement Suite tools, including Conversational Agents for automated support, Agent Assist for real-time agent guidance, and Conversational Insights for valuable data analysis.
  

> ## Google Agentspace
- Google Agentspace is designed to help you and your team use your company's information more effectively. It uses AI to create customized agents that can access and understand data from various sources, regardless of where that data is stored. These agents can then be integrated into your organization’s internal websites or dashboards.
- NotebookLM Enterprise as your specialized AI tool for diving deep into specific documents and web sources – asking questions, summarizing, and creating new content based only on those sources. Agentspace, on the other hand, is your comprehensive enterprise AI assistant. It uses AI agents and unified search to automate tasks and find information across all your connected business systems, not just specific documents you upload.
- You can think of Agentspace like your personal AI assistant for work. It helps employees find information, understand data, and automate tasks. It is designed to increase productivity for teams in a variety of fields like marketing, sales, HR, software, and research and development.


> ## Google Cloud's generative AI API's offerings
- Speech-to-Text API
	- The API converts speech into text.
	- It also transcribes audio and video content.
- Text-to-Speech API
  	- It converts text to natural-sounding speech.
	- The API also creates voice user interfaces and personalized communication.
- Translation API
  	- The Translation API translates text, documents, websites, audio and video files.
- Document Translation API
  	- It translates formatted documents while keeping the original layout.
- Document AI API
	- The Document AI API extracts data from varied formats.
	- It automates data capture and document processing.
	- The API can also summarize documents.
- Cloud Vision API
	- The API analyzes image content, tagging images based on detected objects and text.
	- It can also identify faces and landmarks.
	- The API supports use cases like content moderation and visual search.
- Cloud Video Intelligence API
	- Allows developers to analyze video content and extract meaningful info
	- Content recommendation, video search, and media analysis
- Natural Language API
	- Helps derive insights from unstructured text
	- Understand the sentiment of text, classify content, and extract important entities











> ## Others

- Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that expect a true or correct response, while higher temperatures can lead to more diverse, unexpected, or potentially biased results. With a temperature of 0 the highest probability token is always selected.temperature is a number used to tune the degree of randomness. Low temperature: Means to narrow the range of possible words to those that have high possibilities and are more typical. High temperature: It means to extend the range of possible words to include those that have low possibility and are more unusual. This setting is good if you want to generate more “creative” or unexpected content like an advertisement slogan.
- top K lets the model randomly return a word from the top K number of words in terms of possibility. For example, top 2 means you get a random word from the top 2 possible words including flowers and trees.
- Top P allows the model to return a random word from the smallest subset with the sum of the likelihoods that exceeds or equals to P. For instance, P of 0.75 means you sample from a set of words that have a cumulative probability greater than 0.75.
- Saved info: Storing persistent information for all your Gemini interactions, avoiding repetition and potential inconsistencies.
- Gem: Creating a personalized AI assistant with specific instructions and resources. Gems are personalized AI assistants within Gemini. They provide personalized responses tailored to specific instructions, streamline workflows like templates, prompts, and guided interactions.



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



- Types of AI Models:
  - Predictive AI: Used to make predictions or classifications based on input data
  - Generative AI: Creates new data based on the patterns it has learned from training data
-   






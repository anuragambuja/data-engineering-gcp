
> ## primary ways to use generative AI
- Create: Using generative AI to create new content, such as: 
  - Writing articles, emails, and social media posts.
    - Generate text responses to customer service inquiries using Conversational AI.
    - Draft emails to clients using Gemini in Gmail.
  - Creating images, videos, and audio
    - Create a custom image for a presentation using Gemini in Google Slides.
    - Generate multiple design concepts for brainstorming marketing materials such as website pages using Imagen.
    - Create video tutorials to guide customers through troubleshooting steps using Google Vids.
  - Generating code in various programming languages
    - Generate unit tests and other test cases for code, reducing the manual effort required for testing while still ensuring the code works as expected.
    - Generate code as a starting point for larger software development projects using Gemini Code Assist.
- Summarize: Condense large amounts of information into concise summaries, such as:
  - Summarizing long documents or articles
    - Summarize a lengthy financial report without having to read the entire document using NotebookLM Enterprise.
    - Summarize customer reviews to understand product feedback and sentiment using Gemini in Looker.
  - Extracting key takeaways from meetings or presentations
    - Project managers can automatically generate meeting notes that highlight key decisions and action items using Gemini in Google Meet.
    - Sales teams can use summaries to quickly recap client calls and identify next steps.
  - Creating concise reports from complex data
    - Transform complex data into easily understandable visuals like graphs using Gemini in BigQuery.
- Discover: Help your customers and employees find what they need at the right time, such as:
  - Uncovering hidden patterns and insights in data
    - Analyze purchase history and website traffic to predict future demand and optimize inventory using forecasting models on Vertex AI.
    - Identify viewing patterns of streaming viewers to recommend personalized content to subscribers, increasing engagement and reducing churn using Vertex AI Search.
    - Analyze vast datasets of molecular structures to identify potential drug candidates with higher success rates by fine-tuning models on Vertex AI.
  - Searching for resources or documents 
    - Search for a file or ask questions about its contents using Gemini in Google Drive.
    - Unlock enterprise expertise for employees with agents that bring together Gemini’s advanced reasoning, Google-quality search, and enterprise data, regardless of where it’s hosted using Google Agentspace.
  - Monitoring real-time events
    - Use anomaly detection to identify fraudulent transactions and prevent financial losses.
- Automate: Automate tasks that previously required human intervention, such as:
  - Automated format conversation
    - Convert content to accessible formats in real time by using Google Cloud's APIs, like Text-to-Speech, Speech-to-Text, Translation, and more.
  - Automated documentation
    - Analyze code and automatically generate clear and concise documentation, saving developers time and ensuring consistency using Codey. 
    - Automate contract review and information extraction with Document AI.
  - Automated notifications and alarms
    - Automate customer feedback analysis and ticket creation.
  
> ## Foundation model
- Foundation models are large-scale, general-purpose models trained on a massive amount of data. Examples: Gemini, Imagen, Chirp
- Foundation models, like other AI models, take in inputs, which are called prompts, to produce outputs.
- LLMs focus specifically on language-based tasks within the broader capabilities of foundation models.
- Key features of foundation models
  - Trained on diverse data: Foundation models are trained on a wide variety of data, allowing them to learn general patterns and relationships that can be applied to different tasks.
  - Flexible: With foundation models, one AI model can support a wide range of use cases.
  - Adaptable: Foundation models can be specialized for particular domains or use cases through additional, targeted training.
- Types:
  - Large language models (LLMs): They can translate languages, write different kinds of creative content, and answer your questions in an informative way, even if they are open ended, challenging, or strange. e.g. Gemini is a multimodal model that can process and generate various data types, including text, images, audio, and video, while Gemma is a family of lightweight, open models suitable for local deployments and specialized AI applications. Imagen is a text-to-image diffusion model that generates images from text, while Veo is a model capable of generating video content from text or images.
   - Diffusion models:  They excel in generating high-quality images, audio, and even video by iteratively refining noise (or unstructured/random data and patterns) into structured data.
 
 - Foundation model limitations
   - Data dependency: They require large datasets, and any biases or incompleteness in that data will inevitably seep into their outputs.
   - Knowledge cutoff: Models with older knowledge cutoffs may not know about recent events or discoveries. This can lead to incorrect or outdated answers, since AI models don't automatically update with the latest happenings around the world.
  - Bias: Due to their statistical learning nature, they can sometimes amplify existing biases present in the data. Even subtle biases in the training data can be magnified in the model's outputs.
  - Fairness: These evaluations typically focus on specific categories of bias, potentially overlooking other forms of prejudice. Consequently, these benchmarks do not provide a complete picture of all potential risks associated with the models' outputs, highlighting the ongoing challenge of achieving truly equitable AI.
  - Hallucinations: Because foundation models can't verify information against external sources, they may generate factually incorrect or nonsensical responses. .
  - Edge cases: Rare and atypical scenarios can expose a model's weaknesses, leading to errors, misinterpretations, and unexpected results.
- Techniques to overcome limitations:
  - Grounding: Grounding is the process of connecting the AI's output to verifiable sources of information—like giving AI a reality check. Grounding also anchors responses, ensuring the AI's answers are rooted in your provided data sources
    - Retrieval-augmented generation (RAG): RAG is a grounding method that uses search to find relevant information from a knowledge base and provides that information to the LLM, giving it necessary context. The first step is retrieval. When you ask an AI a question, RAG uses a search engine to find relevant information. This search engine uses an index that understands the semantic meaning of the text, not just keywords. This means it finds information based on meaning, ensuring higher relevance. The retrieved information is then added to the prompt given to the AI. This is the augmentation phase. The AI then uses this augmented prompt, along with its existing knowledge, to generate a response. This is referred to as the generation phase.
  - Prompt engineering: This involves crafting precise prompts to guide the model towards desired outputs. It refines results by understanding the factors that influence a model's responses. However, prompting is limited by the model's existing knowledge; it can't conjure information it hasn't learned.
  - Fine-tuning: Pre-trained models are powerful, but they're designed for general purposes. Tuning helps them excel in specific areas. Tuning involves further training a pre-trained or foundation model on a new dataset specific to your task. This process adjusts the model's parameters, making it more specialized for your needs. e.g. Fine-tuning a translation model to translate between specific languages or domains.
  - Humans in the loop (HITL): HITL systems integrate human input and feedback directly into the ML process.

    ![image](https://github.com/user-attachments/assets/add9336e-3404-442e-a359-bcc2d41d9b88)


> ## Data Quality
- There are five factors to focus on when thinking about data quality.
  - Accuracy
  - Completeness: Completeness refers to the size of a dataset as well as representation within the dataset. The size of the dataset is important because the model needs enough to make an accurate prediction. 
  - Representative: Data needs to be representative and inclusive, otherwise it can lead to skewed samples and biased outcomes. 
  - Consistency: The data must be relevant to the task the AI is designed to perform.
  - Relevance: 
- Secure AI Framework (SAIF) is used to establish security standards for building and deploying AI responsibly, addressing the unique challenges and threats in the AI landscape.

  > ## Factors when choosing a model for GenAI Use Case
  - Modality: Modality refers to the type of data the model can process and generate, such as text, images, video, or audio
  - Context Window: The context window refers to the amount of information a model can consider at one time when generating a response. A larger context window allows the model to "remember" more of the conversation or document, leading to more coherent and relevant outputs, especially for longer texts or complex tasks. However, larger context windows often come with increased computational costs. You need to balance the need for context with the practical limitations of your resources.
  - Security: Security is paramount, especially when dealing with sensitive data.
  - Availability and reliability: The availability and reliability of the model are crucial for production applications. Consider factors like uptime guarantees, redundancy, and disaster recovery mechanisms.
  - Cost: Evaluate the cost-effectiveness of the model in relation to your budget and the expected value of your application.
  - Performance: Evaluate the model's performance on relevant benchmarks and datasets. Consider the trade-offs between performance and cost.
  - Fine-tuning and customization: If you have a specialized use case, consider models that offer fine-tuning capabilities.
  - Ease of integration: Look for models that offer well-documented APIs and SDKs.

> ## Layers of Gen AI
- Gen AI powered application: This is the layer that delivers the AI capability to users through interfaces.
- Agent: This layer utilizes the capabilities of the model layer to perform more complex actions. This layer interacts with the environment, gathers information and makes decisions and executes actions based on the information received. Think of agents as the intelligent pieces within a larger gen AI powered application. They bring specific capabilities to the table.
  -  Conversational agents: Conversational agents are designed to understand what you mean, not just what you say, and respond in a way that makes sense. eg. Answering questions, Casual conversation etc.
        `You provide input > The agent understands > The agent calls a tool to gather additional information > The agent generates a response > The agent delivers the response`
  - Workflow agents: Workflow agents are designed to streamline your work and make sure things get done efficiently and correctly by automating tasks or going through complex processes. e.g. Ecommerce order fulfillment: An agent automatically processes orders, updates inventory, sends shipping notifications, and handles returns.
  - Agents key elements:
    - Reasoning loop: The reasoning loop is the agent's "thinking process." It's a continuous cycle of observing, interpreting, planning, and acting. This iterative process enables agents to analyze situations, plan actions, and adapt based on outcomes. The reasoning loop often utilizes advanced prompt engineering frameworks to guide its decision-making process. Examples of such frameworks include ReAct or chain-of-thought (CoT) prompting. These frameworks can include:
      - Simple rule-based calculations
      - Complex thought chains
      - Machine learning algorithms
      - Probabilistic reasoning techniques
    - Tools: Tools are functionalities that allow the agent to interact with its environment. Tools can be anything from accessing and processing data to interacting with software applications or even physical robots. This empowers agents to connect with real-world information and services, much like apps on our phones.  
- Platform: This is the layer that consists of tools and services that help with building and deploying AI models. This includes model training platforms like Vertex AI and data management tools.
- Model: The model is where the brains of the AI system reside. It comprises various algorithms that learn patterns from data and can make predictions or generate new content. Examples are large language models (LLMs) like Gemini, image recognition models, and recommendation systems.
- Infrastructure: The foundation of any AI system, comprising the hardware (physical servers, cloud computing resources, specialized chips like GPUs and TPUs) and software (operating systems, networking) that provide the necessary computing power, storage, and connectivity to train, deploy, and scale AI models.

  ![image](https://github.com/user-attachments/assets/1284c20d-d811-45ea-9d37-0d5e37902d44)




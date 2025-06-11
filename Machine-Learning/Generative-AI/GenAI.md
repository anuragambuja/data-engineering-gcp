
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
    - Retrieval-augmented generation (RAG): RAG is a grounding method that uses search to find relevant information from a knowledge base and provides that information to the LLM, giving it necessary context. The first step is retrieval. When you ask an AI a question, RAG uses a search engine to find relevant information. This search engine uses an index that understands the semantic meaning of the text, not just keywords. This means it finds information based on meaning, ensuring higher relevance. The retrieved information is then added to the prompt given to the AI. This is the augmentation phase. The AI then uses this augmented prompt, along with its existing knowledge, to generate a response. This is referred to as the generation phase. One way to start using a RAG system without any coding or database development is with a tool called NotebookLM. RAG involves:
      - Retrieval: The AI model first retrieves relevant information from a vast knowledge base (like a database, a set of documents, or even the entire web). This retrieval process is often powered by sophisticated techniques, like semantic search or vector databases.
      - Augmentation: The retrieved information is then incorporated (or "augmented") into the prompt that is fed to the LLM. This augmented prompt now contains both the user's original query and the relevant context retrieved from external sources.
      - Generation: The model then uses this retrieved information to generate the final output. This could be anything from answering a question to writing a creative story.
   
      
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
    - Reasoning loop: The reasoning loop is the agent's "thinking process." It's a continuous cycle of observing, interpreting, planning, and acting. This iterative process enables agents to analyze situations, plan actions, and adapt based on outcomes. The reasoning loop often utilizes advanced prompt engineering frameworks to guide its decision-making process. Examples of such frameworks include ReAct or chain-of-thought (CoT) prompting.
      - ReAct is a prompting framework that allows the language model to reason and take action on a user query, with or without in-context examples. ReAct, which stands for "reasoning and acting," is like giving an LLM a brain and a pair of hands. It allows the LLM to not only think about a problem but also take actions to solve it. Imagine you're asking an LLM to find you a good Italian restaurant nearby. ReAct can be used in Question-answering, Fact verification, Decision making etc.With ReAct, the LLM can:

          ![image](https://github.com/user-attachments/assets/5f024de9-f1ab-493d-8ad6-42b15c370da0)
        - Key components of ReAct:
          - Think: The LLM generates a thought about the problem, similar to CoT.
          - Act: The LLM decides what action to take, such as searching the web, accessing a database, or using a specific tool; the LLM specifies the input for the action, like a search query or database command.
          - Observe: The LLM receives feedback from the action, such as search results or database entries.
          - Respond: The LLM generates a response, which could involve providing an answer to the user, taking further actions, or formulating a new thought for the next iteration.

        - Why is ReAct important?
          - Dynamic problem solving: ReAct allows LLMs to tackle complex tasks that require interacting with external resources and adapting to new information.
          - Reduced hallucination: By grounding the LLM's reasoning in real-world data, ReAct can help reduce the risk of generating incorrect or nonsensical information.
          - Increased trustworthiness: The ability to see the LLM's reasoning process and how it interacts with external sources makes its responses more transparent and trustworthy.

      - Chain-of-thought prompting is a technique where you guide a language model through a problem-solving process by providing examples with intermediate reasoning steps, helping it learn to approach new problems in a more structured and logical way.
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
        
      - These frameworks can include:
        - Simple rule-based calculations
        - Complex thought chains
        - Machine learning algorithms
        - Probabilistic reasoning techniques
    - Tools: Tools are functionalities that allow the agent to interact with its environment. Tools can be anything from accessing and processing data to interacting with software applications or even physical robots. This empowers agents to connect with real-world information and services, much like apps on our phones.
      - Types of agent tools:
        - Extensions (APIs): Extensions provide a standardized way for agents to use APIs, regardless of the API's specific design. This simplifies API interaction, making it easier for agents to access external services and data. Example: An agent designed to book travel might use an extension to interact with a travel company’s API.
        - Functions: Functions represent specific actions the agent can perform. An agent's reasoning system selects the appropriate function based on the task at hand. Example: A "calculate_price" function might take flight details and passenger information as input and return the total cost.
        - Data stores: Data stores provide agents with access to information. This can include real-time data, historical data, or knowledge bases. Data stores ensure that the agent's responses are accurate, relevant, and up-to-date. Example: An agent might use a data store to access current weather conditions, stock prices, or a database of customer information.
        - Plugins: Plugins extend the agent's capabilities by adding new skills or integrations. They can connect the agent to specific services, provide access to specialized tools, or enable interaction with particular platforms. Example: A plugin could enable an agent to interact with a calendar application, allowing it to schedule appointments. 
   
        
    - key components of an agent:
      - Foundational Model: This is the underlying language model (LLM) that powers the agent. It could be a small or large language model, a Google model like Gemini, or a model from another provider. The key is to select a model with training data relevant to the agent's intended use case.
      - Tools: Tools enable the agent to interact with the outside world. These can include extensions that connect to APIs, functions that act as mock API calls, and data stores like vector databases. Tools allow the agent to not only observe the world but also act upon it.

      - Reasoning Loop: This is the core of the agent, responsible for making decisions and taking actions. It's an iterative process where the agent considers its goal, the available tools, and the information it has gathered. Frameworks like ReAct (Reason and Act) are commonly used to guide the reasoning process.
    - Evolution of Agents:
      - Deterministic agents (oldest): Same input will always produce same output.
          ![image](https://github.com/user-attachments/assets/75b9497e-0e12-4858-8479-da0db11344eb)
      - Generative agents:
        - without RAG
        - with RAG (Newest)
        
        ![image](https://github.com/user-attachments/assets/8d1606f2-c324-4517-8c67-26e066045354)

- Platform: This is the layer that consists of tools and services that help with building and deploying AI models. This includes model training platforms like Vertex AI and data management tools. 
- Model: The model is where the brains of the AI system reside. It comprises various algorithms that learn patterns from data and can make predictions or generate new content. Examples are large language models (LLMs) like Gemini, image recognition models, and recommendation systems.
- Infrastructure: The foundation of any AI system, comprising the hardware (physical servers, cloud computing resources, specialized chips like GPUs and TPUs) and software (operating systems, networking) that provide the necessary computing power, storage, and connectivity to train, deploy, and scale AI models.

  ![image](https://github.com/user-attachments/assets/1284c20d-d811-45ea-9d37-0d5e37902d44)



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


> ## Gems
- Gems are AI assistants that can process information and reason over complex ideas within the context of your chosen task.
  - Gems can be tailored with specific instructions and information. This allows them to provide responses that are more relevant to your needs and preferences within that particular use case.
  - Gems can help you streamline repetitive tasks by providing templates, prompts, or guided interactions. This can save you time and effort when working on familiar projects or activities.
  - You can set the context for a Gem, like giving it background information or specific instructions. Then, you can start multiple chats with that Gem, each with its own focus and flow. These chats remain separate, so information from one won't spill over into another. It's like having different conversations with the same expert, each tailored to a specific purpose.


> ## NotebookLM
- NotebookLM is an AI-first notebook, grounded in your own documents, designed to help you gain insights faster.
- You can "ground" NotebookLM in specific sources like documents, presentations, or even audio and video files. This means your AI assistant will only use information from those sources to answer your questions and generate summaries.
- NotebookLM Plus: For users who want to take their research to the next level, there's NotebookLM Plus, a subscription plan that offers benefits like increased capacity, customization of response length and style, and usage analytics.
- NotebookLM Enterprise: NotebookLM Enterprise takes NotebookLM Plus to the next level by adding compliance and administrative features necessary for enterprise environments. This includes extra privacy and security features to give you enhanced control over your data. Your notebook information is only shared with your chosen collaborators, and you can manage access using predefined identity and access management (IAM) roles.
- NotebookLM versus Gems
  - Hyper-focused knowledge: Instead of drawing from a broad knowledge base, NotebookLM focuses solely on the sources you provide. This could be anything from research papers and articles to meeting notes and presentations.
  - Interactive learning: NotebookLM goes beyond simply summarizing information. It encourages active learning by allowing you to ask questions, generate different types of summaries, and even create quizzes to test your understanding.
  - Source-based answers: Every answer and insight provided by NotebookLM is directly grounded in your uploaded sources. This ensures accuracy and allows you to easily trace back to the original information. If you ask NotebookLM a question that isn't covered in the materials you've provided, it will honestly tell you that it can't answer. It won't invent information or speculate. This ensures that the information you get is always grounded in your sources and reliable.
 
> ## Ways to improve your output
- Sampling parameters and settings: Sampling parameters act as settings that influence the AI model's behavior, giving you more customized results. Think of these as knobs and dials you can adjust with your prompt input to impact the model's output. By tweaking these settings, you can ensure the model's output aligns with your specific needs, whether it's generating more creative text, providing more concise summaries, or staying within a certain tone. Most common parameters you can adjust are:
  - Token count: Imagine each word and punctuation mark in your text as a character. These characters are grouped into smaller units called tokens, which represent meaningful chunks of text. Models have limits on how many tokens they can handle at once. A higher token count allows for longer and more complex conversations, but it also requires more processing power. For example, one token is roughly equivalent to four characters in English. So, a hundred tokens would be about sixty to eighty words.
  - Temperature: This parameter controls the "creativity" of the model, because it adjusts the randomness of word choices during text generation, influencing the diversity and unpredictability of the output. A higher temperature makes the output more random and unpredictable, while a lower temperature makes it more focused, deterministic and repeatable.
  - Top-p (nucleus sampling): "Top-p" stands for the cumulative probability of the most likely tokens considered during text generation. This is another way to control the randomness of the model's output. It concentrates the probability on the most likely tokens, making the output more coherent and relevant. A lower top-p value leads to more focused responses (i.e. only the most probable tokens), while a higher value allows for more diversity (i.e. extending to lower probability tokens as well). The model retuns a random word from the smallest subset with the sum of the likelihoods that exceeds or equals to P.

    ![image](https://github.com/user-attachments/assets/48de0d44-69a4-46d4-b15d-84cb5c66c340)

  - Top-k: The model returns a random word from a set of top K possible words.

      ![image](https://github.com/user-attachments/assets/a61f7194-bcbc-43e9-bd30-01ad2d5eeea9)

  - Safety settings: These settings allow you to filter out potentially harmful or inappropriate content from the model's output. You can adjust the level of filtering based on your specific needs and preferences.
  - Output length: This determines the maximum length of the generated text. You can set it to a specific number of words or characters or allow the model to generate text until it reaches a natural stopping point.

> ## Google AI Studio and Vertex AI Studio
- Both Google AI Studio and Vertex AI Studio allow you to experiment with and utilize Google's Gemini API, but they cater to different needs and levels of expertise.

  ![image](https://github.com/user-attachments/assets/9effa349-a5a9-4967-bc7e-0c37f383b252)

  

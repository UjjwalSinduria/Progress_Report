- [x] **What is genAI?**
    *   Generative AI is a branch of Artificial Intelligence focused on creating content, including:
        *   **Text** : Summaries, articles, reports, etc(eg chatGPT)
        *   **Images** : Art, designs, synthetic visuals.
        *   **Videos** : Animations, simulations
        *   **Audio** : Music, Speech synthesis
        *   **Code** : Automated coding or debuging
    *   Generative AI relies heavily on advanced machine learning models like transformers(eg. GPT,Bert)
    and techniques such as **Diffusion models** for image generation

- [x] **What are Transformers?**
    *   Transformers are the class of machine learning models designed for sequence-to-sequence tasks, such as text, audio, and more. They have revolutionized the field of Natural Language processing(NLP) and now begin extended into other domains like computer vision and Generative AI
    *   **Transformer Architecture**: Transformers rely on a mechanism called **self-attention** to process input sequences in parallel
    rather than sequentially (as in RNNs).
    *   **RNN(Recurrent Neural Network)**: 
        *   Old neural networks input and outputs are treated independently, but this is not in the case of RNN.
        RNN is advanced neural network which fed input as its prev output(Means the output of one step fed as an input to the next, allowing them to retian information from previous inputs)
        *   This design Makes RNN well suited for tasks where context from earlier step is essential, such as predicting the next word in a sentence.   
    *   **Core Component on transformer**:
        *   **Encoder**: Processes input sequences(eg: word in a sentence).
        *   **Decorder**: Generates the output sequences (e.g., translations, answers).
        *   **Self Attention Machanism**: Identifies relationships between words or tokens, enabling context awareness.
        *   **Positional Encoding**: Helps the model to understand the order of input tokens.
    *   **KEY Transformer Models**: 
        *   **GPT(Generative Pre-Trained Transformer)**:
            *   Developed by OpenAI, GPT is unidirectional transformer model focused on the text generation and understanding.
            * **How it Works**
                *   PreTrained on large datasets(unsupervised learning)
                *   Fine-tuned for specific tasks(supervised learning)
        *   **BERT (Bidirectional Encoder Representations from Transformers)**
            *   Developed by google, BERT is a bidirectional transformer model focused on understanding the context of word from both left and right of a sentence.
            * **How it works**:
                *   **Uses masked language modeling (MLM)**: Randomly maskes words in a sentence and predicts them based on context.
                *   **Incorporates next sentence prediction (NSP)**: Determines if one sentence follows another logically.

- [x] **How Transformers are used in generative AI**
    *   Transformers serves as the backbone for generative AI applications by understanding and creating complex data patterns.
    *   **Generative AI workFlow using Transformer**:
        *   **Pre-Training**:
            *   Train model on a large scale dataset.
            *   Enables the model to learn languages structures or visual patterns.
        *   **Fine Tuning**:
            *   Adapt the pre-trained model to specific tasks using smaller, domain-specific datasets.
        *   **Inference**:
            *   Deploy the model real-world applications.
            *   Eg: Using a deployed model GPT-4 model for chatbot conversations.

- [x] **AWS Services for Transformers**:
    *   **Amazon SageMaker**:  Pre-train, fine-tune, and deploy Transformer model
    *   **Amazon BedRock**: Direct access to pre-trained transformer-based foundations models.
    *   **AWS Inferentia**: Accelerates inferences for transformer models.
        







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
        *   Old neural networks are treated independently, but this is not in the case of RNN.
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
            * **How its Works**
                *   PreTrained on large datasets(unsupervised learning)
                *   Fine-tuned for specific tasks(supervised learning)
        







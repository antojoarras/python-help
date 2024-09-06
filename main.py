# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Load the knowledge base (a dictionary of Python concepts and their explanations)
knowledge_base = {
    "variable": {"example": "x = 5", "explanation": "A variable is a named storage location that holds a value."},
    "loop": {"example": "for i in range(5): print(i)", "explanation": "A loop is a control structure that allows code to be executed repeatedly."},
    "function": {"example": "def greet(name): print(f'Hello, {name}!')", "explanation": "A function is a block of code that can be called multiple times with different inputs."},
    # Add more concepts to the knowledge base as needed
}

# Define a function to tokenize the input text
def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

# Define a function to perform part-of-speech tagging
def pos_tagging(tokens):
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens

# Define a function to detect the intent of the user's input
def detect_intent(tagged_tokens):
    intent = ""
    for token, tag in tagged_tokens:
        if tag in ["NN", "NNS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:  # Check for noun or verb tokens
            intent = "question"
            break
    return intent

# Define a function to generate a response based on the intent and input tokens
def generate_response(intent, tokens, pos_tags, knowledge_base):
    response = ""
    if intent == "question":
        concept = tokens[0]
        if concept in knowledge_base:
            response = "Here's an example of {}: {}".format(concept, knowledge_base[concept]["example"])
        else:
            response = "Sorry, I don't know about {}.".format(concept)
    elif intent == "help_request":
        concept = tokens[0]
        if concept in knowledge_base:
            response = "Here's a brief explanation of {}: {}".format(concept, knowledge_base[concept]["explanation"])
        else:
            response = "Sorry, I don't know about {}.".format(concept)
    return response

# Define the main function to handle user input
def main():
    while True:
        user_input = input("Enter your question or request: ")
        tokens = tokenize_text(user_input)
        pos_tags = pos_tagging(tokens)
        intent = detect_intent(pos_tags)
        response = generate_response(intent, tokens, pos_tags, knowledge_base)
        print(" response: ", response)

# Call the main function to start the program
if __name__ == "__main__":
    main()

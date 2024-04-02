import openai  # Import the openai module to interact with the OpenAI API
import os  # Import the os module to interact with the operating system

class Chatbot:  # Define a class named Chatbot
    def __init__(self):  # Define the initializer method for the Chatbot class
        openai.api_key = os.getenv("OPEN_API")  # Set the OpenAI API key from an environment variable

    def get_response(self, user_input):  # Define a method to get a response from the chatbot
        # Use the ChatCompletion.create method to generate a response
        # The model parameter specifies the model to use
        # The messages parameter is a list of messages to set the context for the response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        # Return the content of the first choice's message from the response
        return response['choices'][0]['message']['content']

if __name__ == "__main__":  # If this script is run directly (not imported as a module)
    chatbot = Chatbot()  # Create an instance of the Chatbot class
    # Get a response from the chatbot to the prompt "Teach me Machine Learning in 30 days"
    response = chatbot.get_response("Teach me Machine Learning in 30 days")
    print(response)  # Print the response


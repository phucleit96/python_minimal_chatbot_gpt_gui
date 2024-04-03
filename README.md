# Chatbot Application
![DEMO](https://i.imgur.com/F4wkVq1.gif)
This project is a simple chatbot application built with Python, PyQt6, and OpenAI's GPT-3.5-turbo model.

## Features

- A GUI for user interaction, built with PyQt6.
- Real-time chat functionality.
- Uses OpenAI's GPT-3.5-turbo model for generating chatbot responses.
- The chatbot's response retrieval is threaded to keep the GUI responsive.

## Files

- `main.py`: This file contains the `ChatbotWindow` class which is responsible for creating the GUI and handling user interactions.
- `backend.py`: This file contains the `Chatbot` class which interacts with the OpenAI API to generate chatbot responses.


## Usage

1. Install the required Python packages: PyQt6 and openai.
2. Set your OpenAI API key in an environment variable named `OPEN_API`.
3. Run `main.py` to start the application.

## Note

This is a basic chatbot application and may need further improvements for production use. For example, error handling and edge cases might not be fully covered. Always review and test the code thoroughly before using it in a production environment.
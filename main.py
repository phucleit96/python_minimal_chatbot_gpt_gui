import threading  # Import the threading module for creating new threads

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication  # Import necessary PyQt6 classes
import sys  # Import the sys module for system-specific parameters and functions
from backend import Chatbot  # Import the Chatbot class from the backend module

class ChatbotWindow(QMainWindow):  # Define a new class ChatbotWindow that inherits from QMainWindow
    def __init__(self):  # Define the initializer method
        super().__init__()  # Call the initializer of the parent class QMainWindow
        self.setMinimumSize(700, 500)  # Set the minimum size of the window
        self.chatbot = Chatbot()  # Create a new instance of the Chatbot class

        self.chat_area = QTextEdit(self)  # Create a new QTextEdit widget for displaying the chat
        self.chat_area.setGeometry(10, 10, 480, 320)  # Set the geometry of the chat_area widget
        self.chat_area.setReadOnly(True)  # Make the chat_area widget read-only

        self.input_field = QLineEdit(self)  # Create a new QLineEdit widget for inputting text
        self.input_field.setGeometry(10, 340, 480, 40)  # Set the geometry of the input_field widget
        self.input_field.returnPressed.connect(self.send_message)  # Connect the returnPressed signal to the send_message method

        self.button = QPushButton("Send", self)  # Create a new QPushButton widget for sending messages
        self.button.setGeometry(500, 340, 100, 40)  # Set the geometry of the button widget
        self.button.clicked.connect(self.send_message)  # Connect the clicked signal to the send_message method

        self.show()  # Show the window

    def send_message(self):  # Define the send_message method
        user_input = self.input_field.text().strip()  # Get the text from the input_field widget and strip leading/trailing whitespace
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}")  # Append the user input to the chat_area widget
        self.input_field.clear()  # Clear the input_field widget

        # Create a new thread that will call the get_bot_response method with the user input as argument
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()  # Start the new thread

    def get_bot_response(self, user_input):  # Define the get_bot_response method
        response = self.chatbot.get_response(user_input)  # Get the response from the chatbot
        # Append the chatbot response to the chat_area widget
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Travis: {response}</p>")

app = QApplication(sys.argv)  # Create a new QApplication instance
main_window = ChatbotWindow()  # Create a new ChatbotWindow instance
sys.exit(app.exec())  # Start the event loop of the application
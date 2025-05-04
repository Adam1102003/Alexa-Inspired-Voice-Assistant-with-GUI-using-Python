import tkinter as tk              # Library for creating graphical user interfaces.
from tkinter import scrolledtext  # tkinter widget for adding a scrollable text area.
import speech_recognition as sr   # Library for recognizing speech using APIs.
import pyttsx3                    # Library for text-to-speech conversion.
import pywhatkit                  # Library for automating tasks like playing YouTube videos.
import datetime                   # Library for working with dates and times.
import wikipedia                  # Library for fetching information from Wikipedia.
import pyjokes                    # Library for generating random jokes. 

class Alexa:
    def __init__(self):
        # Initialize the speech recognizer
        self.listener = sr.Recognizer()
        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        # Get the available voices from the TTS engine
        self.voices = self.engine.getProperty('voices')
        # Set the voice to use (second voice in the list)
        self.engine.setProperty('voice', self.voices[1].id)
        # Setup the graphical user interface
        self.setup_gui()

    def setup_gui(self):
        # Create the main window
        self.root = tk.Tk()
        # Set the window title
        self.root.title("Alexa Interface")

        # Create a scrollable text area for displaying conversation
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
        # Add the text area to the window
        self.text_area.pack(padx=10, pady=10)

        # Create a button to start listening for commands
        self.listen_button = tk.Button(self.root, text="Listen", command=self.run_alexa, font=("Arial", 12))
        # Add the button to the window
        self.listen_button.pack(pady=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Start the Tkinter event loop
        self.root.mainloop()

    def talk(self, text):
        # Insert Alexa's response into the text area
        self.text_area.insert(tk.END, f"Alexa: {text}\n")
        # Use the TTS engine to say the text
        self.engine.say(text)
        # Wait for the speech to complete
        self.engine.runAndWait()

    def take_command(self):
        try:
            # Use the microphone as the audio source
            with sr.Microphone() as source:
                # Insert "Listening..." message into the text area
                self.text_area.insert(tk.END, "Listening...\n")
                self.text_area.see(tk.END)
                # Listen for the user's command
                voice = self.listener.listen(source)
                # Recognize the command using Google's speech recognition
                command = self.listener.recognize_google(voice)
                # Convert the command to lowercase
                command = command.lower()
                # Check if 'alexa' is in the command
                if 'alexa' in command:
                    # Remove 'alexa' from the command
                    command = command.replace('alexa', '')
                    # Insert the user's command into the text area
                    self.text_area.insert(tk.END, f"You: {command}\n")
                    self.text_area.see(tk.END)
                # Return the command
                return command
        except Exception as e:
            # Insert the error message into the text area
            self.text_area.insert(tk.END, f"Error: {str(e)}\n")
            # Return an empty string if there is an error
            return ""

    def run_alexa(self):
        # Take the command from the user
        command = self.take_command()
        if not command:
            return

        # Process the command and perform the corresponding action
        if 'play' in command:
            # Play a song on YouTube
            song = command.replace('play', '')
            self.talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            # Provide the current time
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.talk('Current time is ' + time)
        elif 'who the heck is' in command:
            # Provide a brief summary from Wikipedia
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            self.talk(info)
        elif "what's your name" in command:
            self.talk('I am Alexa')
        elif 'are you single' in command:
            self.talk('I am in a relationship with Wifi')
        elif 'are you in love' in command:
            self.talk('I am in love with you')        
        elif 'what is the capital city of japan' in command:
            self.talk('The capital city of Japan is Tokyo')
        elif 'what is the process by which plants make their food' in command:
            self.talk('The process by which plants make their food is called photosynthesis')
        elif 'who wrote the play romeo and juliet' in command:
            self.talk('Romeo and Juliet was written by William Shakespeare')
        elif 'what is the largest planet in our solar system' in command:
            self.talk('The largest planet in our solar system is Jupiter')
        elif 'what is the chemical symbol for gold' in command:
            self.talk('The chemical symbol for gold is Au')
        elif 'in which year did the titanic sink' in command:
            self.talk('The Titanic sank in the year 1912')
        elif 'what is the main ingredient in traditional japanese miso soup' in command:
            self.talk('The main ingredient in traditional Japanese miso soup is miso paste, which is made from fermented soybeans')
        elif 'what is the longest river in the world' in command:
            self.talk('The longest river in the world is the Nile River')
        elif 'who was the first person to walk on the moon' in command:
            self.talk('The first person to walk on the moon was Neil Armstrong')
        elif 'what is the formula for calculating the area of a circle' in command:
            self.talk('The formula for calculating the area of a circle is A = πr², where A is the area and r is the radius')
        elif 'what is the smallest unit of life' in command:
            self.talk('The smallest unit of life is the cell')
        elif 'who is known as the father of computers' in command:
            self.talk('Charles Babbage is known as the father of computers')
        elif 'what is the hardest natural substance on earth' in command:
            self.talk('The hardest natural substance on earth is diamond')
        elif 'what is the capital of france' in command:
            self.talk('The capital of France is Paris')
        elif 'which element has the atomic number 1' in command:
            self.talk('The element with the atomic number 1 is hydrogen')
        elif 'what is the name of the longest bone in the human body' in command:
            self.talk('The longest bone in the human body is the femur')
        elif 'what is the main language spoken in brazil' in command:
            self.talk('The main language spoken in Brazil is Portuguese')
        elif 'in which year did world war ii end' in command:
            self.talk('World War II ended in the year 1945')
        elif 'who painted the mona lisa' in command:
            self.talk('The Mona Lisa was painted by Leonardo da Vinci')
        elif 'what is the freezing point of water in celsius' in command:
            self.talk('The freezing point of water in Celsius is 0 degrees')
        elif 'what is the main gas found in the earths atmosphere' in command:
            self.talk('The main gas found in the earth\'s atmosphere is nitrogen')
        elif 'who wrote the novel 1984' in command:
            self.talk('The novel 1984 was written by George Orwell')
        elif 'what is the largest mammal in the world' in command:
            self.talk('The largest mammal in the world is the blue whale')
        elif 'what is the chemical formula for water' in command:
            self.talk('The chemical formula for water is H₂O')
        elif 'who was the first president of the united states' in command:
            self.talk('The first president of the United States was George Washington')
        elif 'what is the primary currency used in japan' in command:
            self.talk('The primary currency used in Japan is the yen')
        elif 'what is the name of the galaxy that contains our solar system' in command:
            self.talk('The name of the galaxy that contains our solar system is the Milky Way')
        elif 'which planet is known as the red planet' in command:
            self.talk('The planet known as the red planet is Mars')
        elif 'who discovered penicillin' in command:
            self.talk('Penicillin was discovered by Alexander Fleming')
        elif 'say my name' in command:
            self.talk('Tasneem Mohammed')
        elif 'my favourite movie' in command:
            self.talk('grave of the fireflies')
        elif 'my family' in command:
            self.talk('You are a happy family of five members')
        elif 'my work' in command:
            self.talk('flutter developer')
        elif 'How old are you' in command:
            self.talk('I am  23 years old')
        elif 'adam' in command:
            self.talk('the team is Mohammed Ashour, Ahmed Ayman, Mohammed Shaaban, Adam, Mohammed Hazem , Mariam , Mariam ,Youmna ,Abdallah Ayman')        
        elif 'what is the speed of light in a vacuum' in command:
            self.talk('The speed of light in a vacuum is approximately 299,792 kilometers per second')
        elif 'joke' in command:
            # Tell a joke
            self.talk(pyjokes.get_joke())
        else:
            # Handle unrecognized commands
            self.talk('Please say the command again.')

    def on_closing(self):
        # Destroy the main window and stop the TTS engine
        self.root.destroy()
        self.engine.stop()


if __name__ == "__main__":
    # Create an instance of the Alexa class and run the application
    alexa = Alexa()

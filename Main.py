import tkinter as tk
from speech_recognition import SpeechRecognition, Microphone
import random
import pywhatkit
import pyttsx3
import AppOpener as Apk
import webbrowser
import datetime
import pyautogui
import wikipedia

class ChatbotGUI:
	def __init__(self):
		self.window = (link unavailable)()
		self.window.title("ChatBot")
		self.window.configure(background="#3498db")
		
		# Text input field
		self.input_field = tk.Entry(self.window, font=("Arial", 12), bg="#f7f7f7")
		self.input_field.pack(padx=10, pady=10)
		
		# Send button
		self.send_button = tk.Button(self.window, text="Send", command=self.send_message, font=("Arial", 12), bg="#2ecc71", fg="#ffffff")
		self.send_button.pack(padx=10, pady=10)
		
		# Chat log text area
		self.chat_log = tk.Text(self.window, font=("Arial", 12), bg="#f7f7f7")
		self.chat_log.pack(padx=10, pady=10)
		
		# Speech recognition
		(link unavailable) = SpeechRecognition()
		self.mic = Microphone()
		
		# Start listening for voice commands
		(link unavailable).start_listening(self.mic, self.process_voice_command)
		
		# Add some personality to the chatbot
		self.responses = {
			"hello": ["Hello!", "Hi there!", "Hey!"],
			"how are you": ["I'm good, thanks!", "I'm doing well!", "I'm great!"],
			"what is your name": ["My name is ChatBot!", "I'm ChatBot!", "ChatBot is my name!"]
		}
		
	def send_message(self):
		message = self.input_field.get()
		self.chat_log.insert(tk.END, "You: " + message + "\n")
		self.input_field.delete(0, tk.END)
		
		# Respond to user input
		if message.lower() in self.responses:
			response = random.choice(self.responses[message.lower()])
			self.chat_log.insert(tk.END, "ChatBot: " + response + "\n")
		
	def process_voice_command(self, voice_command):
		self.chat_log.insert(tk.END, "You (voice): " + voice_command + "\n")
		
		# Respond to voice commands
		if voice_command.lower() in self.responses:
			response = random.choice(self.responses[voice_command.lower()])
			self.chat_log.insert(tk.END, "ChatBot: " + response + "\n")
		
		# Execute desktop assistant commands
		self.execute_command(voice_command)
		
	def execute_command(self, command):
		# Implement desktop assistant commands here
		if "date" in command.lower():
			today = datetime.date.today()
			self.chat_log.insert(tk.END, "ChatBot: Today's date is " + str(today) + "\n")
		elif "time" in command.lower():
			time = datetime.datetime.now()
			current_time = time.strftime("%H:%M:%S")
			self.chat_log.insert(tk.END, "ChatBot: The current time is " + current_time + "\n")
		elif "open" in command.lower():
			software = command.split("open")[1].strip()
			for soft in softs:
				if soft[0] == software:
					Apk.open(soft[1])
					self.chat_log.insert(tk.END, "ChatBot: Opening " + software + "\n")
					break
		elif "search" in command.lower():
			query = command.split("search")[1].strip()
			url = f"(link unavailable)"
			webbrowser.open(url)
			self.chat_log.insert(tk.END, "ChatBot: Searching for " + query + " on Google\n")
		elif "explain" in command.lower():
			query = command.split("explain")[1].strip()
			try:
				results = wikipedia.search(query)
				page = wikipedia.page(results[0])
				summary = wikipedia.summary(results[0], sentences=5)
				self.chat_log.insert(tk.END, "ChatBot: " + summary + "\n")
			except wikipedia.exceptions.DisambiguationError as e:
				self.chat_log.insert(tk.END, "ChatBot: Can you please be more specific?\n")
			except wikipedia.exceptions.PageError as e:
				self.chat_log.insert(tk.END, "ChatBot: Sorry, I couldn't find any information on that.\n")
		elif "play" in command.lower():
			song = command.split("play")[1].strip()
			pywhatkit.playonyt(song)
			self.chat_log.insert(tk.END, "ChatBot: Playing " + song + " on

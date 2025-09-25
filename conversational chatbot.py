# Develop a conversational Chatbot.
import nltk
from nltk.chat import eliza
from nltk.chat import rude
from nltk.chat import iesha
from nltk.chat import zen
def rule_based_chatbot():
print("Hello! I'm a simple rule-based chatbot. Choose a personality:")
print("1. ELIZA (psychotherapist-like)")
print("2. Rude (blunt and often unhelpful)")
print("3. IESHA (teenager-like)")
print("4. Zen (peaceful and philosophical)")
print("5. Exit") # Added an option to exit the personality selection
while True:
choice = input("Enter your choice (1-5): ")
if choice == '1':
print("\nType 'quit' to exit the ELIZA chat.")
eliza.eliza_chat()
break # Exit the personality selection loop after the chat
elif choice == '2':
print("\nType 'quit' to exit the Rude chat.")
rude.rude_chat()
break # Exit the personality selection loop after the chat
elif choice == '3':
print("\nType 'quit' to exit the IESHA chat.")
iesha.iesha_chat()


break # Exit the personality selection loop after the chat
elif choice == '4':
print("\nType 'quit' to exit the Zen chat.")
zen.zen_chat()
break # Exit the personality selection loop after the chat
elif choice == '5':
print("Exiting chatbot.")
break # Exit the personality selection loop
else:
print("Invalid choice. Please enter a number between 1 and
5.")
if __name__ == "__main__":
try:
nltk.data.find('corpora/wordnet')
except LookupError:
print("Downloading necessary NLTK data (wordnet)...")
nltk.download('wordnet')
try:
nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
print("Downloading necessary NLTK data
(averaged_perceptron_tagger)...")
nltk.download('averaged_perceptron_tagger')
rule_based_chatbot()

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert the input to lowercase for easier matching

    # Greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "good morning" in user_input:
        return "Good morning! How can I assist you today?"
    elif "good afternoon" in user_input:
        return "Good afternoon! How can I help you today?"
    elif "good evening" in user_input:
        return "Good evening! How can I assist you today?"
    
    # Small Talk
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what's up" in user_input:
        return "Not much! I'm here to help you. What can I do for you?"
    elif "how's it going" in user_input:
        return "It's going well! How can I assist you today?"

    # Personal Questions
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a chatbot created to assist you. You can call me ChatBot!"
    elif "your age" in user_input:
        return "I don't have an age like humans do, but I was created recently."
    elif "creator" in user_input or "created" in user_input:
        return "I was created by a Software Developer Called Infant Maria Jose."

    # Assistance
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "support" in user_input:
        return "I'm here to support you. What do you need assistance with?"
    elif "assist" in user_input:
        return "Of course! How can I assist you today?"

    # Weather
    elif "weather" in user_input:
        return "I'm not equipped to provide real-time weather updates, However you can visit https://weather.com."
    elif "temperature" in user_input:
        return "I don't have the capability to provide real-time temperature updates. However you can visit https://weather.com"

    # Time and Date
    elif "time" in user_input:
        return "I'm not equipped with a clock, but you can check your device for the current time."
    elif "date" in user_input:
        return "Please check your device for the current date."

    # Directions
    elif "directions" in user_input:
        return "I can't provide real-time directions, However you can visit https://www.google.com/maps"
    elif "navigate" in user_input:
        return "I can't provide navigations, However you can visit https://www.google.com/maps"

    # Food and Drink
    elif "favorite food" in user_input:
        return "I don't eat, but I hear pizza is a popular choice!"
    elif "favorite drink" in user_input:
        return "I don't drink, but many people enjoy coffee."

    # Technology
    elif "favorite technology" in user_input:
        return "I find artificial intelligence fascinating!"
    elif "tech news" in user_input:
        return "You can visit https://indianexpress.com/section/technology/ for latest tech news."

    # Hobbies and Interests
    elif "hobbies" in user_input:
        return "I don't have hobbies, but I can tell you about various hobbies people enjoy."
    elif "interests" in user_input:
        return "I'm interested in helping you! What are your interests?"

    # Jokes and Fun
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "make me laugh" in user_input:
        return "What do you call fake spaghetti? An impasta!"

    # Health and Wellness
    elif "stay healthy" in user_input:
        return "Eating well, exercising, and getting enough sleep are key to staying healthy."
    elif "mental health" in user_input:
        return "It's important to take care of your mental health. Consider speaking to a professional if you need help."

    # Education
    elif "study tips" in user_input:
        return "Regular study sessions, staying organized, and taking breaks can help improve your study habits."
    elif "best way to learn" in user_input:
        return "Everyone learns differently, but active engagement and practice are often very effective."

    # Travel
    elif "travel tips" in user_input:
        return "Pack light, stay safe, and always have a backup plan."
    elif "best places to visit" in user_input:
        return "There are many wonderful places to visit! It depends on your interests."

    # Music and Movies
    elif "favorite music" in user_input:
        return "I don't listen to music, but many people love pop and classical genres."
    elif "favorite movie" in user_input:
        return "I don't watch movies, but 'The Shawshank Redemption' is often highly recommended."

    # Miscellaneous
    elif "fun fact" in user_input:
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible."
    elif "random fact" in user_input:
        return "Octopuses have three hearts and blue blood!"

    # Ending the Conversation
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Default Response
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Simulate a conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)

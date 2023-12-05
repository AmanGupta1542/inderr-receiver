from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output11.mp3'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the audio file
    tts.save(filename)

    # Play the audio file (requires a system command)
    os.system(f"mpg123 {filename}")  # On Windows
    # os.system(f"xdg-open {filename}")  # On Linux

if __name__ == "__main__":
    # Input text
    input_text = "Hello, how are you today?"

    # Convert text to speech and save as an audio file
    text_to_speech(input_text)

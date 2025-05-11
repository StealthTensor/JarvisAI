import speech_recognition as sr
import pyttsx3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    """
    Convert text to speech and log the action.
    """
    try:
        logger.info(f"Speaking: {text}")
        print("Jarvis:", text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"Error in speech synthesis: {str(e)}")
        print("Jarvis: Error in speaking. Please try again.")

def listen():
    """
    Listen for user input via microphone and convert speech to text.
    Returns the recognized text or None if recognition fails.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        logger.info("Listening for user input...")
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            logger.warning("Listening timed out, no speech detected.")
            speak("I didn't hear anything. Please speak again.")
            return None

    try:
        query = recognizer.recognize_google(audio)
        logger.info(f"Recognized: {query}")
        print("You:", query)
        return query
    except sr.UnknownValueError:
        logger.warning("Could not understand the audio.")
        speak("Sorry, I didn't catch that. Could you repeat?")
        return None
    except sr.RequestError as e:
        logger.error(f"Speech recognition service error: {str(e)}")
        speak("The speech service is down. Please try again later.")
        return None
    except Exception as e:
        logger.error(f"Unexpected error in speech recognition: {str(e)}")
        speak("An unexpected error occurred. Please try again.")
        return None
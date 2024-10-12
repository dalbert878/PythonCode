import threading
import queue
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import requests
from kivy.lang import Builder
import pyttsx3
import os

class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Initialize TTS engine and queue
        self.engine = pyttsx3.init()
        self.speech_queue = queue.Queue()
        self.stop_event = threading.Event()

        # Start background thread for speech processing
        self.speech_thread = threading.Thread(target=self._process_speech_queue, daemon=True)
        self.speech_thread.start()

        # Initialize quote placeholders
        self.current_quote = ""
        self.current_author = ""

        # Generate initial quote
        self.generate_quote()

    def generate_quote(self, *args):
        """Fetch and display a new quote from the API."""
        url = "https://zenquotes.io/api/random"
        self.ids.insquote_image.source = "header.jpg"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()[0]
            self.current_quote, self.current_author = data['q'], data['a']

            # Update the UI with new quote
            self.ids.insquote_label.text = self.current_quote
            self.ids.insquote_author.text = f"- {self.current_author}"

            # Speak the new quote
            self.speak_quote(self.current_quote)
        except requests.RequestException as e:
            print(f"Error fetching quote: {e}")
            self.ids.insquote_label.text = "Error fetching quote"
            self.ids.insquote_author.text = ""

    def speak_quote(self, quote):
        """Add a quote to the speech queue."""
        if not self.stop_event.is_set():
            self.speech_queue.put(quote)

    def speak_quote_again(self, *args):
        """Repeat the current quote with the author."""
        if self.current_quote and self.current_author and not self.stop_event.is_set():
            speech_text = f"{self.current_author} once said, {self.current_quote}"
            self.speech_queue.put(speech_text)

    def _process_speech_queue(self):
        """Process queued speech tasks in a background thread."""
        while not self.stop_event.is_set():
            try:
                speech_text = self.speech_queue.get(timeout=1)
                self.engine.say(speech_text)
                self.engine.runAndWait()
                self.speech_queue.task_done()
            except queue.Empty:
                continue

    def stop_speech_processing(self):
        """Stop the speech thread and safely exit."""
        self.stop_event.set()
        self.speech_queue.put(None)  # Stop signal for the queue
        self.speech_thread.join()
        self.engine.stop()

class InsQuote(App):
    def build(self):
        return MyRoot()

    def on_stop(self):
        """Stop the app gracefully and release resources."""
        self.root.stop_speech_processing()
        os._exit(0)  # Force exit to prevent hanging

if __name__ == "__main__":
    InsQuote().run()

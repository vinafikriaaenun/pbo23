import tkinter as tk
from gtts import gTTS
from playsound import playsound

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech App")

        # Create widgets
        self.label = tk.Label(root, text="Enter text:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=10)

        self.language_label = tk.Label(root, text="Select language:")
        self.language_label.pack()

        self.language_var = tk.StringVar()
        self.language_var.set("en")  # Default language is English

        self.language_menu = tk.OptionMenu(root, self.language_var, "en", "id", "de", "ko", "ar")
        self.language_menu.pack(pady=10)

        self.speak_button = tk.Button(root, text="Speak", command=self.speak_text)
        self.speak_button.pack(pady=10)

    def speak_text(self):
        text_to_speak = self.text_entry.get()
        language = self.language_var.get()

        if text_to_speak:
            myobj = gTTS(text=text_to_speak, lang=language, slow=False)
            myobj.save("output.mp3")
            playsound("output.mp3", True)
        else:
            print("Please enter text to speak.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

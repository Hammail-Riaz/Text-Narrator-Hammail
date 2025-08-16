import tkinter as tk
import pyttsx3
import threading

is_speaking = False
speech_thread = None
engine = None   # current engine reference

def speak_text(text):
    global is_speaking, engine
    engine = pyttsx3.init()   # new engine for this speech
    engine.say(text)
    try:
        engine.runAndWait()
    except:
        pass
    # if we finished normally (not stopped)
    is_speaking = False
    engine = None
    speak_button.config(text="Speak")

def toggle_speak():
    global is_speaking, speech_thread, engine
    text = text_area.get("1.0", tk.END).strip()

    if not is_speaking and text:   # start speaking
        is_speaking = True
        speak_button.config(text="Stop")
        speech_thread = threading.Thread(target=speak_text, args=(text,), daemon=True)
        speech_thread.start()
    else:   # stop speaking
        if engine is not None:
            try:
                engine.stop()   # force stop
            except:
                pass
        is_speaking = False
        engine = None
        speak_button.config(text="Speak")

# ------------------ UI ------------------
root = tk.Tk()
root.title("Text Narrator - Hammail")
root.geometry("800x600")
root.iconbitmap("icon.ico")  # Set your icon file here

text_area = tk.Text(root, font=("Arial", 14))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

speak_button = tk.Button(root, text="Speak", command=toggle_speak, width=12)
speak_button.pack(pady=10)

root.mainloop()

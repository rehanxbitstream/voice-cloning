import os
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

import pygame
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs


# ---------------- CONFIGURATION ----------------

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise ValueError("ELEVENLABS_API_KEY not found in .env")

client = ElevenLabs(api_key=api_key)

os.makedirs("output", exist_ok=True)

OUTPUT_FILE = "output/generated_voice.mp3"


# Available voices
VOICES = {
    "Daniel - Steady Broadcaster": "onwK4e9ZLuTAKqWW03F9",
    "Alice - Clear, Engaging Educator": "Xb7hH8MSUJpSbSDYk0k2",
    "George - Warm Storyteller": "JBFqnCBsd6RMkjVDRZzb",
    "Eric - Smooth, Trustworthy": "cjVigY5qzO86Huf0OWal",
    "Matilda - Professional": "XrExE9yKIg1WjnnlVkGX",
}


# Initialize pygame audio
pygame.mixer.init()


# ---------------- FUNCTIONS ----------------

def generate_speech():

    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Input Required",
            "Please enter some text."
        )
        return

    selected_voice = voice_dropdown.get()
    voice_id = VOICES[selected_voice]

    try:
        # Stop currently playing audio
        pygame.mixer.music.stop()

        # Unload current audio file if supported
        try:
            pygame.mixer.music.unload()
        except Exception:
            pass

        status_label.config(text="Generating speech...")
        root.update()

        audio = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )

        os.makedirs("output", exist_ok=True)

        with open(OUTPUT_FILE, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        status_label.config(
            text="Speech generated successfully!"
        )

        messagebox.showinfo(
            "Success",
            "Speech generated successfully!"
        )

    except Exception as e:

        status_label.config(
            text="Generation failed!"
        )

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n\n{e}"
        )
def play_audio():

    if not os.path.exists(OUTPUT_FILE):

        messagebox.showwarning(
            "No Audio",
            "Please generate speech first."
        )

        return

    try:

        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()

        status_label.config(
            text="Playing audio..."
        )

    except Exception as e:

        messagebox.showerror(
            "Playback Error",
            str(e)
        )


def stop_audio():

    pygame.mixer.music.stop()

    status_label.config(
        text="Audio stopped."
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("AI Voice Generator")

root.geometry("750x600")

root.resizable(False, False)


# Title

title_label = tk.Label(
    root,
    text="AI Voice Generator",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


# Description

description_label = tk.Label(
    root,
    text="Generate speech using ElevenLabs AI",
    font=("Arial", 11)
)

description_label.pack()


# Text label

text_label = tk.Label(
    root,
    text="Enter your text:",
    font=("Arial", 12, "bold")
)

text_label.pack(
    anchor="w",
    padx=40,
    pady=(20, 5)
)


# Text box

text_box = scrolledtext.ScrolledText(
    root,
    width=78,
    height=10,
    font=("Arial", 11),
    wrap=tk.WORD
)

text_box.pack(
    padx=40
)


# Voice label

voice_label = tk.Label(
    root,
    text="Select Voice:",
    font=("Arial", 12, "bold")
)

voice_label.pack(
    anchor="w",
    padx=40,
    pady=(15, 5)
)


# Voice dropdown

voice_dropdown = ttk.Combobox(
    root,
    values=list(VOICES.keys()),
    state="readonly",
    width=55
)

voice_dropdown.pack()

voice_dropdown.current(0)


# Generate button

generate_button = tk.Button(
    root,
    text="Generate Speech",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8,
    command=generate_speech
)

generate_button.pack(pady=20)


# Audio controls frame

controls_frame = tk.Frame(root)

controls_frame.pack()


# Play button

play_button = tk.Button(
    controls_frame,
    text="▶ Play Audio",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8,
    command=play_audio
)

play_button.grid(
    row=0,
    column=0,
    padx=10
)


# Stop button

stop_button = tk.Button(
    controls_frame,
    text="⏹ Stop Audio",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8,
    command=stop_audio
)

stop_button.grid(
    row=0,
    column=1,
    padx=10
)


# Status

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10)
)

status_label.pack(pady=20)


# Start application

root.mainloop()
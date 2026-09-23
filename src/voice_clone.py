import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

VOICE_ID = "onwK4e9ZLuTAKqWW03F9"

text = """
Hello, my name is Rehan Khan.
I am currently pursuing Integrated MCA from IIPS.
This is my Multimedia Systems project.
In this project, I am demonstrating AI based text to speech
using Python and ElevenLabs.
"""

print("Generating speech...")

audio = client.text_to_speech.convert(
    text=text,
    voice_id=VOICE_ID,
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128"
)

os.makedirs("output", exist_ok=True)

output_file = "output/generated_voice.mp3"

with open(output_file, "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("Speech generated successfully!")
print(f"Audio saved at: {output_file}")
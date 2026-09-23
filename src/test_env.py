import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

response = client.voices.get_all()

print("\nAvailable Voices:\n")

for voice in response.voices:
    print(f"Name: {voice.name}")
    print(f"Voice ID: {voice.voice_id}")
    print("-" * 40)
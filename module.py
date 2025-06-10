from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Konfigurasi API key dari lingkungan atau langsung (ganti sesuai kebutuhan)
genai.configure(api_key=gemini_key)

# Ekstrak ID video dari berbagai format URL YouTube
def extract_video_id(url):
    parsed_url = urlparse(url)

    if "youtube" in parsed_url.netloc:
        query = parse_qs(parsed_url.query)
        return query.get("v", [None])[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.strip("/")
    return None

# Ambil transkrip video YouTube
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['id', 'en'])
    return " ".join([item['text'] for item in transcript])

# Ringkasan menggunakan Gemini
def summarize_text(text):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(f"Ringkas isi video berikut dalam bahasa Indonesia:\n\n{text}")
    return response.text

import pyaudio
import deepgram
import os
import google.generativeai as genai
from deepgram import DeepgramClient,PrerecordedOptions,FileSource,SpeakOptions
import time
API_KEY='AIzaSyAexHdX9nrYFMBPTW-bYoCdXM7sclJsofo'
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-pro")
stt =DeepgramClient('4a5edcdd5405c0ed4ce6a54071404a827142ce9c')
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text
def get_audio(text):
    print(text)
    response=get_gemini_response(text)
    llm_response_time = time.time()
    print(response)
    SPEAK_OPTIONS = {"text": response}
    directory = r"E:\punt patners\New folder\pro\app1\templates\static"
    filename = os.path.join(directory, "output.wav")

    # Create the directory if it does not exist
    os.makedirs(directory, exist_ok=True)
    try:
        options = SpeakOptions(
        model="aura-asteria-en",
        encoding="linear16",
        container="wav"
        )
        res=stt.speak.v('1').save(filename, SPEAK_OPTIONS, options)
    except Exception as e:
        print(e)
        response = None
    return response
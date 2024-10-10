import streamlit as st
from gtts import gTTS
import os
import tempfile
import base64
from pydub import AudioSegment
import io

def adjust_pitch(audio_segment, octaves):
    new_sample_rate = int(audio_segment.frame_rate * (2.0 ** octaves))
    return audio_segment._spawn(audio_segment.raw_data, overrides={'frame_rate': new_sample_rate})

def text_to_speech(text, language, voice_type, speed):
    tts = gTTS(text=text, lang=language, slow=speed)
    
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    
    sound = AudioSegment.from_mp3(audio_bytes)
    
    # Adjust pitch based on voice type
    if voice_type == 'Male':
        pitched_sound = adjust_pitch(sound, -0.2)  # Lower pitch for male voice
    elif voice_type == 'Female':
        pitched_sound = adjust_pitch(sound, 0.2)   # Higher pitch for female voice
    else:
        pitched_sound = sound  # No pitch adjustment
    
    output_bytes = io.BytesIO()
    pitched_sound.export(output_bytes, format="mp3")
    output_bytes.seek(0)
    
    return output_bytes

def get_binary_file_downloader_html(bin_file, file_label='File'):
    bin_str = base64.b64encode(bin_file.getvalue()).decode()
    href = f'<a href="data:audio/mp3;base64,{bin_str}" download="audio.mp3">Download {file_label}</a>'
    return href

def main():
    st.title("Multilingual Text-to-Speech Converter")

    # Text input
    text = st.text_area("Enter the text you want to convert to speech:")

    # Language selection
    languages = {
        'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
        'Italian': 'it', 'Portuguese': 'pt', 'Hindi': 'hi', 'Japanese': 'ja',
        'Korean': 'ko', 'Chinese': 'zh-CN'
    }
    selected_language = st.selectbox("Select Language", list(languages.keys()))

    # Voice type selection
    voice_types = ['Default', 'Male', 'Female']
    selected_voice = st.selectbox("Select Voice", voice_types)

    # Speed selection
    speed = st.checkbox("Slow mode")

    if st.button("Convert to Speech"):
        if text:
            audio_bytes = text_to_speech(text, languages[selected_language], selected_voice, speed)
            
            # Play the audio
            st.audio(audio_bytes, format='audio/mp3')
            
            # Offer download option
            st.markdown(get_binary_file_downloader_html(audio_bytes, 'Audio'), unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()
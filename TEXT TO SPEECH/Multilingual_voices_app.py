import streamlit as st
from gtts import gTTS
import os
import tempfile

def text_to_speech(text, language, speed, pitch):
    tts = gTTS(text=text, lang=language, slow=speed)
    
    # Save the audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

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

    # Speed selection
    speed = st.checkbox("Slow mode")

    # Pitch selection (note: gTTS doesn't directly support pitch adjustment)
    pitch = st.slider("Pitch", 0.5, 2.0, 1.0, 0.1)
    st.write("Note: Pitch adjustment is not supported by gTTS and won't affect the output.")

    if st.button("Convert to Speech"):
        if text:
            audio_file = text_to_speech(text, languages[selected_language], speed, pitch)
            
            # Play the audio
            st.audio(audio_file)
            
            # Offer download option
            with open(audio_file, "rb") as file:
                btn = st.download_button(
                    label="Download Audio",
                    data=file,
                    file_name="tts_output.mp3",
                    mime="audio/mp3"
                )
            
            # Clean up the temporary file
            os.unlink(audio_file)
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()
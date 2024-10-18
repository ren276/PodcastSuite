import streamlit as st
import os
import sys
from PIL import Image
import io

# Set the path to your Fooocus installation and add it to sys.path
FOOOCUS_PATH = r"C:\users\mahfooz alam\Desktop\MINOR PROJECT\Human avatar generator\Fooocus-main"
sys.path.append(FOOOCUS_PATH)

# Import Fooocus modules
from fooocus_api import generate_image
from fooocus_version import version

def generate_avatar(prompt, negative_prompt, style, steps):
    output_path = os.path.join(FOOOCUS_PATH, "outputs")
    os.makedirs(output_path, exist_ok=True)

    params = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "style_selections": [style],
        "performance_selection": "Speed",
        "aspect_ratios_selection": "1152×896",
        "image_number": 1,
        "image_seed": -1,
        "sharpness": 2.0,
        "guidance_scale": 7.0,
        "base_model_name": "juggernautXL_v8Rundiffusion.safetensors",
        "refiner_model_name": "None",
        "refiner_switch": 0.8,
        "loras": [
            [
                "sd_xl_offset_example-lora_1.0.safetensors",
                0.1
            ]
        ],
        "advanced_params": {
            "adaptive_cfg": 7.0,
            "adm_scaler_positive": 1.5,
            "adm_scaler_negative": 0.8,
            "adm_scaler_end": 0.3,
            "refiner_strength": 0.5,
            "positive_adm_scale": 1.5,
            "negative_adm_scale": 0.8,
            "adm_scaler_end": 0.3
        },
        "steps": steps,
        "output_path": output_path
    }

    try:
        images = generate_image(params)
        if images:
            return Image.open(io.BytesIO(images[0]))
        else:
            st.error("No image was generated.")
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
    
    return None

def main():
    st.title("Stable Diffusion Avatar Generator")
    st.write(f"Using Fooocus version: {version}")

    prompt = st.text_input("Enter your avatar description:", "A futuristic cyborg with glowing blue eyes")
    negative_prompt = st.text_input("Enter negative prompt:", "ugly, deformed, low quality")
    
    style = st.selectbox("Choose a style:", ["Fooocus V2", "Fooocus Enhance", "Fooocus Sharp"])
    steps = st.slider("Number of steps:", min_value=20, max_value=100, value=30)

    if st.button("Generate Avatar"):
        with st.spinner("Generating your avatar..."):
            image = generate_avatar(prompt, negative_prompt, style, steps)
        
        if image:
            st.image(image, caption="Generated Avatar", use_column_width=True)
            
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Download Avatar",
                data=byte_im,
                file_name="generated_avatar.png",
                mime="image/png"
            )
        else:
            st.error("Failed to generate the avatar. Please check the error messages above and try again.")

if __name__ == "__main__":
    main()
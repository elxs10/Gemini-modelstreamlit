import google.generativeai as genai
import streamlit as st
import json

# Function to initialize session state
def initialize_session_state():
    return st.session_state.setdefault('api_key', None)

# Main Streamlit app
def text_page():
    st.title("scnmone")

    # Initialize session state
    initialize_session_state()

    # Configure API key
    api_key = "AIzaSyAhmX3uyVgyRc36DXy_mVmr3jhE-UbyxMk"
    # Check if the API key is provided
    if not api_key:
        st.sidebar.error("AIzaSyAhmX3uyVgyRc36DXy_mVmr3jhE-UbyxMk")
        st.stop()
    else:
        # Store the API key in session state
        st.session_state.api_key = api_key

    genai.configure(api_key=api_key)

    # Create a sidebar expander for customization options
    with st.sidebar:
        with st.expander("Customization Options"):
            # Set up the model configuration options
            temperature = st.slider("Temperature", 0.0, 1.0, 0.9, 0.1)
            top_p = st.number_input("Top P", 0.0, 1.0, 1.0, 0.1)
            top_k = st.number_input("Top K", 1, 100, 1)
            max_output_tokens = st.number_input("Max Output Tokens", 1, 10000, 2048)

    # Set up the model
    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
    }

    safety_settings = "{}"
    safety_settings = json.loads(safety_settings)
        
    prompt = st.text_input("Enter your Query:")
    # Check if the query is provided
    if not prompt:
        st.error("Please enter your query.")
        st.stop()

    gemini = genai.GenerativeModel(model_name="gemini-pro", safety_settings=safety_settings)

    prompt_parts = [prompt]
    
    try:
        response = gemini.generate_content(prompt_parts)
        st.subheader("Gemini:")
        if response.text:
            st.write(response.text)
        else:
            st.write("No output from Gemini.")
    except Exception as e:
        st.write(f"An error occurred: {str(e)}")

# Run the Streamlit app
if __name__ == "__main__":
    text_page()

import streamlit as st
from brain import Summarizer #import class Summarizer from brain.py
from io import StringIO

#Page Config
st.set_page_config(page_title="TL;DR Generator", page_icon="📚")

#Cache the model
#Streamlit runs load_model whenever the model changes, uses cache to make it faster
@st.cache_resource
def load_model():
    return Summarizer()

#Sidebar(max length summary)
st.sidebar.header("Settings")
st.sidebar.write("Change the summary length:")
#slider(title, min, max, starting position)
max_len = st.sidebar.slider("Max Length", 50, 300, 150)
min_len = st.sidebar.slider("Min Length", 10, 100, 40)

#Main Page
st.title("TL;DR Generator")
st.markdown("Summarize long articles or documents using **PyTorch**.")

#Initialize model, as soon as the model is loaded, it removes spinner
with st.spinner("Waking up the AI Brain... (First run takes 30s)"):
    bot = load_model()

#Input tabs(either paste or upload file)
tab1, tab2 = st.tabs(["✍️ Paste Text", "📂 Upload File"])
user_input = ""

#Page with paste
with tab1:
    text_paste = st.text_area("Paste text here:", height=300)
    if text_paste:
        user_input = text_paste

#Page with upload
with tab2:
    uploaded_file = st.file_uploader("Choose a .txt file", type="txt")
    if uploaded_file is not None:
        #Convert file to string
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        user_input = stringio.read()
        st.success(f"Loaded: {uploaded_file.name}")

st.divider()

#Clicking generate
if st.button("Generate Summary", type="primary"):
    if user_input:
        with st.spinner('Reading and summarizing...'):
            try:
                #Pass user input and sidebar settings to brain
                result = bot.summarize(user_input, max_length=max_len, min_length=min_len)
                
                st.success("Summary Ready!")
                st.markdown(f"### Result:\n{result}")
                
                #Download Button
                st.download_button(
                    label="Download Summary",
                    data=result,
                    file_name="summary.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide some text to summarize.")
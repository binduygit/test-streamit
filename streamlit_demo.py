import streamlit as st
import pinecone
import os
import openai
from openai import OpenAI

os.environ["OPENAI_API_KEY"]="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"
client=OpenAI()

pinecone.init(
	api_key='2646175b-b6a8-4af5-9b99-8199edf4906a',
	environment='us-west1-gcp-free'
)
index = pinecone.Index('movie-recommendation')

#AI Functions

def generate_blog(topic, additional_text):
    prompt = f"""
    You are a copy writer with years of experience writing impactful blog that converge and help elevate brands.
    Your task is to write a blog on any topic system provides you with. Make sure to write in a format that works for Medium.
    Each blog should be separated into segments that have titles and subtitles. Each paragraph should be three sentences long.

    Topic: {topic}
    Additiona pointers: {additional_text}
    """

    response = client.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 700,
        temperature = 0.9
    )
    return response

def generate_images(prompt, number_of_images):
    response = client.images.generate(
        prompt = prompt,
        n=number_of_images,
        size="512x512"
    )

    return response

st.set_page_config(layout="wide")
st.title("Open API webapp")
st.sidebar.title("AI Apps")

ai_app = st.sidebar.radio("Choose an AI APP", ("Blog Generator", "Image Generator", "Movie Recommendation"))

if ai_app == "Blog Generator":
    st.header("Blog Generator")
    st.write("Input a topic to generate a blog about it using OpenAI API")
    topic = st.text_area("Topic", height=30)
    additional_text = st.text_area("Additional Text", height=30)
    if st.button("Generate Blog"):
        with st.spinner("Generating ..."):
            
            response = generate_blog(topic, additional_text)
            st.text_area("Generated Blog", value = response.choices[0].text, height=700)

elif ai_app == "Image Generator":
    st.header("Image Generator")
    st.write("Input a topic to generate an image about it using OpenAI API")
    prompt = st.text_area("Topic", height=30)
    number_of_images = st.slider("Number of Images",1,5,1)
    if st.button("Generate Image") and prompt != "":
        with st.spinner("Generating ..."):
            response = generate_images(prompt, number_of_images)

            for output in response.data:
                st.image(output.url)

elif ai_app ==  "Movie Recommendation":
    st.header("Movie Recommendation")
    st.write("Input a topic to recommend a movie using OpenAI API")
    movie_desc = st.text_area("Topic", height=30)
    if st.button("Generate Movie Recommendation") and movie_desc !="":
        with st.spinner("Recommending ..."):
            
            vector = client.embeddings.create(
                model = "text-embedding-ada-002",
                input = movie_desc
            )
            result_vector = vector.data[0].embedding
            result = index.query(
                result_vector,
                top_k=10,
                include_metadata=True
            )
            for movie in result.matches:
                st.write(movie['metadata']['title'])
else:
    pass

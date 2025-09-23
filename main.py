from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

# Ask for API key in UI (for local testing)
api_key = st.text_input("Enter your Google API Key", type="password")

# Use either the environment variable or user input
final_api_key = os.getenv("GOOGLE_API_KEY", api_key)

if not final_api_key:
    st.error("❌ No API key found. Please enter it or set GOOGLE_API_KEY as an environment variable.")
else:
    os.environ["GOOGLE_API_KEY"] = final_api_key
    st.success("✅ API key configured successfully!")

    llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)
    
    prompt_1=ChatPromptTemplate.from_messages([
        ("system", """You are a helpful assistant that Summarize the conversation in 2 to 3 sentences.
            "Summarize the key points of this conversation in 2–3 sentences, ensuring the recap is concise, clear, and suitable for quick reference or reuse as a prompt."""),
        ("user", "{transcript}")
    ])
    
    prompt_2=ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that Analyze the given summary and extract the customer’s sentiment as one of the following categories: Positive, Neutral, or Negative. Provide only the sentiment label without additional explanation. "),
        ("user", "{summarie}")
    ])
    
    
    st.title("Transcript Summarization")
    input_text=st.text_input("Enter your transcript here", key="input")
    if st.button("Submit"):
        final_promt_1=prompt_1.invoke({"transcript": input_text})
        st.write("Transcript: ", input_text)
        summary=llm.invoke(final_promt_1)
        st.write("Summary: ", summary.content)
        final_promt_2=prompt_2.invoke({"summarie": summary.content})
        sentiment=llm.invoke(final_promt_2)
        st.write("Sentiment: ", sentiment.content)
        data={"Transcript": [input_text], "Summary": [summary.content], "Sentiment": [sentiment.content]}
        df=pd.DataFrame(data)
        csv=df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name="Transcript_Summarization.csv",
            mime="text/csv",
            key='download_csv_button'
    
        )



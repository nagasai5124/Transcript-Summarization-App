# Transcript Summarization App

A Streamlit-based web application that automatically summarizes conversation transcripts and analyzes their sentiment using Google's Gemini AI model.

## Features

- **Transcript Summarization**: Converts lengthy conversation transcripts into concise 2-3 sentence summaries
- **Sentiment Analysis**: Analyzes the summarized content to determine sentiment (Positive, Neutral, or Negative)
- **CSV Export**: Download results as a CSV file for further analysis
- **User-Friendly Interface**: Simple Streamlit web interface for easy interaction

## Prerequisites

- Python 3.7 or higher
- Google AI API key (for Gemini model access)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/transcript-summarization-app.git
cd transcript-summarization-app
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Google AI API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter your conversation transcript in the text input field

4. Click "Submit" to generate:
   - A concise summary of the transcript
   - Sentiment analysis of the conversation

5. Download the results as a CSV file using the download button

## Dependencies

- `langchain`: Framework for building applications with LLMs
- `langchain-google-genai`: Google Generative AI integration for LangChain
- `streamlit`: Web app framework for machine learning and data science
- `pandas`: Data manipulation and analysis library
- `python-dotenv`: Load environment variables from .env file
- `langgraph`: Additional LangChain graph functionality

## Project Structure

```
transcript-summarization-app/
│
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
└── README.md              # Project documentation
```

## How It Works

1. **Input Processing**: User provides a conversation transcript through the Streamlit interface
2. **Summarization**: The application uses Google's Gemini 2.5 Pro model to generate a concise summary
3. **Sentiment Analysis**: The summary is analyzed to determine overall sentiment
4. **Output Generation**: Results are displayed and made available for CSV download

## Configuration

The application uses the following configuration:
- **Model**: Google Gemini 2.5 Pro
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Summary Length**: 2-3 sentences
- **Sentiment Categories**: Positive, Neutral, Negative

## API Requirements

You'll need a Google AI API key to use this application. You can obtain one by:
1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

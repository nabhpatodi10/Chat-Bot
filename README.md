# Chat-Bot

## Overview

This repository contains a chatbot project built in Python using LangChain, Mongo DB, Google Gemini API and Groq API. The project employs vector embeddings for processing and storing information in a MongoDB database. Additionally, it includes a FastAPI implementation for interacting with the chatbot.

## Features

- **LangChain Integration**: Utilizes LangChain for connecting to LLMs.
- **Google Gemini API**: Integrates with the Google Gemini API for enhanced language capabilities.
-  **Groq API**: Integrates with the Groq for utilising Llama 3.1 70b LLM for enhanced language capabilities.
- **Vector Embeddings**: Stores vector embeddings in a MongoDB database for efficient querying.
- **FastAPI**: Provides a FastAPI interface for easy interaction with the chatbot.

## Installation

To get started with this project, follow the instructions below.

### Prerequisites

Ensure you have the following installed:

- Python 3.9 or higher
- MongoDB
- Google Gemini API access
- Groq API access
- FastAPI
- LangChain

You can do this by running the following command:
```bash
pip install -r requirements.txt
```

### Clone the Repository

```bash
git clone https://github.com/nabhpatodi10/Chat-Bot.git
cd Chat-Bot
```

## Configuration

### MongoDB and Google Gemini API

Set up your Mongo DB URI and Google Gemini API key and ensure it is accessible in your environment. You can set it up in a `.env` file or directly in your environment variables.

## Usage

### Running the FastAPI Server

To start the FastAPI server, run:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Project Structure

- `main.py`: Entry point for the FastAPI application.
- `query.py`: Handles the querying logic using LangChain and Google Gemini API.
- `db.py`: Manages database connections and operations with MongoDB.

## API Endpoints

### /storevector
Here we can input a string which will be appended to a text file and then the entire content of the text file will be converted into vector embeddings and then stored in the Mongo DB.

### /queryresult
Here the chatbot will take the user input as string and then give the answer to the question as the output. This output will be generated using the vector embeddings stored in the Mongo DB.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

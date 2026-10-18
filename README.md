
# Winter Soup Ideas Using LangChain

## Overview
This project uses LangChain and OpenAI's GPT-4o-mini model to generate exactly five healthy soup ideas for winter.

## Technologies Used
- Python
- LangChain
- ChatOpenAI
- OpenAI API
- python-dotenv

## Project Structure

```text
Winter-Soup-Ideas/
├── breakfast.py
├── .env
├── .gitignore
└── README.md
```

## Requirements
- Python 3.9 or later
- OpenAI API key

## Installation

Install the required packages:

```bash
pip install langchain-openai python-dotenv
```

## Configuration

Create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

Replace the placeholder with your actual API key.

**Security:** Never commit your `.env` file or expose your API key on GitHub.

## Execution

Run the script from your terminal:

```bash
python breakfast.py
```

The program generates exactly five healthy winter soup ideas, formatted as a numbered list with one line per idea.

## Key Learning Outcomes

- Using LangChain's `ChatOpenAI` class.
- Sending prompts with `llm.invoke()`.
- Extracting the response text using `reply.content`.
- Writing specific prompts to control output format.
- Loading API keys securely using environment variables.
- Comparing model responses across multiple runs.

## Assignment Result

Executed the script twice and compared the generated soup ideas.

**Run comparison:** Update this section with whether both runs produced the same five ideas.

## Author
Python and LangChain Learning Assignment

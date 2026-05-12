# Learning Tutorial Generator

A small tool that fetches a given article, processes the content with a local Llama model, and generates a learning tutorial as a Markdown file.

## What it does

The project takes an article URL as input, extracts the article content, and uses a locally running Llama model to create a clear, structured learning tutorial. The final output is saved as a `.md` file.

## Features

- Fetches content from a provided article URL
- Extracts the article text and relevant links
- Uses a local Llama model for tutorial generation
- Exports the result as a Markdown file
- Runs locally without relying on external AI APIs

## Requirements

- Python 3.10+
- A local Llama model setup
- Internet access for fetching article content

## Usage

```bash
python create_summary.py https://example.com/article
# Brochure Generator

A small tool that fetches information from a given website, processes the content with a local Llama model, and generates a company brochure as a Markdown file.

## What it does

The project takes a website URL as input, extracts relevant company information, and uses a locally running Llama model to create a concise brochure-style summary. The final output is saved as a `.md` file.

## Features

- Fetches content from a provided website
- Extracts useful company information
- Uses a local Llama model for brochure generation
- Exports the result as a Markdown file
- Runs locally without relying on external AI APIs

## Requirements

- Python 3.10+
- A local Llama model setup
- Internet access for fetching website content

## Usage

```bash
python create_brochure.py https://example.com
# AI Poem/Lyrics Generator

Generate creative text such as poetry or lyrics from a given topic using a Hugging Face text-generation pipeline.

## Features

- Turns a topic or prompt into a short piece of creative text (poem or lyrics)
- Wraps the `transformers` `text-generation` pipeline
- Uses the small, widely available GPT-2 model by default
- Minimal, class-based API (`PoemGenerator`)

## Requirements

- Python 3.8 or newer
- `transformers`
- PyTorch (`torch`) as the pipeline backend
- An internet connection on the first run, to download the model weights

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from ai_content_creator import PoemGenerator

generator = PoemGenerator()
print(generator.generate_poem("the ocean"))
```

The first call downloads the default model, so it may take a moment. Generation is sampled, so repeated runs on the same topic produce different output.

## Project Structure

```text
ai_content_creator/
├── ai_content_creator.py   # PoemGenerator implementation
├── requirements.txt
└── README.md
```

## License

This project is released under the **MIT License**.

## Author

**Roxana Khaleghi**

# AI Poem & Lyrics Generator

Generate short creative text — poems or lyrics — from a topic prompt, using a pretrained
GPT-2 language model through Hugging Face `transformers`.

## What it does

`ai_content_creator.py` defines `PoemGenerator`, which loads the `gpt2` text-generation
pipeline and produces a short sample for a given topic.

```python
from ai_content_creator import PoemGenerator

generator = PoemGenerator()
print(generator.generate_poem("the ocean"))
```

## Requirements

- Python 3.9+
- `transformers`, `torch` (see `requirements.txt`)

```bash
python -m pip install -r requirements.txt
```

The first run downloads the `gpt2` weights (about 500 MB) from the Hugging Face Hub.

## Notes and limitations

- The model is small and English-only; output is a rough draft, not a finished piece.
- Generation uses sampling (`do_sample=True`) with `max_length=100`, so results vary per run.
- Long inputs are truncated from the left side of the prompt: keep the topic short.

## Status

Single-module prototype. Packaging as an importable package and a command-line entry point
is planned; the file currently combines the module source and its documentation.

## License

No license file is present yet. Until one is added, the default copyright applies.

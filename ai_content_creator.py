# ai_content_creator/generator.py
from transformers import pipeline

class PoemGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_poem(self, topic):
        return self.generator(f"Write a short poem about {topic}", max_length=100, do_sample=True)[0]['generated_text']

# ai_content_creator/README.md
"""
# AI Poem/Lyrics Generator

Generate creative text such as poetry or lyrics from a given topic.

## Example:
```python
g = PoemGenerator()
print(g.generate_poem("the ocean"))
```
"""
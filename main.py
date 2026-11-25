"""Example usage for the AI content creator.

Run:  python main.py "the ocean"
"""

import sys

from ai_content_creator.generator import PoemGenerator


def main() -> None:
    topic = sys.argv[1] if len(sys.argv) > 1 else "the ocean"
    generator = PoemGenerator()
    print(generator.generate_poem(topic))


if __name__ == "__main__":
    main()

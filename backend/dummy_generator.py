# Dummy generator for local testing.
# Replace this with your AI backend code when ready.

import random

sample_posts = [
    "Exploring new ideas in AI media ecosystems.",
    "A quick update from the generative feed!",
    "Today's topic: emergent digital worlds.",
    "Welcome to the AI feed prototype.",
    "This post was generated using the local dummy backend.",
]

def generate_post(topic="General"):
    return f"[{topic}] " + random.choice(sample_posts)

if __name__ == "__main__":
    print(generate_post("Demo"))

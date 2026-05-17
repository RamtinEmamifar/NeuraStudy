"""
Explain Mode for NeuraStudy.

Returns a simple, beginner-friendly explanation for a given topic.
This MVP uses a small built-in dictionary of common topics.
If the topic is unknown, it returns a generic helpful message.
"""

# A small built-in knowledge base for the MVP.
# Keys are stored in lowercase for easy lookup.
KNOWLEDGE_BASE = {
    "python": (
        "Python is a popular programming language known for being easy to read "
        "and write. It is used for web development, data analysis, artificial "
        "intelligence, automation, and more."
    ),
    "math": (
        "Math is the study of numbers, shapes, and patterns. It helps us solve "
        "problems, measure things, and understand how the world works."
    ),
    "physics": (
        "Physics is the science of matter, energy, and how they interact. "
        "It explains things like motion, gravity, light, and electricity."
    ),
    "biology": (
        "Biology is the study of living things — plants, animals, and humans. "
        "It explores how organisms grow, reproduce, and interact with their environment."
    ),
    "history": (
        "History is the study of past events, people, and societies. It helps "
        "us understand how the world we live in today came to be."
    ),
    "ai": (
        "AI (Artificial Intelligence) is the field of building computer systems "
        "that can perform tasks usually requiring human intelligence, such as "
        "understanding language, recognizing images, or making decisions."
    ),
    "machine learning": (
        "Machine learning is a part of AI where computers learn patterns from "
        "data instead of being directly programmed with rules."
    ),
}


def explain_topic(topic):
    """
    Return a simple explanation of the given topic.

    Args:
        topic (str): The topic the user wants to learn about.

    Returns:
        str: A short, beginner-friendly explanation.
    """
    key = topic.strip().lower()

    if key in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[key]

    # Fallback message for unknown topics
    return (
        f"Sorry, I don't have a built-in explanation for '{topic}' yet.\n"
        f"Try a general topic like: python, math, physics, biology, history, "
        f"ai, or machine learning.\n"
        f"(Future versions of NeuraStudy will support many more topics!)"
    )

"""
Quiz Mode for NeuraStudy.

Generates 3-5 simple exam-style questions about a given topic.
Uses generic question templates so it works for any input.
"""

# Generic question templates that work for any topic
QUESTION_TEMPLATES = [
    "What is {topic}?",
    "Can you give a real-life example of {topic}?",
    "Why is {topic} important?",
    "What are the main ideas or concepts behind {topic}?",
    "How would you explain {topic} to a friend in one sentence?",
]


def generate_quiz(topic):
    """
    Generate a list of simple quiz questions about the topic.

    Args:
        topic (str): The topic for the quiz.

    Returns:
        list[str]: A list of 5 questions about the topic.
    """
    topic = topic.strip()
    questions = [template.format(topic=topic) for template in QUESTION_TEMPLATES]
    return questions

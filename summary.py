"""
Summary Mode for NeuraStudy.

Takes a block of text and returns a short bullet-point summary.
This MVP uses a simple rule:
- Split the text into sentences.
- Return the first few sentences (and the longest one) as key points.
"""


def split_into_sentences(text):
    """
    Split text into sentences using common punctuation marks.

    Args:
        text (str): The input text.

    Returns:
        list[str]: A list of sentence strings.
    """
    # Replace common end-of-sentence marks with a single marker, then split.
    marker = "<SPLIT>"
    for punct in [".", "!", "?"]:
        text = text.replace(punct, punct + marker)

    sentences = [s.strip() for s in text.split(marker) if s.strip()]
    return sentences


def summarize_text(text, max_bullets=5):
    """
    Return a short bullet-point summary of the input text.

    Args:
        text (str): The text to summarize.
        max_bullets (int): Maximum number of bullet points to return.

    Returns:
        list[str]: A list of summary bullets.
    """
    sentences = split_into_sentences(text)

    if not sentences:
        return ["No content to summarize."]

    # If there are fewer sentences than max_bullets, return them all.
    if len(sentences) <= max_bullets:
        return sentences

    # Otherwise, pick the first sentences (they usually contain the main idea)
    # plus the longest sentence (often the most informative).
    summary = sentences[: max_bullets - 1]
    longest = max(sentences, key=len)
    if longest not in summary:
        summary.append(longest)

    return summary

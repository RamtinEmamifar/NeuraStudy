"""
NeuraStudy - A simple terminal-based learning assistant.

This is the main entry point. It shows a menu and lets the user
choose between three modes: Explain, Quiz, and Summary.
"""

from explain import explain_topic
from quiz import generate_quiz
from summary import summarize_text


def show_menu():
    """Print the main menu options."""
    print("\n" + "=" * 40)
    print("       Welcome to NeuraStudy 📚")
    print("=" * 40)
    print("1. Explain a topic")
    print("2. Generate a quiz")
    print("3. Summarize text")
    print("4. Exit")
    print("=" * 40)


def run_explain_mode():
    """Ask the user for a topic and print an explanation."""
    topic = input("\nEnter a topic to explain: ").strip()
    if not topic:
        print("⚠️  No topic provided.")
        return
    explanation = explain_topic(topic)
    print("\n--- Explanation ---")
    print(explanation)


def run_quiz_mode():
    """Ask the user for a topic and print quiz questions."""
    topic = input("\nEnter a topic for the quiz: ").strip()
    if not topic:
        print("⚠️  No topic provided.")
        return
    questions = generate_quiz(topic)
    print("\n--- Quiz Questions ---")
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question}")


def run_summary_mode():
    """Ask the user for text and print a bullet-point summary."""
    print("\nPaste your text below. Press Enter twice when finished:")
    lines = []
    empty_line_count = 0
    while True:
        line = input()
        if line == "":
            empty_line_count += 1
            if empty_line_count >= 1 and lines:
                break
        else:
            empty_line_count = 0
            lines.append(line)

    text = " ".join(lines).strip()
    if not text:
        print("⚠️  No text provided.")
        return

    bullets = summarize_text(text)
    print("\n--- Summary ---")
    for bullet in bullets:
        print(f"• {bullet}")


def main():
    """Run the main application loop."""
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            run_explain_mode()
        elif choice == "2":
            run_quiz_mode()
        elif choice == "3":
            run_summary_mode()
        elif choice == "4":
            print("\nGoodbye! Keep learning 🚀")
            break
        else:
            print("⚠️  Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

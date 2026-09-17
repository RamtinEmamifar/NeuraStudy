# NeuraStudy 📚

A simple, beginner-friendly **terminal-based learning assistant** for students.

NeuraStudy helps you understand topics, generate quick quizzes, and summarize text — all from your terminal, with no internet or API keys required.

---

## ✨ Features

- **Explain Mode** — Type a topic and get a simple, easy-to-understand explanation.
- **Quiz Mode** — Get 5 simple exam-style questions on any topic to test yourself.
- **Summary Mode** — Paste any block of text and receive a short bullet-point summary.

---

## 🛠️ Tech Stack

- **Language:** Python 3 (standard library only)
- **Interface:** Terminal / Command-line
- **External APIs:** None

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/RamtinEmamifar/NeuraStudy.git
   cd NeuraStudy
   ```

2. **Run the app**
   ```bash
   python main.py
   ```

3. **Choose an option from the menu** (1–4) and follow the prompts.

> ✅ Requires **Python 3.6+**. No installations or dependencies needed.

---

## 📂 Project Structure

```
NeuraStudy/
│
├── main.py        # Entry point — shows menu and handles user input
├── explain.py     # Logic for explaining topics
├── quiz.py        # Logic for generating quiz questions
├── summary.py     # Logic for summarizing text
└── README.md      # This file
```

---

## 💡 Example Usage

```
========================================
       Welcome to NeuraStudy 📚
========================================
1. Explain a topic
2. Generate a quiz
3. Summarize text
4. Exit
========================================
Choose an option (1-4): 1

Enter a topic to explain: python

--- Explanation ---
Python is a popular programming language known for being easy to read
and write. It is used for web development, data analysis, artificial
intelligence, automation, and more.
```

---

## 🔮 Future Improvements (v2 Ideas)

- Integrate an AI model (local or API-based) for dynamic explanations and smart quizzes
- Save user sessions and progress to a local file
- Add a flashcard-style review mode with spaced repetition

---

## 📜 License

This project is open-source and free to use under the MIT License.

---

Made with ❤️ for students who want to learn better.

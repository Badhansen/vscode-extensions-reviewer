# VSCode Extensions Reviewer

A set of Python scripts to fetch and export user reviews for popular AI coding assistant extensions from the Visual Studio Code Marketplace.

---

## 🚀 Features

-   Fetches reviews for:
    -   GitHub Copilot
    -   Claude Code for VSCode
    -   Gemini Code Assist
-   Exports reviews to Excel files for easy analysis

---

## 📦 Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/Badhansen/vscode-extensions-reviewer.git
    cd vscode-extensions-reviewer
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install required packages**

    ```bash
    pip install -r requirements.txt
    ```

---

## 🛠️ Usage

Run any of the scripts to fetch reviews and save them as Excel files in the `data/` directory:

-   **GitHub Copilot:**

    ```bash
    python copilot.py
    ```

-   **Claude Code for VSCode:**

    ```bash
    python claude.py
    ```

-   **Gemini Code Assist:**
    ```bash
    python google.py
    ```

The output Excel files will be named with the extension and the current date.put Excel files will be named with the extension and the current date.

---

## 📁 Project Structure

```
vscode-extensions-reviewer/
├── claude.py
├── copilot.py
├── google.py
├── requirements.txt
├── data/
└── README.md
```

---

## 📝 Notes

-   Make sure the `data/` directory exists before running the scripts. the `data/` directory exists before running the scripts.
-   The scripts use public APIs and may be subject to rate limits.- The scripts use public APIs and may be subject to rate limits.

---

## 📄 License

MIT License

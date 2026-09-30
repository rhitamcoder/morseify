# 🆘 Morseify

**A simple command-line tool that converts text into Morse code.**

Morseify takes any text you type, letters, numbers, periods, commas, and spaces, and converts it into Morse code right in your terminal. It validates your input before converting, so you'll never get a silent failure or a crash from an unsupported character.

---

## 🎮 How to Use

1. Run the script
2. Type the text you want converted (uppercase or lowercase, both work)
3. Get your Morse code output instantly
4. Choose whether to convert something else or exit

**Example:**

```
=== Welcome to Morseify 🆘 ===
Kindly provide the items you want to convert into Morse: SOS HELP
... --- ... / .... . .-.. .--.
Do you want to use the tool again? (y/n):
```

---

## ✨ Features

- 🔤 **Full alphabet & digit support** — converts A-Z and 0-9 to Morse code
- ✅ **Input validation** — rejects unsupported characters and re-prompts instead of crashing
- 🔁 **Loop until you're done** — convert as many phrases as you like in one session
- ␣ **Space handling** — spaces between words are converted to `/`, the standard Morse word separator
- 🔡 **Case-insensitive** — input is automatically uppercased before conversion

---

## 🛠️ Tech Stack

- **Python 3** — no external libraries or dependencies required

---

## 📁 Project Structure

```
morseify/
├── code.py          # Full conversion logic
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (pure standard library, nothing else needed)

### Running the Tool

```
git clone https://github.com/rhitamcoder/morseify.git
```
```
cd morseify
```
```
python code.py
```

Type your text when prompted, and Morseify will print the Morse code translation.

---

## 🧠 How It Works

- **`code_dict`** maps every supported character (A-Z, 0-9, `.`, `,`, and space) to its Morse code equivalent
- **Input validation** loops until every character in the input exists as a key in `code_dict`, rejecting anything unsupported
- **`text_to_morse()`** loops through each character of the input and looks up its Morse code, joining the results with spaces
- An outer loop lets you convert multiple phrases in one run, exiting only when you choose not to continue

---

## 📌 Supported Characters

| Type | Characters |
|------|-----------|
| Letters | A–Z |
| Digits | 0–9 |
| Punctuation | `.` `,` |
| Whitespace | Space (converted to `/`) |

Any other character (e.g. `!`, `?`, `@`) will trigger a "invalid character" prompt to try again.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

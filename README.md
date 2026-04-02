# MDViewer

A simple, fast, and user-friendly Markdown viewer for the desktop, built with Python and PySide6.

## Features
- View Markdown files in a clean, native desktop window
- Supports opening files via command line or piping from standard input
- Syntax highlighting and basic Markdown rendering
- Cross-platform (tested on macOS)

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/karltbraun/mdviewer.git
   cd mdviewer
   ```
2. **Set up the Python environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   *(Or use [uv](https://github.com/astral-sh/uv) for faster installs if available)*

3. **(Optional) Add the wrapper script to your PATH:**
   ```sh
   cp mdviewer ~/bin/
   chmod +x ~/bin/mdviewer
   ```

## Usage
- **Open a Markdown file:**
  ```sh
  ./mdviewer path/to/file.md
  ```
- **Pipe Markdown content:**
  ```sh
  cat file.md | ./mdviewer
  ```

## Development
- Main application: `src/main.py`
- Bash wrapper: `mdviewer`
- Requires Python 3.8+ and PySide6

## License
MIT License

---

*Created by Karl T. Braun*

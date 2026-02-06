# Desktop Assistant 🖥️

A Python-based desktop assistant that responds to text commands to automate common system tasks and provide entertainment.

## 🌟 Features

This intelligent assistant can perform the following actions:

- **🌐 Browser Automation**: Open Chrome and perform Google searches
- **📝 Text Editing**: Launch Notepad for quick note-taking
- **🎨 Creative Tools**: Open Paint for drawing and image editing
- **📸 Camera Access**: Launch system camera for photos/selfies
- **🎲 Entertainment**: Play Heads or Tails coin flip game
- **😂 Humor**: Tell random jokes to brighten your day
- **🔍 Web Search**: Perform Google searches directly from the assistant
- **⏰ System Info**: Display current date and time

## 🚀 Getting Started

### Prerequisites

- **Python 3.8 or higher**
- **Windows 10/11**, **macOS 10.15+**, or **Linux** (Ubuntu 20.04+/Debian 10+)

### Installation Instructions

#### 🔧 Windows Setup

1. **Install Python**:
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Dependencies**:
   ```powershell
   pip install pyttsx3==2.90
   ```

3. **Run the Assistant**:
   ```powershell
   python prog.py
   ```

#### 🍎 macOS Setup

1. **Install Python**:
   ```bash
   # Using Homebrew (recommended)
   brew install python
   ```

2. **Install Dependencies**:
   ```bash
   pip3 install pyttsx3==2.90
   ```

3. **Run the Assistant**:
   ```bash
   python3 prog.py
   ```

#### 🐧 Linux Setup

1. **Install Python and Dependencies**:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip espeak
   
   # Install Python package
   pip3 install pyttsx3==2.90
   ```

2. **Run the Assistant**:
   ```bash
   python3 prog.py
   ```

### 📋 Requirements

- **Python**: 3.8 or higher
- **pyttsx3**: 2.90 (Text-to-speech engine)
- **System Applications**: Chrome, Notepad, Paint, Calculator (pre-installed on most systems)

> **Note**: If you encounter pyttsx3 errors on Linux, ensure `espeak` is installed using the command above.

## 🎮 Usage Guide

### Basic Commands

The assistant responds to three main command types:

1. **Run/Launch/Open** - Start applications
2. **Close/Kill/Exit** - Terminate applications  
3. **Other Commands** - Special features

### 📚 Command Examples

#### Browser Operations
```
User: "run chrome"
Assistant: Asks what to search for
User: "python tutorials"
Assistant: Opens Chrome with Google search results

User: "close chrome"
Assistant: Closes all Chrome instances
```

#### Text Editor
```
User: "open notepad"
Assistant: Launches Notepad application

User: "close notepad"
Assistant: Closes Notepad
```

#### Creative Tools
```
User: "launch paint"
Assistant: Opens Microsoft Paint

User: "close paint"
Assistant: Closes Paint application
```

#### Calculator
```
User: "open calculator"
Assistant: Launches system calculator

User: "close calculator"
Assistant: Closes calculator
```

#### Camera & System Info
```
User: "open camera"
Assistant: Launches system camera app

User: "what is the date"
Assistant: Shows current system date

User: "what is the time"
Assistant: Shows current system time
```

#### Entertainment Features
```
User: "tell me a joke"
Assistant: Shares a random programming joke

User: "play heads or tails game"
Assistant: Starts interactive coin flip game
```

### 🎯 Sample Interaction Session

```
Hello User
How can I help you: run chrome
What you want to search: machine learning
Request Initiated
[Chrome opens with ML search results]

How can I help you: open notepad
Request Initiated!!
[Notepad launches]

How can I help you: tell me a joke
This might make you laugh
Write an essay on cricket the teacher told the class, Chintu finishes his work in five minutes...

How can I help you: exit
Ok Bye,See You later
```

## 🛠️ Development

### Project Structure
```
Desktop-Assistant/
├── prog.py          # Main application code
├── requirements.txt # Python dependencies
├── README.md        # This documentation
├── LICENSE          # MIT License
└── .gitignore       # Git ignore rules
```

### Code Overview
The main application (`prog.py`) contains:
- **Command parsing logic** for user input
- **Cross-platform application launching** using `subprocess` and `os`
- **Text-to-speech functionality** via `pyttsx3`
- **Game implementation** for entertainment features
- **Error handling** for common issues

## 🤝 Contributing

We welcome contributions from the community! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Start for Contributors
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Developed as part of the **IIEC RISE** Python Specialist course
- Mentored by **Mr. Vimal Daga** (World Record Holder)
- Built with Python and pyttsx3 text-to-speech engine

---

⭐ **Star this repository if you find it helpful!**

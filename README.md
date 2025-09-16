# Mental Health Chatbot

A prototype mental health chatbot built with Python (Flask) and a modular structure. This app demonstrates conversational support and basic mental health check-ins.

## Features

- Interactive chat interface
- Modular chatbot logic
- Simple database storage (local file or SQLite)
- Easy to extend for new features

## Project Structure

```
mental-health-chatbot/
├── app.py
├── models/
│   └── chatbot.py
├── storage/
│   └── database.py
├── utils/
│   └── helpers.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
└── README.md
```

## Getting Started

1. Clone the repository
2. Create a virtual environment and install dependencies:
   ```
pip install -r requirements.txt
```
3. Run the app:
   ```
python app.py
```
4. Open your browser at `http://localhost:5000`

## License

MIT

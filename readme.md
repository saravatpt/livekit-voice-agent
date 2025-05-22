# LiveKit Voice Agent

This project is a Live agent built using LiveKit.

## Requirements

- Python 3.7+
- See `requirements.txt` for Python dependencies.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in a `.env` file.
4. Run the agent.

## Usage

### Support Agent (`support-agent.py`)
This agent is a general-purpose live agent.

**How to Run:**
To run the Support Agent in console mode:
```bash
python support-agent.py console
```
To run the Support Agent in development mode (for testing with LiveKit demo page):
```bash
python support-agent.py dev
```

### Interview Agent (`interview-agent.py`)

This agent is designed to conduct technical interviews for an AI/ML Engineer (Fresher) position. It follows a structured interview process and interacts with both the candidate and HR.

**Key Features:**
-   **Candidate ID Validation:** Requires candidates to provide a valid interview ID.
-   **Resume Validation:** Checks if the candidate's resume matches the job description.
-   **Environment Check:** Ensures the candidate shares their screen and turns on their camera, with only a notepad visible.
-   **Structured Interview:** Asks basic AI/ML questions, Python questions, and a coding question.
-   **HR Interaction:** Provides an interview summary and rating to HR upon request with a valid HR ID (e.g., H1234).

**How to Run:**
To run the Interview Agent:
```bash
python interview-agent.py
```

## Contributing

[Information on how to contribute]

## License

[License information]

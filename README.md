# URL Shortener with Analytics

A lightweight URL shortening service built with FastAPI and SQLite. Generate short URLs from long ones, redirect users to the original sites, and (optionally) track click analytics—all in a simple Python application.

## Features
- **Shorten URLs**: Convert long URLs into 6-character short codes (e.g., `http://localhost:8000/xyz789`).
- **Redirect**: Visit a short URL to be redirected to the original destination.
- **Analytics**: Tracks click counts per short URL (stats endpoint in progress).

## Tech Stack
- **FastAPI**: A modern, high-performance Python web framework.
- **SQLite**: A serverless database for storing URL mappings and click data.
- **Uvicorn**: An ASGI server to run the FastAPI app.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DylGit3/url-shortener
   cd url-shortener
2. **Install requirements**:
pip install -r requirements.txt
3. **Run the App**:
uvicorn app.main:app --reload
4. **Input long URL**:
Open new terminal and type in the following:
    curl -X POST "http://localhost:8000/shorten" -d "long_url=https://example.com" -H "Content-Type: application/x-www-form-urlencoded"

## Future Improvements
Add a /stats/{short_code} endpoint for click analytics (in progress).
Create a simple HTML frontend for user-friendly URL shortening.
Deploy to Render for public access.
Add URL validation to ensure valid input.

## License
Feel free to use and modify

## Why I Created This
I built this project to sharpen my skills in modern Python web development using FastAPI, a framework I wanted to explore for its speed and ease of use. It’s a practical, real-world application that combines API design, database management with SQLite, and a bit of analytics—all in a week-long sprint. I aimed to create something functional for my portfolio that demonstrates clean code, problem-solving (like handling form data and imports), and a foundation I can extend with features like deployment or a frontend. Plus, who doesn’t love a good URL shortener?
from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
import random
import string
from .database import save_url, get_url


def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def setup_routes(app: FastAPI, db):
    @app.post("/shorten")
    async def shorten(long_url: str = Form(...)):
        short_code = generate_code()
        save_url(db, short_code, long_url)
        return {"short_url": f"http://localhost:8000/{short_code}"}

    @app.get("/{short_code}")
    async def redirect(short_code: str):
        result = get_url(db, short_code)
        if result:
            long_url, clicks = result
            db.execute("UPDATE urls SET clicks = ? WHERE short = ?",
                       (clicks + 1, short_code))
            db.commit()
            return RedirectResponse(long_url)
        return {"error": "Not found"}

    # TESTING NEEDED
    @app.get("/stats/{short_code}")
    async def stats(short_code: str):
        result = get_url(db, short_code)
        if result:
            long_url, clicks = result
            return {"long_url": long_url, "clicks": clicks}
        return {"error": "Not found"}

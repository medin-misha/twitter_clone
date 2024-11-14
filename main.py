from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from handlers import user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/me", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.get("/api/users/me")
async def func():
    return {
        "result": "true",
        "user": {
            "id": "int",
            "name": "str",
            "followers": [{"id": "int", "name": "str"}],
            "following": [{"id": "int", "name": "str"}],
        },
    }


app.mount("/static", StaticFiles(directory="static/"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8977)

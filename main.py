from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from handlers import user_router, media_router, tweet_router, get_image

app = FastAPI()

app.include_router(user_router)
app.include_router(media_router)
app.include_router(tweet_router)


@app.get("/me", response_class=HTMLResponse)
async def main():
    return FileResponse("./static/index.html")


app.mount("/static", StaticFiles(directory="./static/"), name="static")


@app.get("/{filename}")
async def get_image_view(filename: str):
    image = await get_image(filename=filename)
    return image


if __name__ == "__main__":
    uvicorn.run("main:app", port=8977)

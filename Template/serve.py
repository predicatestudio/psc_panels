from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory=Path(__file__).parent), name="static")


@app.get("/")
def home():
    return RedirectResponse("static/example.html")


def main():
    uvicorn.run("serve:app", reload=True)


if __name__ == "__main__":
    main()

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")
template = Jinja2Templates(".")


def get_panels():
    panels = []
    for dir in [obj for obj in Path(__file__).parent.iterdir() if obj.is_dir()]:
        if dir.joinpath("example.html").exists():
            panels.append(str(dir.stem))
    return panels


@app.get("/")
def home(request: Request):
    return template.TemplateResponse(
        "index.html", {"request": request, "example_panels": get_panels()}
    )


def main():
    import uvicorn

    uvicorn.run("serve:app", reload=True)


if __name__ == "__main__":
    main()

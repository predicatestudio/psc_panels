from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()
template = Jinja2Templates(".")


def get_panels():
    """Dynamically searches for panels with an example.html"""
    panels = []
    for dir in [obj for obj in Path(__file__).parent.iterdir() if obj.is_dir()]:
        if dir.joinpath("example.html").exists():
            panels.append(str(dir.stem))
    return panels


# Mount panel dirs as static files
for panel in get_panels():
    app.mount("/" + panel, StaticFiles(directory=panel), name=panel)

# Index with links to examples
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

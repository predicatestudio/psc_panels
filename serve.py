from genericpath import exists
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json
import uvicorn


app = FastAPI()
template = Jinja2Templates(".")


def get_panels():
    """Dynamically searches for panels with an example.html"""
    panels = []
    for dir in [obj for obj in Path(__file__).parent.iterdir() if obj.is_dir()]:
        if dir.joinpath("example.html").exists():
            panels.append(str(dir.stem))
    return panels


# Mounts each panel in static
for panel in get_panels():
    app.mount("/static/" + panel, StaticFiles(directory=panel), name=panel)


@app.get("/display/{panel}")
def showcase(request: Request, panel):
    data_file = Path(f"./{panel}/panelData.json")
    panel_data = {}
    print(data_file.absolute())
    print("/home/benjamin/predicatestudio/psc_panels/SwitchPanel/panelData.json")
    if data_file.exists():
        with data_file.open("r") as f:
            panel_data = json.load(f)
    return template.TemplateResponse(
        "showcase.html",
        {"request": request, "panel": panel, "panel_data": panel_data},
    )


# Index with links to examples
@app.get("/")
def home(request: Request):
    return template.TemplateResponse(
        "index.html", {"request": request, "example_panels": get_panels()}
    )


def main():
    uvicorn.run("serve:app", reload=True)


if __name__ == "__main__":
    main()

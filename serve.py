from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json

app = FastAPI()
template = Jinja2Templates(".")


def get_panels():
    """Dynamically searches for panels with an example.html"""
    panels = []
    for dir in [obj for obj in Path(__file__).parent.iterdir() if obj.is_dir()]:
        if dir.joinpath("example.html").exists():
            panels.append(str(dir.stem))
    return panels

with Path('/home/benjamin/predicatestudio/psc_panels/SwitchPanel/switch-panel.json').open('r') as f:
    my_data=json.load(f)
    # {
    #     "switches": [
    #         {'label': "Gray Switch"},
    #         {"label": "Blue Switch", "color": "primary"},
    #         {"label": "Green Switch", "color": "success"},
    #         {"label": "Info Switch", "color": "info"},
    #         {"label": "Warning Switch", "color": "warning"},
    #         {"label": "Danger Switch", "color": "danger"},
    #     ],
    #     "head": "Default Header",
    # },

# Mount panel dirs as static files
for panel in get_panels():
    app.mount("/static/" + panel, StaticFiles(directory=panel), name=panel)

@app.get("/display/{panel}")
def showcase(request: Request, panel):
    # return("hello World")
    return template.TemplateResponse(
        "showcase.html",
        {
            "request": request,
            "panel": panel,
            "panel_data": my_data
            
        },
    )


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

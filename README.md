# psc_panels
A free and open source kit of ui-components used by Predicate Studio and open to more.


## Viewing a panel

To view a panel, open the associated example.html in a basic server, such as VS-Code's live server. A similar server can be run from the adjacent serve.py. Note that your python environment will need fastapi and uvicorn installed.
````
pip install fastapi uvicorn
````
Alternatively, consider running the top-level .py file, server.py. This will allow you to peruse each panel. The requirements are the same.

## Creating Components

To create a panel component, start with the template file. The files within are as follows:

#### serve.py
This file is an extremely simple server. Run it to locally host the adjacent example.html for viewing and testing.
#### example.html
This is an example html implementation of your panel. Ideally this has very little variation from the template.
This is only used with the adjacent serve.py.
#### Example.vue
This is an example .vue implementation of your panel. Ideally this has very little variation from the template.
This is only used with server.py
#### panelData.json
This is sample json object for this panel. To provide more examples for the sake of documentation, consider adding a json folder with alternatives. 
#### Template.vue
This file should be renamed to your panel name. This should be the true core of your panel.
#### /components
This directory should contain .vue files containing components for your panel.

## Requirements
All widgets are implemented in vue.js with bootstrap 5.

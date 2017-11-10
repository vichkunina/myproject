from jinja2 import Environment, FileSystemLoader
from webob import Request
import os

assets = [
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]

css = []
js = []


def app(environ, start_response):
    response_code = '200 OK'
    response_type = ('Content-Type', 'text/HTML')
    start_response(response_code, [response_type])

    for item in assets:
        (shortname, extension) = os.path.splitext(item)
        if extension == '.css':
            css.append(item)
        elif extension == '.js':
            js.append(item)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    print(template.render(css=css, js=js))


req = Request.blank('index.html')
print(req.get_response(app))

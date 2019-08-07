from flask import render_template, url_for
import json
import pprint
import pathlib
import yaml

from dummyapp import app_obj, API_PREFIX


def load_api_documentation():
    p = pathlib.Path(app_obj.root_path) / "static/yaml/rest_api.yaml"
    with open(p, "r") as f:
        return yaml.safe_load(f)


def unquote_embedded_json(s: str) -> str:
    """Handle quoted, multiline embedded json

    e.g.:
        value: |
            '{'
            '   "key": value,
            '}'

    Returns: valid json string
    """
    quote_chars = ['\'', "\""]

    def unquote(line):
        if line[0] in quote_chars:
            line = line[1:]
        if line[len(line)-1] in quote_chars:
            line = line[:-1]
        return line

    return "".join(map(unquote, filter(lambda x: len(x) > 0, s.split("\n"))))


def process():
    HOST = "localhost"
    PORT = 5000

    documentation = load_api_documentation()
    methods = []

    for endpoint in documentation["endpoints"]:
        m = {
            "route": f"{endpoint['route']}",
            "endpoint": f"http://{HOST}:{PORT}/{API_PREFIX}{endpoint['route']}"
        }

        if "example" in endpoint:
            try:
                example_value = endpoint["example"]
                # pprint.pprint(f"value: {example_value}")
                example_str = unquote_embedded_json(example_value)
                structure = json.loads(example_str)
                beautified = json.dumps(structure, indent=4)

                m["example_raw"] = (structure,)
                m["example"] = beautified

            except Exception as e:
                print(e)
        methods.append(m)

    return methods


@app_obj.route("/")
def index():
    return render_template("index.html")


@app_obj.route("/documentation")
def documentation():
    methods = process()
    # pprint.pprint(methods)
    return render_template("documentation.html", methods=methods, api_prefix=API_PREFIX)

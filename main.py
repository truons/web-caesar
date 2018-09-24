from flask import Flask, request
from caesar import rotate_string
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader )

app = Flask(__name__)
app.config['DEBUG'] = True

add_form = """
 <form action="/add" method="POST">
    <label>
        Rotate by:
        <input type="text" name="rot"/>
    </label>
    <input type="Submit" name="text"/>
    </form>
"""   
@app.route("/add", methods=['POST'])
<h1></h1>
def index():
    return form.format(...)

app.run()    
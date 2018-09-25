from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
           }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/",  method="post">
            <label>
                Rotate by:
                <input type="text" name="rot" value="0">
            </label><br>
            <textarea name="text" cols="70" rows="10">{0}</textarea><br>
            <input type="submit" value="Submit Query" name="submit">
        </form>
    </body>
</html>

 
"""
@app.route("/")   
def index():
    return form.format("")
   

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    message = request.form['text']
    text = rotate_string(message, rot)
    return form.format(text)
    


app.run()    
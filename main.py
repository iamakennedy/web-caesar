from flask import Flask, request 
from caesar import rotate_string

#imports the Flask class from the flask module
app = Flask(__name__)
#app will be the object created by the constructor Flask 
app.config['DEBUG'] = True
#debug configuration setting for the flask application will be enabled. Enables helpful behaviors like displaying errors in the browser, ensuring file changes are reloaded while the server is running 

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

        <form method='POST'>
        Rotate by: <input type="text" name="rot" value="0"> 
        <textarea name="text">{0}</textarea>
        <input type ="submit">
            


        </form>

    </body>

</html>

"""





@app.route("/")
#decorator that creates a mapping between the path- in this case the root or "/" and the function we are about to define 

def index():
    return form.format ("") 
#function returns a literal string 
@app.route("/", methods=['POST'])

def encrypt (): 
    text = str(request.form.get("text"))
    rot = int(request.form.get("rot"))
    
    encrypted_msg = rotate_string (text,rot) 
    return form.format(encrypted_msg)


#    return "<h1>encrypted message:</h1>"

app.run()
#pass control to the Flask object
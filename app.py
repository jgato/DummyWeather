#  This service free software: you can redistribute it and/or modify it under the terms of AGPL License

#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
#   BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT,
#   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#   WHETHER IN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#   See  LICENSE file for full license information  in the project root.

# Author: Jose Gato Luis <jgato.luis@gmail.com>


from flask import Flask
from flask import render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def hello():
    message_from_k8s= os.environ.get('MESSAGE', 'It seems there are no messages')
    return render_template("index.html", msg=message_from_k8s)

@app.route("/predict")
def predict():
    elements = [("good","https://cdn2.iconfinder.com/data/icons/weather-color-2/500/weather-01-256.png"),
    ("bad","https://cdn2.iconfinder.com/data/icons/weather-color-2/500/weather-32-256.png"),
    ("warm","https://cdn2.iconfinder.com/data/icons/weather-color-2/500/weather-21-256.png"),
    ("hot","https://cdn2.iconfinder.com/data/icons/weather-color-2/500/weather-01-256.png"),
    ("cold","https://cdn4.iconfinder.com/data/icons/free-line-christmas-icons/24/Snowflake-256.png")]

    element = random.choice(elements)
    print (element)
    return  render_template("predict.html", prediction=element[0], img =element[1])

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))


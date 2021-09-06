import flask
import requests

app = flask.Flask(__name__)


# app.config["DEBUG"] = True


@app.route('/<website>', methods=['GET'])
def proxywebsite(website):
    getwebsite = requests.get("https://" + str(website))
    if getwebsite.status_code == 200:
        return str(getwebsite.text)
    else:
        return "Error! Status code was: " + str(getwebsite.status_code)


app.run(port=8080)

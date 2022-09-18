"""
APP1
"""
from flask import Flask

app_name = 'app1'
app = Flask(app_name)


@app.route('/')
def hello_world():
    """
    Flask endpoint
    :return: TXT
    """
    return f"Hello World From {app_name}!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)


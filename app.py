import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

# get environment vars from cloud9
h = os.getenv('IP', '0.0.0.0')
p = int(os.getenv('PORT', 8080))

if __name__ == '__main__':
    app.run(debug=True,host=h,port=p)
from flask import Flask, render_template, request
import json
from zoomus import ZoomClient
import os

app = Flask(__name__)

client = ZoomClient(os.environ['ZOOM_KEY'], os.environ['ZOOM_SECRET'])

@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/response_page', methods = ['POST'])
def response_page():
    response = client.webinar.register(id="709-106-138", email="moseley.sammy@gmail.com", first_name="Samuel", last_name="Moseley")
    print(response)
    name = request.form['name']    
    return render_template('response_page.html', name=name)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
        #app.run()
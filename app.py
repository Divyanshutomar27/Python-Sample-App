from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure! This Python app is deployed using GitHub Actions on Azure App Service."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

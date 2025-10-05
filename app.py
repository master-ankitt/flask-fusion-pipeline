from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Run on all interfaces so EC2 can expose it publicly
    app.run(host='0.0.0.0', port=80)
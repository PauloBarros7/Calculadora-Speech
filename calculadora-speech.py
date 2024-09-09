from flask import Flask, render_template

CalcApp = Flask(__name__)

@CalcApp.route('/')
def app():
    return render_template('app-template.html')

if __name__ == "__main__":
    CalcApp.run(debug=True)
from flask import Flask, render_template
from flask_cors import CORS
import subprocess

app = Flask(__name__, static_folder='static')

CORS(app)

@app.route('/')
def index():
    return render_template("portal.html")

@app.route('/iniciar_robo', methods=['POST'])
def iniciar_robo():
    try:
        subprocess.Popen(["python", "C:\\Users\\gabriel.borato\\Documents\\AutomateJBPMail\\bot.py"])
    except Exception as e:
        print("Erro ao iniciar o robô:", e)
    return render_template("portal.html")

if __name__ == '__main__':
    app.run(debug=True)

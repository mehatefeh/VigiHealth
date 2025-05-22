from flask import Flask, render_template, request, jsonify
from model import analyze_blood_pressure

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    sys = data.get('systolic')
    dia = data.get('diastolic')
    pulse = data.get('pulse')
    result = analyze_blood_pressure(sys, dia, pulse)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

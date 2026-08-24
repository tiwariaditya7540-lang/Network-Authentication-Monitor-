from flask import Flask, render_template, request, jsonify
from monitor import NetworkAuthMonitor

app = Flask(__name__)
monitor = NetworkAuthMonitor(threshold=5, time_window_seconds=120)

@app.route('/')
def index():
    return render_template('dashboard.html', alerts=monitor.get_alerts())

@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    result = monitor.authenticate(data['ip'], data['username'], data['password'])
    return jsonify(result)

@app.route('/api/v1/clear-history', methods=['POST'])
def clear_history():
    monitor.clear_alerts()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
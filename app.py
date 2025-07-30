from flask import Flask, render_template, jsonify
from scanner import capture_fingerprint
from notifier import send_success_message, send_alert_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scan():
    result = capture_fingerprint()
    if result == "MATCH_123":
        send_success_message()
        return jsonify({'status': 'success'})
    else:
        send_alert_message()
        return jsonify({'status': 'fail'})

if __name__ == '__main__':
    app.run(debug=True)

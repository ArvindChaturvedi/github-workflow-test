from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/serviceB', methods=['GET'])
def service_b_endpoint():
    return jsonify({
        "message": "Hello from Service B",
        "status": "success"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

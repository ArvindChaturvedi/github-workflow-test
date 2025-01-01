from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/serviceA', methods=['GET'])
def service_a_endpoint():
    return jsonify({
        "message": "Hello from Service A",
        "status": "success"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, send_from_directory
from flask_sslify import SSLify
import os

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"\nServer running at:")
    print(f"Local:   https://localhost:5000")
    print(f"Network: https://{local_ip}:5000")
    print("\nUse the Network URL on your mobile device!")
    print("Note: You may need to accept the security warning in your browser")
    
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc', debug=True) 
import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Membaca config dari .env [cite: 23, 25]
r_host = os.getenv('REDIS_HOST', 'arkhe-core')
r_port = os.getenv('REDIS_PORT', 6379)

# Koneksi ke Redis [cite: 11]
db = redis.Redis(host=r_host, port=r_port, decode_responses=True)

@app.route('/')
def index():
    return "Monitoring Terminal: Sistem Arkhe Stabil."

@app.route('/energy')
def get_energy():
    # Simulasi pencatatan daya [cite: 11]
    count = db.incr('arkhe_energy_level')
    return jsonify({
        "status": "Stable",
        "total_energy_units": count,
        "location": "Fontaine"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
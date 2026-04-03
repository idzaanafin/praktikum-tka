import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def welcome():
    return "Welcome"

@app.route('/count')
def count():
    hits = cache.incr('hits')
    return f"Jumlah akses ke endpoint ini: {hits} kali.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

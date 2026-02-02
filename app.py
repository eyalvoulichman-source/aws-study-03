from flask import Flask
import redis
import os

app = Flask(__name__)

# שליחת שם השרת דרך משתנה סביבה (גמישות של DevOps)
redis_host = os.getenv("REDIS_HOST", "redis-service")

try:
    r = redis.Redis(host=redis_host, port=6379, decode_responses=True)
except Exception as e:
    print(f"Error connecting to Redis: {e}")

@app.route("/")
def index():
    count = r.incr("counter")
    return f"count:{count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
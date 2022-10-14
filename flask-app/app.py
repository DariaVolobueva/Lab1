from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
    "https://i.imgur.com/qeg6O0j.jpg",
    "https://i.imgur.com/OlnmoY4.jpg",
    "https://i.imgur.com/iZpNdfg.jpg",
    "https://i.imgur.com/roBPE4I.jpg",
    "https://i.imgur.com/1oIw65I.jpg",
    "https://i.imgur.com/0RHf5n9.jpg",
    "https://i.imgur.com/btJgEkq.jpg",
    "https://i.imgur.com/ZLcgOCP.jpg",
    "https://i.imgur.com/PMoTvow.jpg",
    "https://i.imgur.com/6HZg6DB.jpg",
    "https://i.imgur.com/Ke7FpMX.jpg",
    "https://i.imgur.com/NEtBSxy.jpg"
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
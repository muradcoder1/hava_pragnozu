from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key=afe2aaf24756473993f120621241403&q={city}"
    response = requests.get(url)
    
    weather_data = response.json()
    return weather_data["current"]["temp_c"], weather_data["current"]["condition"]["text"], weather_data["location"]["name"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        temperature, condition, location = fetch_weather(city)
        return render_template("index.html", city=location, temperature=temperature, condition=condition)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
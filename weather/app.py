from flask import Flask, render_template, request
import requests

# Configure application
app = Flask(__name__)
app.config["DEBUG"] = False

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    # render the home page template
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    # get the city name from the form submission
    city = request.form['city']
    
    try:
        # make an API request to get the weather data for the city
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=48f750b4ba7b9b8f2db9ed909f8ac51c'
        r = requests.get(url)
        data = r.json()
        # extract the relevant data from the API response
        des = data['weather'][0]['description']
        temp = round(data['main']['temp']-273)
        hum = round(data['main']['humidity'])
        wind = round(data['wind']['speed'] * 3.6)
        icon = data['weather'][0]['icon']
        # render the weather template, passing in the weather data
        return render_template('index.html', temp=temp, wind=wind, city=city, hum=hum, des=des, icon= icon)

    # if city is invalid
    except:
        error=True
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
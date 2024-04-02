from flask import Flask,request,render_template

# urllib.request to make a request to api 
import urllib.request 

import json
  
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'kanpur' #default name kanpur
    
    #api key 
    api = '46df8dd505279f263c4851d7cd81a1e3'
    
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read() 

    
    list_of_data = json.loads(source)
    
    def get_weather_icon(weather):
        if weather == "Clear":
            return "https://example.com/clear.png"  # URL for clear weather icon
        elif weather == "Clouds":
            return "https://example.com/clouds.png"  # URL for cloudy weather icon
        elif weather == "Rain":
            return "https://example.com/rain.png"    # URL for rainy weather icon
        else:
            return "https://example.com/default.png" # URL for default weather icon
        
    weather_icon = get_weather_icon(list_of_data['weather'][0]['main'])
    
    data = {
        
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat']), 
        "temp": str(list_of_data['main']['temp']) + 'k', 
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']), 
        "weather_icon": weather_icon
    }
    print(data) 
    return render_template('index.html', data = data) 
    
    
if __name__ == "__main__":
    app.run(debug=True)


import streamlit as st
import requests
from PIL import Image

API_key="0685156d04d06f8a234ce690ef11e50f"
def main():
    st.title("Simple Weather Casting Websit")
    city=st.text_input("Enter City Name").lower()
    if st.button("Find"): 
        appear,icon,temp,humidity,name,msg = check_weather(city)
        if msg is  None:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(icon)
            with col2:
                st.metric(f'{appear}',f"{temp}°C")
            with col3:
                st.metric("Humidity", f"{humidity}%")
            st.success(f'This is weather casting of {name}!', icon="✅")
        else:
            st.error(f'{msg}', icon="🚨")
            
        
def check_weather(city):
    base_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    weather_data=requests.get(base_url).json()
    # st.json(weather_data)
    status=weather_data['cod']
    if status==200:
        appear=weather_data['weather'][0]['main']
        icon_id=weather_data['weather'][0]['icon']
        icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        temp=round(temp_convert(weather_data['main']['temp']),2)
        humidity=weather_data['main']['humidity']
        name=weather_data['name']
        return appear,icon,temp,humidity,name,None
    else:
        msg=weather_data['message']
        return None,None,None,None,None,msg
    
def temp_convert(temp):
    return temp - 273.15

if __name__ == '__main__':
    main()
    
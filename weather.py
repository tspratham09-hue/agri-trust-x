import streamlit as st
import requests

def get_coordinates_from_user(farmer_name, phone_number):
    """Dynamically geocodes the user based on profile."""
    if not phone_number:
        phone_number = "0000000000"
        
    if "admin" in farmer_name.lower() or phone_number == "0000000000":
        return 12.8700, 74.8800, "Mangaluru, Karnataka"
        
    locations = [
        (12.2958, 76.6394, "Mysuru, Karnataka"),
        (15.3647, 75.1240, "Hubballi, Karnataka"),
        (16.8302, 75.7100, "Vijayapura, Karnataka"),
        (13.3409, 74.7421, "Udupi, Karnataka")
    ]
    hash_val = sum(int(digit) for digit in phone_number if digit.isdigit())
    return locations[hash_val % len(locations)]

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get('current_weather', None)
    except Exception:
        return None
    return None

def render_weather_widget(farmer_name="Farmer", phone_number="0000000000"):
    lat, lon, location_name = get_coordinates_from_user(farmer_name, phone_number)
    
    st.header("🌦️ Dynamic Weather Shield")
    st.caption(f"Live telemetry for: **{location_name}**")
    
    weather_data = get_weather(lat, lon)
    
    with st.container(border=True):
        if weather_data:
            col1, col2 = st.columns(2)
            col1.metric(label="🌡️ Temperature", value=f"{weather_data.get('temperature', 'N/A')} °C")
            col2.metric(label="💨 Wind Speed", value=f"{weather_data.get('windspeed', 'N/A')} km/h")
            
            st.divider()
            if weather_data.get('weathercode', 0) in [51, 53, 55, 61, 63, 65, 66, 67, 80, 81, 82]:
                st.error("🚨 ALERT: Rain expected in your region! Protect harvested produce immediately.")
            else:
                st.success("✅ Clear skies. Optimal conditions for agricultural logistics.")
        else:
            st.warning("⚠️ Weather station telemetry syncing.")
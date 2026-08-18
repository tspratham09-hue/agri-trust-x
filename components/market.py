import streamlit as st
import pandas as pd
import requests
from utils.market_engine import get_fallback_prices

# --- PREMIUM VECTOR ILLUSTRATIONS ---
CROP_IMAGES = {
    "Paddy (Rice)": "https://img.icons8.com/color/480/rice-bowl.png",
    "Arecanut": "https://img.icons8.com/color/480/palm-tree.png",
    "Coconut": "https://img.icons8.com/color/480/coconut.png",
    "Onion": "https://img.icons8.com/color/480/onion.png",
    "Tomato": "https://img.icons8.com/color/480/tomato.png",
    "Coffee": "https://img.icons8.com/color/480/coffee.png", 
    "Cotton": "https://img.icons8.com/color/480/cotton.png",
    "Sugarcane": "https://img.icons8.com/color/480/bamboo.png",
    "Maize": "https://img.icons8.com/color/480/corn.png",
    "Groundnut": "https://img.icons8.com/color/480/peanuts.png",
    "Turmeric": "https://img.icons8.com/color/480/ginger.png", 
    "Chilli (Red)": "https://img.icons8.com/color/480/chili-pepper.png",
    "Default": "https://img.icons8.com/color/480/agriculture.png"
}

def get_live_gov_data(api_key):
    """Attempts to fetch live data from the Government API."""
    # Agmarknet API endpoint for daily commodity prices
    url = f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={api_key}&format=json&limit=12"
    try:
        # We only wait 4 seconds. If Gov servers are too slow, we trigger the fallback to save the UI.
        response = requests.get(url, timeout=4)
        if response.status_code == 200:
            records = response.json().get("records", [])
            if len(records) > 0:
                return records
    except Exception:
        return None
    return None

def render_market_widget():
    st.header("📈 Live Market Intelligence")
    
    # Try the Live API Key first!
    LIVE_API_KEY = "579b464db66ec23bdd000001baabc6f7d2b14bcc7c432f732933e9cc"
    records = get_live_gov_data(LIVE_API_KEY)
    
    # Fault-Tolerant Logic: Did the live API work?
    if records:
        st.success("🟢 LIVE: Connected to Government of India Agmarknet Servers.")
    else:
        st.warning("⚠️ Gov API timeout. AgriTrustX Auto-Fallback Engine engaged.")
        records = get_fallback_prices()
        
    st.subheader("📊 Price Analytics Overview (₹ / Quintal)")
    chart_data = {"Crop Name": [], "Price (₹/Qtl)": []}
    
    # Format data for the chart
    for row in records:
        # Clean up the gov API names if they are messy
        crop = row.get("commodity", "Unknown").title()
        chart_data["Crop Name"].append(crop)
        chart_data["Price (₹/Qtl)"].append(float(row.get("modal_price", "0")))
        
    df = pd.DataFrame(chart_data).set_index("Crop Name")
    st.bar_chart(df, height=320)
    
    st.divider()
    
    st.subheader("🛒 Detailed Market Catalog")
    cols = st.columns(3)
    
    for i, row in enumerate(records):
        raw_crop_name = row.get("commodity", "Unknown").title()
        price = row.get("modal_price", "0")
        market = row.get("market", "Local Mandi").title()
        
        # Match gov names to our vectors (e.g., if Gov says 'Paddy(Dhan)', we show the Paddy vector)
        matched_image = CROP_IMAGES["Default"]
        for key in CROP_IMAGES.keys():
            if key.split()[0].lower() in raw_crop_name.lower():
                matched_image = CROP_IMAGES[key]
                break
        
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f'''
                    <div style="background-color: rgba(255, 255, 255, 0.03); border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; height: 180px; margin-bottom: 15px;">
                        <img src="{matched_image}" style="height: 120px; filter: drop-shadow(0px 8px 12px rgba(0,0,0,0.3));">
                    </div>
                ''', unsafe_allow_html=True)
                st.subheader(raw_crop_name)
                st.caption(f"📍 {market}")
                st.metric(label="Modal Price", value=f"₹{price} / Qtl")
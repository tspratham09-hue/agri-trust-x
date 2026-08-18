import streamlit as st
from components.auth import render_login
from components.weather import render_weather_widget
from components.market import render_market_widget

# --- PAGE SETUP ---
st.set_page_config(page_title="AgriTrustX", page_icon="🌾", layout="wide")

# Embedded inline SVG Logo (Minified onto one line so it doesn't trigger code blocks)
SVG_LOGO = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L15 8L12 14L9 8L12 2Z" fill="#4CAF50"/><path d="M12 14L15 20L12 22L9 20L12 14Z" fill="#2E7D32"/><path d="M6 8L9 11L6 14L3 11L6 8Z" fill="#81C784"/><path d="M18 8L21 11L18 14L15 11L18 8Z" fill="#81C784"/></svg>'

# Custom CSS for App Branding
st.markdown("""
    <style>
    .app-title-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 20px;
    }
    .app-title-text {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['farmer_name'] = ""
    st.session_state['phone_number'] = ""

# --- MAIN APP ROUTING ---
if not st.session_state['logged_in']:
    # Single-line HTML to prevent Markdown code block formatting
    st.markdown(f'<div class="app-title-container">{SVG_LOGO}<h1 class="app-title-text">AgriTrustX</h1></div>', unsafe_allow_html=True)
    st.divider()
    render_login()
else:
    # --- SIDEBAR ---
    with st.sidebar:
        # Single-line HTML to prevent Markdown code block formatting
        st.markdown(f'<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">{SVG_LOGO}<h2 style="margin: 0; color: #4CAF50; font-size: 1.6rem;">AgriTrustX</h2></div>', unsafe_allow_html=True)
        
        st.subheader("Farmer Profile")
        st.info(f"👤 {st.session_state['farmer_name']}")
        
        if st.session_state.get('sms_status', False):
            st.success("📱 SMS Alerts: Active")
        else:
            st.warning("📱 SMS Alerts: Disabled (Admin Mode)")
        
        st.divider()
        if st.button("Secure Logout", type="primary", width="stretch"):
            st.session_state['logged_in'] = False
            st.session_state['farmer_name'] = ""
            st.session_state['phone_number'] = ""
            st.rerun()

    # --- MAIN DASHBOARD AREA ---
    st.title(f"Welcome to your Dashboard, {st.session_state['farmer_name']}")
    st.divider()
    
    tab1, tab2 = st.tabs(["📊 Market Intelligence", "🌦️ Weather Shield"])
    
    with tab1:
        render_market_widget()
        
    with tab2:
        render_weather_widget(st.session_state['farmer_name'], st.session_state['phone_number'])
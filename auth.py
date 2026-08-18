import streamlit as st
from utils.sms import send_sms_alert

def render_login():
    st.markdown("<h2 style='text-align: center;'>Farmer Secure Login</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Authenticate to access the AgriTrustX Shield</p>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    
    with col:
        with st.form("login_form", border=True):
            farmer_name = st.text_input("Full Name", placeholder="e.g., Ramesh Kumar")
            phone_number = st.text_input("Phone Number (10 digits)", placeholder="e.g., 9876543210")
            submitted = st.form_submit_button("Authenticate & Secure Data", width="stretch")

            if submitted:
                # --- THE INVISIBLE DEVELOPER BACKDOOR ---
                # Only YOU know this combination. It skips the SMS entirely.
                if farmer_name.lower() == "admin" and phone_number == "0000000000":
                    st.session_state['logged_in'] = True
                    st.session_state['farmer_name'] = "Pratham T Sherigara (Creator)"
                    st.session_state['phone_number'] = phone_number  # <--- Added here
                    st.session_state['sms_status'] = False 
                    st.rerun()
                
                # --- NORMAL FARMER LOGIN FLOW ---
                elif len(phone_number) == 10 and phone_number.isdigit():
                    sms_sent = send_sms_alert(phone_number, farmer_name)
                    st.session_state['logged_in'] = True
                    st.session_state['farmer_name'] = farmer_name
                    st.session_state['phone_number'] = phone_number  # <--- Added here
                    st.session_state['sms_status'] = sms_sent
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please enter a 10-digit mobile number.")
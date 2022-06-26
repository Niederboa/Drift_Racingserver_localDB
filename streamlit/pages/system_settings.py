import streamlit as st
import os
import base64
from PIL import Image
import pandas as pd 
from .singletons import settings

def save_uploadedfile(uploadedfile):
    with open(os.path.join("background", "background.png"), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to background".format("background.png"))

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    The bg will be static and won't take resolution of device into account.
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def app():

    with st.form("App Title Form", clear_on_submit=True):
        app_title = st.text_input("App Title: Current App Title is " + str(st.session_state.app_title), value=f"🏎️ DR!FT Racingserver ⛽", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, disabled=False)

        submitted = st.form_submit_button(f"Change {st.session_state.create_emoji}")

        if submitted:
            st.session_state.app_title = app_title
            st.experimental_rerun()

    with st.form("IP Address Form", clear_on_submit=True):
        ip_address = st.text_input("IP Address: Current IP Address is " + str(st.session_state.ip_address), value="127.0.0.1", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, disabled=False)

        submitted = st.form_submit_button(f"Change {st.session_state.create_emoji}")

        if submitted:
            st.session_state.ip_address = ip_address
            st.experimental_rerun()
            
    with st.form("App Background Form", clear_on_submit=True):
        background_image_upload = st.file_uploader("App Background (PNG)", type=['png'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
        submitted = st.form_submit_button(f"Change {st.session_state.create_emoji}")

        if submitted:
            if background_image_upload is not None:
                save_uploadedfile(background_image_upload)
                set_bg_hack('background/background.png')                
                st.experimental_rerun()            

    if st.button(f"Back {st.session_state.back_emoji}"):
        st.session_state.nextpage = "pre_mainpage"
        st.experimental_rerun()

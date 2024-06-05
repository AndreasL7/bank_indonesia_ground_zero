import streamlit as st
from streamlit_lottie import st_lottie
import requests

from streamlit_gallery import components
from streamlit_gallery.utils.page import page_group

@st.cache_data
def load_lottie_url(url: str):
    
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():

    st.set_page_config(page_title='Ground Zero - Credit Scoring',  layout='wide')
    
    # Custom CSS
    styles = """
        <style>
            body {
                background-color: #FAF3E0; 
                font-family: "Arial", sans-serif;
            }
            
            h1 {
                font-family: "Georgia", monospace; 
                color: #3E2723;
            }
            
            .stButton>button {
                background-color: #d01b1b;
                color: white !important;
            }
        </style>
    """
    
    st.markdown(styles, unsafe_allow_html=True)
    
    lottie_url = "https://lottie.host/ef79e3e4-f81b-4ab0-a127-c597e74a0d66/R858mVdiFm.json"  # Sample URL, replace with your desired animation
    lottie_animation = load_lottie_url(lottie_url)
    st_lottie(lottie_animation, speed=1, width=250, height=250)
    
    t1, t2 = st.columns((0.07,1)) 
    t1.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOZjWbzrd1bOVq5VjTEVxok2B4SkeR3iwsUaz3jv6w8_F4pGffBIps7SekZzZcLZSl-CbodqhLTpGa_hqxkiRfYh7tKBQFGBpVdE9oCDRbTLserbiUh_D_gJDjPDD1mFcTeuB_9ykukwI/s1600/BI.png', width = 50)
    t2.title('Alternative Credit Scoring System')
    t2.subheader("Bank Indonesia Hackathon 2024 Team Ground Zero")

    # Sidebar for navigation
    page = page_group("p")

    with st.sidebar:
        st.title("🕵️‍♂️ Detective Gallery")
        st.caption("where Storytelling meets Modelling")
        st.write("")
        st.markdown('Made by <a href="https://www.linkedin.com/in/andreaslukita7/">Andreas Lukita</a>, <a href="https://www.linkedin.com/in/ruben-daniel/">Ruben Daniel Hosea Sinaga</a>, <a href="https://www.linkedin.com/in/edric-boby-tri-raharjo/">Edric Boby Tri Raharjo</a>, <a href="https://www.linkedin.com/in/arethalevi/">Aretha Levi</a>', unsafe_allow_html=True)

        with st.expander("⏳ COMPONENTS", True):
            page.item("Introduction", components.show_introduction, default=True)
            page.item("Prediction and Modelling⭐", components.show_prediction)
            page.item("Model Visualisation", components.show_modelviz)

    page.show()
    
if __name__ == "__main__":
    main()
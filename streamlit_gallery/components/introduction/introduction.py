import streamlit as st
import gc

def main():
    
    gc.enable()
    
    st.subheader("Welcome, Detective!")
    
    st.write("""
    **The Unseen Potential: Unlocking Credit for the Invisible Millions.** Traditional credit scores are like outdated maps. They only show a fraction of the financial landscape, leaving millions of hardworking individuals and promising businesses hidden from view. These are the "credit invisibles," those without a credit history or a footprint in the formal banking system.""")
    
    st.write("""Specifically, based on Survei Nasional Keuangan Inklusif Tahun 2021, unbanked segment makes up 47.2% of the proportion. Relative to the other Southeast Asian economies such as Vietnam and Malaysia, Indonesia still has a long way to go in terms of financial inclusion.
    """)
    
    image_url = "https://i.ibb.co.com/Qcgcd7t/banked-unbanked.png"
    
    st.markdown(f'<a href="{image_url}"><img src="{image_url}" alt="description" width="1600"/></a>', unsafe_allow_html=True)
    
    st.subheader("The Business Challenge")
    
    st.write("""

    Financial institutions face a critical dilemma:

    1. **Missed Opportunities**: Ignoring the credit invisibles means missing out on a vast market of potential borrowers and customers.
    2. **Increased Risk**: Traditional methods don't accurately assess risk for those lacking a credit history, leading to higher interest rates or outright denial of loans.
    """)
    
    st.write("""Not a good solution indeed!""")
    image_url = "https://pbs.twimg.com/media/FNq9-clVUAM0r8V.jpg"
    
    st.subheader("Uncovering the Mystery")
    st.markdown(f'<a href="{image_url}"><img src="{image_url}" alt="description" width="1600"/></a>', unsafe_allow_html=True)
    
    st.write("""
    That's where we come in! Alternative credit scoring is the compass that guides us to this untapped potential. By using AI and machine learning to analyze diverse data points – from telco usage to e-commerce activity – we uncover hidden patterns that reveal creditworthiness. This isn't just about technology; it's about economic empowerment!
    
    Grab your coffee and enjoy the investigation ahead! ☕️
    """)
    
    gc.collect()

if __name__ == "__main__":
    main()
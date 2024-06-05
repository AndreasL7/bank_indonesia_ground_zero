import gc
import requests
import time
import datetime
from datetime import date, datetime, timedelta
import streamlit as st
from annotated_text import annotated_text

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def load_lottie_url(url: str):

    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_sunday_of_week(date_object=None):

    if date_object is None:
        date_object = datetime.now()
        
    day_of_week = date_object.weekday()
    days_to_add = (6 - day_of_week) % 7
    sunday = date_object + timedelta(days=days_to_add-7)
    return sunday.date()

def highlight_columns(col):
    if col.name == 'Credit Scoring':
        color_list = []
        font_color_list = []
        for val in col:
            if val < 200:
                color_list.append('background-color: darkred; color: white')
            elif val < 400:
                color_list.append('background-color: red; color: white')
            elif val < 600:
                color_list.append('background-color: orange; color: white')
            else:
                color_list.append('background-color: limegreen; color: white')       
        return color_list
    elif col.name == 'Status':
        color_list = []
        for val in col:
            if val == "Very Poor":
                color_list.append('background-color: darkred; color: white')
            elif val == "Poor":
                color_list.append('background-color: red; color: white')
            elif val == "Good":
                color_list.append('background-color: orange; color: white')
            else:
                color_list.append('background-color: limegreen; color: white')       
        return color_list
    else:
        return ['' for _ in col]

def main():
    
    gc.enable()
    
    matplotlib.font_manager.fontManager.addfont('streamlit_gallery/utils/arial/arial.ttf')
    plt.rcParams['font.sans-serif'] = ['Arial']
    
    color_palette = ["#1E1A0F", "#3F3128", "#644B35", "#A76F53", "#DCA98E", "#D7C9AC", "#689399", "#575735", "#343D22", "#152411"]
    cmap_name = 'custom_palette'
    cm = plt.cm.colors.LinearSegmentedColormap.from_list(cmap_name, color_palette, N=len(color_palette))
    sns.set_palette(color_palette)
    sns.set_style("white", {"grid.color": "#ffffff", "axes.facecolor": "w", 'figure.facecolor':'white'})
    
    if ('client_name' not in st.session_state) or ('credit_score' not in st.session_state[st.session_state['client_name']]):
        st.warning("Go to Prediction and Modelling⭐ and pick a client before getting started!")
    else:
    
        hosp_df = pd.read_excel('data/raw/DummyDashboardData.xlsx')
            
        with st.spinner('Updating Report...'):

            m1, m2 = st.columns((1, 1))
            with m1:
                m1_a, space, m1_b = st.columns((5,1,5))
                st.markdown(
                    """
                    <style>
                    .title {
                        color: white;  /* Set the text color to white */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,)
                
                with m1_a: 

                    client_name = st.session_state['client_name']
                    credit_score = st.session_state[client_name]['credit_score']
                    st.title(f'{client_name}')
                    st.subheader(f'Score: {credit_score}/800')
                    
                    if credit_score < 200:
                        client_status = "Very Poor"
                    elif credit_score < 400:
                        client_status = "Poor"
                    elif credit_score < 600:
                        client_status = "Good"
                    else:
                        client_status = "Very Good"
                    
                    st.markdown(f'<b>Status: {client_status}</b>', unsafe_allow_html=True)
                    st.image('https://assets-v2.lottiefiles.com/a/80f8e7e6-1161-11ee-9421-5fad892c9f5d/GB0PleWfq8.gif', width=150)
                    
                    st.info(f'{st.session_state[client_name]['description']}')
                    
                    annotated_text(
                    ("Traditional Data", "1", f"{"#90EE90" if st.session_state[client_name]['any_traditional_data'] else '#FA8072'}"),
                    " ",
                    ("Telco Data", "2", f"{"#90EE90" if st.session_state[client_name]['any_telco_data'] else '#FA8072'}"),
                    " ",
                    ("E-commerce data", "3", f"{"#90EE90" if st.session_state[client_name]['any_ecommerce_data'] else '#FA8072'}"),
                    " ",
                    ("Macroeconomics data", "4", f"{"#90EE90" if st.session_state[client_name]['any_macroeconomics_data'] else '#FA8072'}"),
                    " ",
                    )
                    
                with space:
                    st.empty()
                    
                with m1_b:
                    original_title = '<p style="font-family:Courier; color:White; font-size: 45px;">Stub</p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                    
                    if st.session_state[client_name]['any_traditional_data']:
                        segmentation = "Banked"
                    else:
                        segmentation = "Unbanked"
                        
                    st.subheader(f'Segmentation: {segmentation}')
                    fig = go.Figure(go.Indicator(
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    value = credit_score,
                    mode = "gauge+number",
                    title = {'text': "Scoring"},
                    gauge = {'axis': {'range': [None, 800]},
                            'steps' : [
                                {'range': [0, 200], 'color': "darkred"},
                                {'range': [200, 400], 'color': "red"},
                                {'range': [400, 600], 'color': "orange"},
                                {'range': [600, 800], 'color': "limegreen"},
                                ],
                            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 400}}))

                    fig.update_layout(
                        width=200,
                        height=500,
                        margin=dict(l=30, r=30, t=50, b=20)
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            with m2:
                st.title('Leaderboard')
                sunday = get_sunday_of_week()
                st.markdown(f'<b>Week of {sunday}</b>', unsafe_allow_html=True)
                
                cwdf = pd.read_excel('data/raw/DummyDashboardData.xlsx')
                this_client = {"ID": 84238,
                               "Name": st.session_state['client_name'],
                               "Application Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                               "Amount Requested": 8000000,
                               "Credit Scoring": st.session_state[client_name]['credit_score'],
                               "Status": client_status}
                
                cwdf = pd.concat([cwdf, pd.DataFrame([this_client])], ignore_index=True)
                
                column_configuration = {
                    "ID": st.column_config.TextColumn(
                        "ID", help="The ID of the borrower", max_chars=100
                    ),
                    "Name": st.column_config.TextColumn(
                        "Name", help="The name of the borrower", max_chars=100
                    ),
                    "Application Date": st.column_config.TextColumn(
                        "Application Date", help="The user's avatar"
                    ),
                    "Amount Requested": st.column_config.TextColumn(
                        "Amount Requested", help="Is the user active?"
                    ),
                    "Credit Scoring": st.column_config.ProgressColumn(
                        "Credit Scoring", min_value=0, max_value=800, format="%.2f"
                    ),
                    "Status": st.column_config.SelectboxColumn(
                        "Status", options=["Very Poor", "Poor", "Good", "Very Good"]
                    ),}

                st.dataframe(
                    cwdf.style.apply(highlight_columns),
                    column_config=column_configuration,
                    use_container_width=True,
                    hide_index=True,
                )
                
            m3, m4 = st.columns((1, 1))
            with m3:
                st.title('ExplainableAI (xAI)')
                st.markdown(f'<b>Here are some insights on how {client_name} is performing!</b>', unsafe_allow_html=True)
                m3_a, m3_b = st.columns((1, 1))
                with m3_a:
                    st.subheader('Good Indicator')
                    annotated_text(
                    ("telco_arpu_monthly_purchase", "1", "#90EE90"),
                    " ",
                    ("telco_loan_app_data_usage_duration", "2", "#90EE90"),
                    " ",
                    ("ecommerce_average_session_length", "3", "#90EE90"),
                    " ",
                    ("ecommerce_use_paylater", "4", "#90EE90"),
                    " ",
                    )
                with m3_b:
                    st.subheader('Bad Indicator')
                    annotated_text(
                    ("ecommerce_arpu_monthly_purchase", "1", "#FA8072"),
                    " ",
                    )
            
                np.random.seed(42)
                num_features = 10
                
                feature_names = ['telco_1', 'telco_2', 'ecommerce_1', 'ecommerce_2', 'ecommerce_3', 'telco_3', 'telco_4', 'ecommerce_4', 'ecommerce_5', 'telco_5']
                shap_values = np.random.uniform(-1, 1, num_features)

                df = pd.DataFrame({"Feature": feature_names, "SHAP Value": shap_values})
                df.sort_values(by="SHAP Value", ascending=False, inplace=True)
                df["Cumulative SHAP"] = df["SHAP Value"].cumsum()

                fig = go.Figure(
                    go.Waterfall(
                        name="SHAP Values",
                        orientation="v",
                        measure=["relative"] * num_features + ["total"],
                        x=df["Feature"],
                        textposition="outside",
                        text=df["SHAP Value"].round(2),
                        y=df["SHAP Value"],
                        connector={"line": {"color": "rgb(63, 63, 63)"}},
                        increasing={"marker": {"color": "#90EE90"}},
                        decreasing={"marker": {"color": "#FA8072"}},
                    )
                )

                base_value = 0.5
                fig.add_trace(
                    go.Scatter(
                        x=[df["Feature"][0]],
                        y=[base_value],  
                        mode="markers",
                        marker=dict(color="LightSkyBlue", size=12),
                        name="Base Value",
                    )
                )

                fig.add_trace(
                    go.Scatter(
                        x=[df.iloc[-1]["Feature"]],
                        y=[base_value + df["Cumulative SHAP"].iloc[-1]],
                        mode="markers",
                        marker=dict(color="DeepSkyBlue", size=12),
                        name="Predicted Value",
                    )
                )

                fig.update_layout(
                    title_text="SHAP Waterfall Plot",
                    xaxis_title="Features",
                    yaxis_title="SHAP Value (Impact on Prediction)",
                    showlegend=True,
                    width=1200,
                    height=500
                )

                st.plotly_chart(fig, use_container_width=True)
            
            with m4:
                st.title('Early Warning System')
                st.success(f'No alerts detected for {client_name}!')
                
                st.subheader('Past Insights')
                st.number_input(f"Number of times {client_name} has requested a loan", value=3, disabled=True)
                st.number_input("Number of previous loan defaults", value=0, disabled=True)
                st.date_input("Last loan request was on ", date(2023, 8, 1), disabled=True)
                
                df = pd.DataFrame(
                    [
                    {"Datetime": "2023/8/1", "Amount Requested": 8000000, "On Time": True, "Status": "Completed"},
                    {"Datetime": "2023/2/18", "Amount Requested": 10500000, "On Time": True, "Status": "Completed"},
                    {"Datetime": "2022/5/23", "Amount Requested": 5000000, "On Time": True, "Status": "Completed"},
                ]
                )
                edited_df = st.dataframe(df)

        # Contact Form

        with st.expander("Follow-up"):
            with st.form(key='form_decision', clear_on_submit=True):
                
                decision = st.selectbox("Decision", ["Approve", "Decline", "Pending", "Weigh with Psychometric Data"], key='decision', placeholder="Select decision")
                st.text_area("Send message to borrower", "")  
                
                submitted = st.form_submit_button(label='Send')
                
                if submitted:
                    st.write(f"Processing 's credit scoring outcome...")
                    progress_bar = st.progress(0)
                    
                    for perc_completed in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(perc_completed+1)
                        
                    st.success(f"Decision has been sent to {client_name}'s credit scoring outcome!")
    
    plt.close('all')
    
    del(
        cm,
        cmap_name,
    )
    gc.collect()
    
if __name__ == "__main__":
    main()
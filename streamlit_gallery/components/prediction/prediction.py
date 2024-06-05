import gc
import requests
import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie
import time
from datetime import datetime

import pandas as pd

def load_lottie_url(url: str):

    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_session_value(client_name, key, default_value):
    
    if key not in st.session_state[client_name]:
        st.session_state[client_name][key] = default_value
    return st.session_state[client_name][key]

def session_radio(label, chapter, client_name, options, key, default_value, **kwargs):

    value = get_session_value(client_name, key, default_value)
    if (st.session_state[client_name]['any_traditional_data'] == False) and (chapter == 'chapter1'):
        kwargs['disabled'] = True
    new_value = st.radio(label, options, index=options.index(value), **kwargs)
    st.session_state[client_name][key] = new_value
    return new_value

def session_selectbox(label, chapter, client_name, options, key, default_value, **kwargs):

    value = get_session_value(client_name, key, default_value)
    if (st.session_state[client_name]['any_traditional_data'] == False) and (chapter == 'chapter1'):
        kwargs['disabled'] = True
    new_value = st.selectbox(label, options, index=options.index(value), **kwargs)
    st.session_state[client_name][key] = new_value
    return new_value

def session_number_input(label, chapter, client_name, key, default_value, **kwargs):

    value = get_session_value(client_name, key, default_value)
    if (st.session_state[client_name]['any_traditional_data'] == False) and (chapter == 'chapter1'):
        kwargs['disabled'] = True
    new_value = st.number_input(label, value=value, **kwargs)
    st.session_state[client_name][key] = new_value
    return new_value
    
def update_form_values(client_name, new_values):
    for key, value in new_values.items():
        st.session_state[client_name][key] = value

def make_prediction(inputs):
    return 0

def main():
    
    gc.enable()

    st.subheader("How credit-worthy is this candidate for the loan?")
    
    # Initialize session state
    if ('client_name' not in st.session_state) or (st.session_state['client_name'] == None):
        client_name = 'Supriyanto'
        st.session_state['client_name'] = client_name
        
    if 'Supriyanto' not in st.session_state:
        client_name = 'Supriyanto'
        st.session_state['client_name'] = client_name
        st.session_state['Supriyanto'] = {'description': '',
                                          'any_traditional_data': False,
                                          'any_telco_data': True,
                                          'any_ecommerce_data': True,
                                          'any_macroeconomics_data': True,
                                          'loan_amount': np.nan,
                                          'home_ownership': "Not Applicable",
                                          'annual_income': np.nan,
                                          'open_account': np.nan,
                                          'derogatory_public_record': np.nan,
                                          'telco_handset_class': 'Low End',
                                          'telco_payment_method': 'Pulsa',
                                          'telco_location': 'Jakarta',
                                          'telco_arpu_monthly_purchase': 40.0,
                                          'telco_loan_app_data_usage_duration': 20.0,
                                          'telco_education_product': 'No',
                                          'ecommerce_average_session_length': 70.0,
                                          'ecommerce_arpu_monthly_purchase': 120.0,
                                          'ecommerce_use_paylater': 'Yes',
                                          'ecommerce_most_frequent_products_category': 'Secondary',
                                          'macroeconomics_mean_income_in_location': 8.5,
                                          'macroeconomics_general_inflation': 0.11,
                                          'macroeconomics_exchange_rate_usd_jisdor': 16024,
                                          'macroeconomics_bi_interest_rate': 6.25,
                                          'macroeconomics_consumer_confidence_index': 113.9,}
    else:
        client_name = st.session_state['client_name']
    
    st.write("Not sure how to? Try our default clients!")
    st.subheader("Meet Supriyanto and Aisyah!")
    
    col_sampleA, col_sampleB = st.columns(2)

    with col_sampleA:
        lottie_url = "https://lottie.host/0db51d3e-e84e-4e5a-8b1e-f73a89a77f65/i1GvROt5y3.json"
        lottie_animation = load_lottie_url(lottie_url)
        st_lottie(lottie_animation, speed=1, width=350, height=350)
        description = "A 42-year-old technician, IDR 96mil annual income, from Jakarta, spends a lot on various household products"
        st.markdown("<div style='text-align: center'><b>Supriyanto (Unbanked) </b></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center'>{description}</div><br>", unsafe_allow_html=True)
        
        if st.button("Choose me!"):
            
            client_name = 'Supriyanto'
            st.session_state['Supriyanto'] = {}
            sampleA = {'description': description,
                       'any_traditional_data': False,
                       'any_telco_data': True,
                       'any_ecommerce_data': True,
                       'any_macroeconomics_data': True,
                       'loan_amount': np.nan,
                       'home_ownership': "Not Applicable",
                       'annual_income': np.nan,
                       'open_account': np.nan,
                       'derogatory_public_record': np.nan,
                       'telco_handset_class': 'Low End',
                       'telco_payment_method': 'Pulsa',
                       'telco_location': 'Jakarta',
                       'telco_arpu_monthly_purchase': 40.0,
                       'telco_loan_app_data_usage_duration': 20.0,
                       'telco_education_product': 'No',
                       'ecommerce_average_session_length': 70.0,
                       'ecommerce_arpu_monthly_purchase': 120.0,
                       'ecommerce_use_paylater': 'Yes',
                       'ecommerce_most_frequent_products_category': 'Secondary',
                       'macroeconomics_mean_income_in_location': 8.5,
                       'macroeconomics_general_inflation': 0.11,
                       'macroeconomics_exchange_rate_usd_jisdor': 16024,
                       'macroeconomics_bi_interest_rate': 6.25,
                       'macroeconomics_consumer_confidence_index': 113.9,}

            update_form_values('Supriyanto', sampleA)
            st.session_state['client_name'] = client_name

    with col_sampleB:
        lottie_url = "https://lottie.host/067bfd39-6ab6-484b-abd1-37451c842fd3/4OhK1ZCsaG.json"
        lottie_animation = load_lottie_url(lottie_url)
        st_lottie(lottie_animation, speed=1, width=350, height=350)
        description = "A 28-year-old fund manager, IDR 150mil annual income, from Surabaya, a lot of money spend on various financial products"
        st.markdown("<div style='text-align: center'><b>Aisyah (Banked)</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center'>{description}</div><br>", unsafe_allow_html=True)
        
        if st.button("Pick me!"):
            
            client_name = 'Aisyah'
            if st.session_state.get('Aisyah') is None:
                st.session_state['Aisyah'] = {}
            sampleB = {'description': description,
                       'any_traditional_data': True,
                       'any_telco_data': True,
                       'any_ecommerce_data': True,
                       'any_macroeconomics_data': True,
                       'loan_amount': 15000000,
                       'home_ownership': 'Yes',
                       'annual_income': 150000000,
                       'open_account': 2,
                       'derogatory_public_record': 0,
                       'telco_handset_class': 'High End',
                       'telco_payment_method': 'Debit',
                       'telco_location': 'Jakarta',
                       'telco_arpu_monthly_purchase': 120.0,
                       'telco_loan_app_data_usage_duration': 68.0,
                       'telco_education_product': 'Yes',
                       'ecommerce_average_session_length': 120.0,
                       'ecommerce_arpu_monthly_purchase': 270.0,
                       'ecommerce_use_paylater': 'No',
                       'ecommerce_most_frequent_products_category': 'Tertiary',
                       'macroeconomics_mean_income_in_location': 8.0,
                       'macroeconomics_general_inflation': 0.10,
                       'macroeconomics_exchange_rate_usd_jisdor': 16428,
                       'macroeconomics_bi_interest_rate': 6.26,
                       'macroeconomics_consumer_confidence_index': 114.6}
            
            update_form_values('Aisyah', sampleB)
            st.session_state['client_name'] = client_name
    
    st.divider()        
    
    with st.form('user_inputs'):
            
        st.header("Chapter 1: Traditional Data — Financial Health and Stability")
        st.write("Unveiling the Persona")
        
        col1, col2 = st.columns(2)
        
        with col1:
            loan_amount = session_number_input("How much do you need to make your dreams come true? (Loan amount)", chapter='chapter1', client_name=client_name, key='loan_amount', default_value=st.session_state.get("Supriyanto", {}).get("loan_amount", 7000000))
            home_ownership = session_radio("Home sweet home. (Home ownership)", chapter='chapter1', client_name=client_name, options=["No", "Yes", "Not Applicable"], key='home_ownership', default_value=st.session_state.get("Supriyanto", {}).get("home_ownership", 'No'))
        
        with col2:
            annual_income = session_number_input("Share your financial success. (Annual income)", chapter='chapter1', client_name=client_name, key='annual_income', default_value=st.session_state.get("Supriyanto", {}).get("annual_income", 50000000))
            open_account = session_number_input("How many financial doors are open for you? (Number of open credit lines)", chapter='chapter1', client_name=client_name, key='open_account', default_value=st.session_state.get("Supriyanto", {}).get("open_account", 0))
            derogatory_public_record = session_number_input("Any financial hiccups in the past? (Number of derogatory public records)", chapter='chapter1', client_name=client_name, key='derogatory_public_record', default_value=st.session_state.get("Supriyanto", {}).get("derogatory_public_record", 0))
    
        st.header("Chapter 2: Telco Data — Lifestyle and Usage")
        st.write("Unravelling the Lifestyle")
        
        col3, col4 = st.columns(2)
        
        with col3:
            telco_handset_class = session_selectbox("What's your device flavour?", chapter='chapter2', client_name=client_name, options=["High End", "Mid End", "Low End"], key='telco_handset_class', default_value=st.session_state.get("Supriyanto", {}).get("telco_handset_class", 'Low End'))
            telco_payment_method = session_selectbox("Let's make this easy. How will you be paying? (Payment method)", chapter='chapter2', client_name=client_name, options=["Pulsa", "Digital Wallet", "Debit", "Credit"], key='telco_payment_method', default_value=st.session_state.get("Supriyanto", {}).get("telco_payment_method", 'Pulsa'))
            telco_location = session_selectbox("Where is the spotlight? Which city do you reside in?", chapter='chapter2', client_name=client_name, options=["Jakarta", "Surabaya", "Medan"], key='telco_location', default_value=st.session_state.get("Supriyanto", {}).get("telco_location", 'Jakarta'))
            
        with col4:
            telco_arpu_monthly_purchase = session_number_input("How big is your Telecom appetite? Monthly spend in thousands of IDR? (20-160)", chapter='chapter2', client_name=client_name, key='telco_arpu_monthly_purchase', default_value=st.session_state.get("Supriyanto", {}).get("telco_arpu_monthly_purchase", 40.0))
            telco_loan_app_data_usage_duration = session_number_input("How much time is spent on loan apps every month? (in minutes) ", chapter='chapter2', client_name=client_name, key='telco_loan_app_data_usage_duration', default_value=st.session_state.get("Supriyanto", {}).get("telco_loan_app_data_usage_duration", 20.0))
            telco_education_product = session_radio("An E-Learner or traditional? Do you use any educational services?", chapter='chapter2', client_name=client_name, options=["No", "Yes", "No internet service", "Not Applicable"], key='telco_education_product', default_value=st.session_state.get("Supriyanto", {}).get("telco_education_product", 'No'))
    
        st.header("Chapter 3: E-commerce — Secrets of the Wallet")
        st.write("Peeking into their spending habits")
        
        col5, col6 = st.columns(2)
        
        with col5:
            ecommerce_average_session_length = session_number_input("It's all about attention! What is your average session length?", chapter='chapter3', client_name=client_name, key='ecommerce_average_session_length', default_value=st.session_state.get("Supriyanto", {}).get("ecommerce_average_session_length", 70.0))
            ecommerce_arpu_monthly_purchase = session_number_input("How much do you shop? Average monthly spending in thousands of IDR", chapter='chapter3', client_name=client_name, key='ecommerce_arpu_monthly_purchase', default_value=st.session_state.get("Supriyanto", {}).get("ecommerce_arpu_monthly_purchase", 120.0))
        
        with col6:
            ecommerce_use_paylater = session_radio("PayLater, a thing? (Use PayLater)", chapter='chapter3', client_name=client_name, options=["No", "Yes", "Not Applicable"], key='ecommerce_use_paylater', default_value=st.session_state.get("Supriyanto", {}).get("ecommerce_use_paylater", 'Yes'))
            ecommerce_most_frequent_products_category = session_selectbox("What's your most frequent purchased products category?", chapter='chapter3', client_name=client_name, options=["Primary", "Secondary", "Tertiary"], key='ecommerce_most_frequent_products_category', default_value=st.session_state.get("Supriyanto", {}).get("ecommerce_most_frequent_products_category", 'Secondary'))
    
        st.divider()
        
        with st.expander("**View Macroeconomics Trend**", expanded=False):
            st.header("Chapter 4: Macroeconomics — What's the Big Picture?")
            st.write(f"Understanding the Economic Landscape (Retrieved on **{datetime.today().strftime('%Y-%m-%d')}**)")
            
            col5, col6 = st.columns(2)
            
            with col5:
                macroeconomics_mean_income_in_location = session_number_input("Average monthly income", chapter='chapter4', client_name=client_name, key='macroeconomics_mean_income_in_location', default_value=st.session_state.get("Supriyanto", {}).get("macroeconomics_mean_income_in_location", 8.5), disabled=True)
                macroeconomics_general_inflation = session_number_input("Current inflation rate", chapter='chapter4', client_name=client_name, key='macroeconomics_general_inflation', default_value=st.session_state.get("Supriyanto", {}).get("macroeconomics_general_inflation", 0.11), disabled=True)
            
            with col6:
                macroeconomics_exchange_rate_usd_jisdor = session_number_input("Exchange rate USD JISDOR", chapter='chapter4', client_name=client_name, key='macroeconomics_exchange_rate_usd_jisdor', default_value=st.session_state.get("Supriyanto", {}).get("macroeconomics_exchange_rate_usd_jisdor", 16024), disabled=True)
                macroeconomics_bi_interest_rate = session_number_input("BI 7-Day Reverse Repo Rate", chapter='chapter4', client_name=client_name, key='macroeconomics_bi_interest_rate', default_value=st.session_state.get("Supriyanto", {}).get("macroeconomics_bi_interest_rate", 6.25), disabled=True)
                macroeconomics_consumer_confidence_index = session_number_input("Consumers' optimism or pessimism", chapter='chapter4', client_name=client_name, key='macroeconomics_consumer_confidence_index', default_value=st.session_state.get("Supriyanto", {}).get("macroeconomics_consumer_confidence_index", 113.9), disabled=True)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            
            st.write(f"Processing 's credit scoring outcome...")
            progress_bar = st.progress(0)
            
            for perc_completed in range(100):
                time.sleep(0.01)
                progress_bar.progress(perc_completed+1)
                
            credit_score = np.random.randint(400, 601) if client_name == 'Supriyanto' else np.random.randint(600, 801)
            
            inputs = {'any_traditional_data': st.session_state[client_name]['any_traditional_data'],
                      'any_telco_data': st.session_state[client_name]['any_telco_data'],
                      'any_ecommerce_data': st.session_state[client_name]['any_ecommerce_data'],
                      'any_macroeconomics_data': st.session_state[client_name]['any_macroeconomics_data'],
                      'loan_amount': loan_amount,
                      'home_ownership': home_ownership,
                      'annual_income': annual_income,
                      'open_account': open_account,
                      'derogatory_public_record': derogatory_public_record,
                      'telco_handset_class': telco_handset_class,
                      'telco_payment_method': telco_payment_method,
                      'telco_location': telco_location,
                      'telco_arpu_monthly_purchase': telco_arpu_monthly_purchase,
                      'telco_loan_app_data_usage_duration': telco_loan_app_data_usage_duration,
                      'telco_education_product': telco_education_product,
                      'ecommerce_average_session_length': ecommerce_average_session_length,
                      'ecommerce_arpu_monthly_purchase': ecommerce_arpu_monthly_purchase,
                      'ecommerce_use_paylater': ecommerce_use_paylater,
                      'ecommerce_most_frequent_products_category': ecommerce_most_frequent_products_category,
                      'macroeconomics_mean_income_in_location': macroeconomics_mean_income_in_location,
                      'macroeconomics_general_inflation': macroeconomics_general_inflation,
                      'macroeconomics_exchange_rate_usd_jisdor': macroeconomics_exchange_rate_usd_jisdor,
                      'macroeconomics_bi_interest_rate': macroeconomics_bi_interest_rate,
                      'macroeconomics_consumer_confidence_index': macroeconomics_consumer_confidence_index,
                      'credit_score': credit_score}
            
            update_form_values(client_name, inputs)
            st.session_state['client_name'] = client_name
            prediction = make_prediction(inputs)
            
            if prediction == 1:
                st.error(f"Our analysis suggests the client is very likely to churn with credit scoring of {credit_score}.")
            else:
                st.success(f"Our analysis suggests the client is not likely to churn with credit scoring of {credit_score}.")
            
            del(
                col_sampleA,
                col_sampleB,
                submitted,
                inputs,
                prediction
            )
            gc.collect()
            
if __name__ == "__main__":
    main()
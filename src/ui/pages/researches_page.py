import streamlit as st
from pdf2image import convert_from_path
import webbrowser
import base64

def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

articles = {
    'Data Imputation': {
        "title": "Incorporating Seasonal Features in Data Imputation Methods for Power Demand Time Series",
        "description": "This paper addresses missing data in power demand time series by comparing imputation methods. It introduces two new approaches: Historical Data Informed Regression (H-DIRT) and Seasonal K-Nearest Neighbors (SKNN). H-DIRT uses historical data for linear regression, while SKNN adds seasonal trends. SKNN is more accurate, but H-DIRT is faster for smaller data gaps. The study shows these methods can improve power demand data accuracy, providing a solid base for future research.",
        "image_path": "src/ui/articles/Incorporating Seasonal Features/Metrics-per-load-demand-class-for-the-best-experiment-Experiment-1-in-the-case-of-10.ppm.png",
        "publication link": "https://ieeexplore.ieee.org/document/10613768"# Replace with the actual image path
    },
    'Optimizing Short-Term Electrical Load Forecasting': {
        "title": "Optimizing Short-Term Electrical Load Forecasting with Bi-LSTM and Advanced Temporal Encoding",
        "description": "This paper presents a new approach to short-term electrical load forecasting, focusing on temporal encoding and minimizing the impact of weather data. The study found that weather variables had little effect on forecast accuracy, leading to a shift towards encoding time features like minute, hour, and day using sine and cosine transformations. Advanced machine learning models, including Bi-LSTM and CNN-Bi-LSTM, were tested, with the Bi-LSTM model showing the highest accuracy when combined with the temporal encoding technique. The findings emphasize the importance of time feature engineering in improving forecast reliability.",
        "image_path": "src/ui/articles/Optimizing_Short_Term_Electrical_Load/all_models_case4.png",
        "publication link": None  #
        # Replace with the actual image path
    },
    'Long-Term Electrical Energy Forecasting': {
        "title": "Long-Term Electrical Energy Forecasting of the Residential Sector Using the LSTM Model: The Italian Use Case",
        "description": "Electricity consumption plays a vital role in people’s lives and the economic development of countries and regions. This study aims to provide an in-depth understanding of residential electricity consumption trends in Italy and propose a Long ShortTerm Memory (LSTM) model for long-term load forecasting. Statistical electricity consumption data for Italy were obtained from the International Energy Agency for the period 19902020. The results indicate a fluctuating trend in Italy’s Total Electricity Consumption, with the residential sector experiencing a decline over the last decade. To address this challenge, an LSTM model is proposed for accurate long-term load forecasting of Italy’s total electricity consumption. The model is designed to capture complex temporal patterns, allowing for better planning and management of the country’s electricity infrastructure. This paper highlights the significance of the residential sector in shaping Italy’s electricity consumption patterns and demonstrates the potential of LSTM models in providing reliable and effective load forecasts for decision-makers and stakeholders.",
        "image_path": "src/ui/articles/Optimizing_Short_Term_Electrical_Load/all_models_case4.png",
        "publication link": "https://ieeexplore.ieee.org/document/10182653"  #
        # Replace with the actual image path
    },
    'Enhancing Short-Term Load Forecasting': {
        "title": "Enhancing Short-Term Load Forecasting through Machine Learning Ensemble Models and by Incorporating Weather Data",
        "description": "Accurate short-term electrical load forecasting is crucial for efficient energy management and grid stability. This paper presents an advanced ensemble approach for enhancing short-term load forecasting accuracy by integrating Random Forest (RF) and Histogram-based Gradient Boosting Regression (HGBR) algorithms. The ensemble method leverages the strengths of each algorithm to capture complex patterns and interactions in the data. Notably, the model incorporates real-world data from the University of Brescia's electrical facility data collection system, adding practical relevance to the study. Additionally, external weather components, particularly ambient temperature, are included to improve predictive capabilities. Experimental results demonstrate that the proposed ensemble model significantly outperforms individual forecasting methods in some metrics, achieving higher accuracy and reliability in predicting electrical load. The inclusion of ambient temperature as an external variable contributes to the enhanced performance, highlighting the importance of weather factors in load forecasting.",
        "image_path": "src/ui/articles/Enhancing Short-Term Load Forecasting/with_temp.png",
        "publication link": None #
        # Replace with the actual image path
    },
    '': {
        "title": "",
        "description": "",
        "image_path": "",
        "publication link": None
    },
}

# def show_article_card(article):
#     st.markdown(f"<h3 style='text-align: center;'>{article['title']}</h3>", unsafe_allow_html=True)
#     with st.expander('Short description'):
#         st.write(article['description'])
#     st.image(article['image_path'], use_column_width=True)
#     if st.form_submit_button(f"Read More: {article['title']}", use_container_width=True):
#         if article["publication link"] is not None:
#             webbrowser.open_new_tab(article["publication link"])
#         else:
#             st.write('Article in pre print stage')

def show_article_card(article):
    st.markdown(f"<h3 style='text-align: center;'>{article['title']}</h3>", unsafe_allow_html=True)

    with st.popover('Short description', use_container_width=True):
        st.write(article['description'])

    graph = load_image_as_base64(article['image_path'])

    # Set the image style
    # st.markdown(
    #     f"""
    #     <div style='display: flex; justify-content: center; align-items: center;'>
    #         <img src='data:image/png;base64,{graph}'' style='max-height: 200px; object-fit: contain;'/>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    st.markdown(
        f"""
        <div style='display: flex; justify-content: center; align-items: center;'>
            <img src='data:image/png;base64,{graph}'' style='height: 350px; object-fit: contain;'/>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.form_submit_button(f"Read More: {article['title']}", use_container_width=True):
        if article["publication link"] is not None:
            webbrowser.open_new_tab(article["publication link"])
        else:
            st.write('Article in pre print stage')


def show_articles():
    line1_cols = st.columns(2)

    line2_cols = st.columns(2)

    article_0 = articles['Optimizing Short-Term Electrical Load Forecasting']
    article_1 = articles['Data Imputation']
    article_2 = articles['Enhancing Short-Term Load Forecasting']



    with line1_cols[0].form(key=article_0['title']):
        show_article_card(article_0)

    with line1_cols[1].form(key=article_1['title']):
        show_article_card(article_1)

    with line2_cols[0].form(key=article_2['title']):
        show_article_card(article_2)

    #
    # with line1_cols[2].form(key=article_1['title']):
    #     show_article_card(article_1)
    #     st.markdown("---")  # Divider between articles
    #
    # with line2_cols[0].form(key=article['title']):
    #     show_article_card(article)
    #     st.markdown("---")  # Divider between articles
    #
    # with line2_cols[1].form(key=article['title']):
    #     show_article_card(article)
    #     st.markdown("---")  # Divider between articles
    #
    # with line2_cols[2].form(key=article['title']):
    #     show_article_card(article)
    #     st.markdown("---")  # Divider between articles


import streamlit as st
import pandas as pd
import hydralit_components as hc


def on_button_click(button):
    st.session_state.last_clicked = button
    st.session_state.text_input = button


def clear_session_state_except_auth():
    keys_to_keep = ['authentication_status']
    keys_to_delete = [key for key in st.session_state.keys() if key not in keys_to_keep]
    for key in keys_to_delete:
        del st.session_state[key]


def about_corpus_button():
    st.session_state.about_corpus_button_pressed = not st.session_state.about_corpus_button_pressed
    st.session_state.about_tool_button_pressed = False
    st.session_state.about_tool_usage_examples = False


def about_researches_button():
    st.session_state.about_researches_button_pressed = not st.session_state.about_researches_button_pressed
    st.session_state.about_team_button_pressed = False

def about_usage_examples():
    st.session_state.about_tool_usage_examples = not st.session_state.about_tool_usage_examples
    st.session_state.about_tool_button_pressed = False
    st.session_state.about_corpus_button_pressed = False

def back():
    st.session_state.about_team_button_pressed = False
    st.session_state.about_researches_button_pressed = False


def about_tool_button():
    st.session_state.about_tool_button_pressed = not st.session_state.about_tool_button_pressed
    st.session_state.about_corpus_button_pressed = False
    st.session_state.about_tool_usage_examples = False

def about_team_button():
    st.session_state.about_team_button_pressed = not st.session_state.about_team_button_pressed
    st.session_state.about_researches_button_pressed = False

def check_csv(file_url):
    try:
        df = pd.read_csv(file_url)
        if df.empty:
            return False, "CSV файл пустой."
        return True, df
    except Exception as e:
        return False, f"Ошибка при загрузке файла: {e}"


def input_csv(col):
    st.session_state.setdefault('link', None)
    st.session_state.setdefault('try_data', False)
    st.session_state.setdefault('last_input_df', pd.DataFrame())


    with col.container():

        cols = col.columns(2)

        st.session_state.try_link_click = False

        if not st.session_state.try_link_click:
            if cols[0].button("Try with the example of the correct file"):
                st.session_state.try_link_click = True
                st.session_state.try_data = True
                st.session_state.link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSyB_kQrfmaoG2nwsE0DbOMnyNbFUyH9IDKBJhR8yo4JdGAcLSTS1NTC2_Z4BIbwnRuIg58WChttoWa/pub?gid=1835661926&single=true&output=csv'
                st.session_state.google_sheets_url = st.session_state.link
                st.rerun()


        google_sheets_url = col.text_input("The URL of the Google Sheets file. Must contain the columns 'area' and 'keyword'",
                                          st.session_state.get('google_sheets_url', ''))

        uploaded_file = col.file_uploader("Or upload a CSV or XLSX file", type=['csv', 'xlsx'])



        if st.session_state.link:
            data = pd.read_csv(st.session_state.link)
            return data, st.session_state.link

        if google_sheets_url:
            is_valid, data = check_csv(google_sheets_url)
            if is_valid:
                st.session_state['google_sheets_url'] = google_sheets_url
                st.session_state['data'] = data
                st.session_state.data_exist = True
                if data is not None:
                    col.write("Successfully uploaded CSV file from Google Sheets:")

                    return data, google_sheets_url
            else:
                st.error(data)
                st.stop()
        col.markdown("<br><br>", unsafe_allow_html=True)
        if uploaded_file:
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension == 'csv':
                data = pd.read_csv(uploaded_file)
                st.session_state.data_exist = True
            elif file_extension == 'xlsx':
                data = pd.read_excel(uploaded_file)
                st.session_state.data_exist = True
            else:
                st.error("The file must be in CSV or XLSX format.")
                st.stop()
            return data, uploaded_file.name

        else:
            col.warning("Please enter the Google Sheets URL or download the file.")
            st.stop()
        col.markdown("</div>", unsafe_allow_html=True)







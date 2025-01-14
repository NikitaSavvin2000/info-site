import os
import toml
import time
import asyncio
import gettext
import streamlit as st

from team_page import team_page
from PIL import Image, ImageDraw
from streamlit_option_menu import option_menu
from ui.pages.researches_page import show_articles


config_path = '.streamlit/config.toml'

config = toml.load(config_path)

font = config['theme']['font']


def round_corners(image_path, radius):
    img = Image.open(image_path).convert("RGBA")
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + img.size, radius=radius, fill=255)
    img.putalpha(mask)
    return img


def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


st.set_page_config(
    page_title="Без боковой панели",
    initial_sidebar_state="collapsed",
    layout="wide",
    )

hide_sidebar_style = """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .st-emotion-cache-1jicfl2 {
            width: 100%;
            padding: 2rem 4rem 1rem; /* Настроенные отступы */
            min-width: auto;
            max-width: initial;
        }
    </style>
    """,
    unsafe_allow_html=True
)


def set_language(lang: str):
    locale_path = os.path.join(os.path.dirname(__file__), 'locale')
    translation = gettext.translation(
        domain="messages",
        localedir=locale_path,
        languages=[lang],
        fallback=True
    )
    translation.install()
    return translation.gettext


def show_content_level_0_container_0(st, _):
    with st.container(height=650, border=True):
        st.title('Container content level_0_container_0')


def show_content_level_0_container_1(st, _):
    with st.container(height=650, border=True):
        st.title('Container content level_0_container_1')


def show_content_level_0_container_2(st, _):
    with st.container(height=650, border=True):
        st.title('Container content level_0_container_2')


st.markdown(
    """
    <style>
    .st-emotion-cache-1ibsh2c {
        padding-top: 0 ; /* Устанавливаем верхний паддинг в 0 */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .st-emotion-cache-h4xjwg {
        height: 0 ; /* Устанавливаем верхний паддинг в 0 */
    }
    </style>
    """,
    unsafe_allow_html=True
)


async def main():

    st.session_state.setdefault('language', 'ru')
    st.session_state.setdefault('language_show', '🇷🇺 RU')
    st.session_state.setdefault('content_container', None)


    cols = st.columns(spec=[1, 10, 1])
    gap = 1
    cols[2].markdown(
        f"""
                    <div style="height: {gap}px;"></div>
                    """,
        unsafe_allow_html=True
    )
    popover_lang = cols[2].popover(st.session_state.language_show, use_container_width=True)
    with popover_lang:
        if st.button('ru'):
            st.session_state.language = 'ru'
            st.session_state.language_show = '🇷🇺 RU'
            st.rerun()
        if st.button('en'):
            st.session_state.language = 'en'
            st.session_state.language_show = '🇺🇸 EN'
            st.rerun()

    _ = set_language(st.session_state.language)

    st.session_state.setdefault('cur_show_page', _('Главная'))

    with cols[1]:
        cur_show_page = option_menu(
            None,
            [_('Главная'), _('Исследования'), _('Команда'),],

            icons=['house-door', 'search', 'people'],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            key="sidebar_menu",
        )
    if cur_show_page != st.session_state.cur_show_page:
        st.session_state.content_container = None
        st.session_state.cur_show_page = cur_show_page
    back_buttom = 'Назад'
    if st.session_state.content_container == 'level_0_container_0':
        gap = 1
        cols[0].markdown(
            f"""
                <div style="height: {gap}px;"></div>
                """,
            unsafe_allow_html=True
        )
        if cols[0].button(back_buttom, type='primary', key='back_level_0_container_0', use_container_width=True):
            st.session_state.content_container = None
            st.rerun()
        show_content_level_0_container_0(st, _)
    elif st.session_state.content_container == 'level_0_container_1':
        gap = 1
        cols[0].markdown(
            f"""
                    <div style="height: {gap}px;"></div>
                    """,
            unsafe_allow_html=True
        )
        if cols[0].button(back_buttom, type='primary', key='back_level_0_container_1', use_container_width=True):
            st.session_state.content_container = None
            st.rerun()
        show_content_level_0_container_1(st, _)
    elif st.session_state.content_container == 'level_0_container_2':
        gap = 1
        cols[0].markdown(
            f"""
                    <div style="height: {gap}px;"></div>
                    """,
            unsafe_allow_html=True
        )
        if cols[0].button(back_buttom, type='primary', key='back_level_0_container_2', use_container_width=True):
            st.session_state.content_container = None
            st.rerun()
        show_content_level_0_container_2(st, _)
    elif st.session_state.cur_show_page == _('Команда'):
        team_page()
    elif st.session_state.cur_show_page == _('Исследования'):
        show_articles()

    elif st.session_state.cur_show_page == _('Главная'):

        with st.container(height=700, border=False):
            st.title('Horizon TSD')
            title_text = _('Horizon Time Series Data - Система прогнозирования временных рядов')
            st.write(f'### {title_text}')

            gap = 150
            st.markdown(
                f"""
                <div style="height: {gap}px;"></div>
                """,
                unsafe_allow_html=True
            )
            text_header = _('Прогнозируйте будущее, основываясь на данных')
            text_header = f'### {text_header}'
            st.write_stream(stream_data(text_header))

            text_dexc = _('Наш инструмент прогнозирования временных рядов предоставляет мощные возможности для предиктивной аналитики в производственных процессах, энергетике, медицине и бизнесе. Он помогает принимать обоснованные решения на основе данных, улучшая планирование, оптимизацию и диагностику в различных отраслях')
            text_dexc = f'##### {text_dexc}'
            st.write_stream(stream_data(text_dexc))


        cols = st.columns(3)
        font_size = "30px"
        font_style = font
        gap = 0
        height = 620
        height_image = 190
        width_image_col = 5
        text = 'text '*120

        with cols[0].container(height=height, border=True):
            col_0_title = 'Test container 0 '

            cols_image = st.columns(spec=[1,width_image_col,1])
            with cols_image[1].container(height=height_image, border=False):
                image_path = 'src/ui/images/238-2383266_line-graph-png-transparent-line-graph-png.png'
                st.image(image_path, use_container_width=True)

            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{col_0_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div style="height: {gap}px;"></div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)
            if st.button('Подробнее', type='primary', use_container_width=True, key='1'):
                st.session_state.content_container = 'level_0_container_0'
                st.rerun()

        with cols[1].container(height=height, border=True):

            cols_image = st.columns(spec=[1,width_image_col,1])
            with cols_image[1].container(height=height_image, border=False):
                image_path = 'src/ui/images/238-2383266_line-graph-png-transparent-line-graph-png.png'
                st.image(image_path, use_container_width=True)

            col_1_title = 'Test container 1'
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{col_1_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div style="height: {gap}px;"></div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)
            if st.button('Подробнее', type='primary', use_container_width=True, key='2'):
                st.session_state.content_container = 'level_0_container_1'
                st.rerun()

        with cols[2].container(height=height, border=True):
            cols_image = st.columns(spec=[1,width_image_col,1])
            with cols_image[1].container(height=height_image, border=False):
                image_path = 'src/ui/images/238-2383266_line-graph-png-transparent-line-graph-png.png'
                st.image(image_path, use_container_width=True)

            col_2_title = 'Test container 2'
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{col_2_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div style="height: {gap}px;"></div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)
            if st.button('Подробнее', type='primary', use_container_width=True, key='3'):
                st.session_state.content_container = 'level_0_container_2'
                st.rerun()


        gap = 100
        st.markdown(
            f"""
            <div style="height: {gap}px;"></div>
            """,
            unsafe_allow_html=True
        )
        with st.container(height=250, border=False):
            title_mid = 'Какой-то заголовок посередине'
            st.markdown(
                f"""
                <div style="font-family: {font}; text-align: center; font-size: 60px; margin: 0 auto;">
                    <h1>{title_mid}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )
        cols = st.columns(2)
        font_size = "25px"
        font_style = font
        height = 200
        cont_face_text = 100
        text = 'text ' * cont_face_text
        with cols[0].container(height=height, border=True):
            line_0_col_0_title = 'Test container 0 0'
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{line_0_col_0_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)
        with cols[1].container(height=height, border=True):
            line_0_col_1_title = 'Test container 0 1'
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{line_0_col_1_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)

        with cols[0].container(height=height, border=True):
            line_1_col_0_title = 'Test container 1 0 '
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{line_1_col_0_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)

        with cols[1].container(height=height, border=True):
            line_1_col_1_title = 'Test container 1 1'
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{line_1_col_1_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)

    st.markdown("---")
    gap = 20
    st.markdown(
        f"""
                <div style="height: {gap}px;"></div>
                """,
        unsafe_allow_html=True
    )
    with st.container(height=200, border=False):
        title_mid = 'Попробуйте сами!'
        st.markdown(
            f"""
                    <div style="font-family: {font}; text-align: center; font-size: 60px; margin: 0 auto;">
                        <h1>{title_mid}</h1>
                    </div>
                    """,
            unsafe_allow_html=True
        )
        gap = 40
        st.markdown(
            f"""
                        <div style="height: {gap}px;"></div>
                        """,
            unsafe_allow_html=True
        )
        cols = st.columns(3)
        link_button_text = _('То как это может выглядеть у вас')
        cols[1].link_button(label=link_button_text, url='http://77.37.136.11:8501', help=None, type="primary",  disabled=False, use_container_width=True)
    st.markdown("---")

    st.write(' ')
    text_contact = _('Свяжитесь с нами:')
    st.markdown(f"### {text_contact}")
    text_question = _('Если у вас есть вопросы или вы хотите узнать больше, свяжитесь с нами:')
    text_phone = _('Телефон:')
    text_site = _('Веб-сайт:')
    st.write(f"""
    {text_question}
    📧 Email: support@forecastingtool.com
    📞 {text_phone} +7 (915) 548-88-52
    🌐 {text_site} [forecastingtool.com](http://77.37.136.11:8501)
    """)

    # Подвал
    st.markdown("---")
    text_last = _('2025 Horizon Time Series Data. Все права защищены.')
    st.markdown(f"© {text_last}")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

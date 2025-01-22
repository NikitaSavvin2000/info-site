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
    st.write('# Прогнозирование 📈')
    st.markdown('---', unsafe_allow_html=True)
    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    simple_forecast_1 = "src/ui/images/simple_forecast_1.png"
    simple_forecast_1 = round_corners(simple_forecast_1, radius=50)

    simple_forecast_2 = "src/ui/images/simple_forecast.png"
    simple_forecast_2 = round_corners(simple_forecast_2, radius=50)

    analysis_page_1 = "src/ui/images/time_series_analysis.png"
    analysis_page_1 = round_corners(analysis_page_1, radius=50)

    analysis_page_2 = "src/ui/images/time_series_analysis_2.png"
    analysis_page_2 = round_corners(analysis_page_2, radius=50)

    grid_search_page = "src/ui/images/grid_search.png"
    grid_search_page = round_corners(grid_search_page, radius=50)

    analytics = "src/ui/images/dark_theme_no_text-Photoroom.png"
    analytics = round_corners(analytics, radius=50)

    adv_forecast_2 = "src/ui/images/adv_forecast_2.png"
    adv_forecast_2 = round_corners(adv_forecast_2, radius=50)

    adv_forecast_1 = "src/ui/images/adv_forecast_1.png"
    adv_forecast_1 = round_corners(adv_forecast_1, radius=50)

    images_col_left[0].image(simple_forecast_2, use_container_width=True, caption="Демонстрация интерфейса")
    text_simple_forecast = _('Простой прогноз')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
    images_col_left[1].write(f'{text_simple_forecast_desc}')
    text_simple_forecast_2 = _('Делай простой прогноз просто загрузив данные')
    images_col_left[1].write(f'{text_simple_forecast_2}')

    images_col_right[1].image(adv_forecast_1, use_container_width=True, caption="Демонстрация интерфейса")
    title_text_learn_model = _('Обучай свои модели')
    images_col_right[0].success(f"##### 📚 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
    images_col_right[0].write(f'{text_learn_model_desc}')

    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(adv_forecast_2, use_container_width=True, caption="Демонстрация интерфейса")
    text_simple_forecast = _('Оценивай точность самостоятельно')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Оценивай точность своих моделей самостоятельно')
    images_col_left[1].write(f'{text_simple_forecast_desc}')


def show_content_level_0_container_1(st, _):
    st.write('# Анализ и обработка данных 🔍')
    st.markdown('---', unsafe_allow_html=True)
    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    simple_forecast_1 = "src/ui/images/simple_forecast_1.png"
    simple_forecast_1 = round_corners(simple_forecast_1, radius=50)

    simple_forecast_2 = "src/ui/images/simple_forecast.png"
    simple_forecast_2 = round_corners(simple_forecast_2, radius=50)

    analysis_page_1 = "src/ui/images/time_series_analysis.png"
    analysis_page_1 = round_corners(analysis_page_1, radius=50)

    analysis_page_2 = "src/ui/images/time_series_analysis_2.png"
    analysis_page_2 = round_corners(analysis_page_2, radius=50)

    grid_search_page = "src/ui/images/grid_search.png"
    grid_search_page = round_corners(grid_search_page, radius=50)

    analytics = "src/ui/images/dark_theme_no_text-Photoroom.png"
    analytics = round_corners(analytics, radius=50)

    analytics_screenshot_1 = "src/ui/images/analysis_screenshot1.png"
    analytics_screenshot_1 = round_corners(analytics_screenshot_1, radius=50)

    analytics_screenshot_2 = "src/ui/images/analysis_screenshot_2.png"
    analytics_screenshot_2 = round_corners(analytics_screenshot_2, radius=50)

    analytics_screenshot_3 = "src/ui/images/analysis_screenshot_3.png"
    analytics_screenshot_3 = round_corners(analytics_screenshot_3, radius=50)

    adv_forecast = "src/ui/images/adv_forecast_2.png"
    adv_forecast = round_corners(adv_forecast, radius=50)

    images_col_left[0].image(analytics_screenshot_1, use_container_width=True, caption="Демонстрация интерфейса")
    text_simple_forecast = _('Интерактивный дашборд')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
    images_col_left[1].write(f'{text_simple_forecast_desc}')
    text_simple_forecast_2 = _('Делай простой прогноз просто загрузив данные')
    images_col_left[1].write(f'{text_simple_forecast_2}')


    images_col_right[1].image(analytics_screenshot_2, use_container_width=True, caption="Демонстрация интерфейса")
    text_title_analysis = _('Визуализация метрик')
    images_col_right[0].success(f"##### 🔍 {text_title_analysis}")
    text_analysis_desc = _('Раздел анализа данных предназначен для глубокого изучения временных рядов, выявления сезонных закономерностей и временных колебаний. Это инструмент для тех, кто хочет получить полное понимание динамики данных, оценить их структуру и прогнозируемость. С помощью мощных аналитических методов можно не только выявить тренды, но и глубже понять скрытые паттерны и сезонные эффекты, что помогает принимать более точные решения в бизнесе и стратегии. Анализ данных – это ключ к обоснованным выводам и эффективному управлению ресурсами.')
    images_col_right[0].write(f'{text_analysis_desc}')


    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(analytics_screenshot_3, use_container_width=True, caption="Демонстрация интерфейса")
    title_text_learn_model = _('Анализ сезонностей')
    images_col_left[1].success(f"##### 📚 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
    images_col_left[1].write(f'{text_learn_model_desc}')


def show_content_level_0_container_2(st, _):
    st.write('# Минимизация рисков 🔍')
    st.markdown('---', unsafe_allow_html=True)
    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    simple_forecast_1 = "src/ui/images/simple_forecast_1.png"
    simple_forecast_1 = round_corners(simple_forecast_1, radius=50)

    simple_forecast_2 = "src/ui/images/simple_forecast.png"
    simple_forecast_2 = round_corners(simple_forecast_2, radius=50)

    analysis_page_1 = "src/ui/images/time_series_analysis.png"
    analysis_page_1 = round_corners(analysis_page_1, radius=50)

    analysis_page_2 = "src/ui/images/time_series_analysis_2.png"
    analysis_page_2 = round_corners(analysis_page_2, radius=50)

    grid_search_page = "src/ui/images/grid_search.png"
    grid_search_page = round_corners(grid_search_page, radius=50)

    analytics = "src/ui/images/dark_theme_no_text-Photoroom.png"
    analytics = round_corners(analytics, radius=50)

    adv_forecast = "src/ui/images/adv_forecast_2.png"
    adv_forecast = round_corners(adv_forecast, radius=50)

    images_col_left[0].image(simple_forecast_2, use_container_width=True, caption="Демонстрация интерфейса")
    text_simple_forecast = _('Простой прогноз')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
    images_col_left[1].write(f'{text_simple_forecast_desc}')
    text_simple_forecast_2 = _('Делай простой прогноз просто загрузив данные')
    images_col_left[1].write(f'{text_simple_forecast_2}')


    images_col_right[1].image(analysis_page_1, use_container_width=True, caption="Демонстрация интерфейса")
    text_title_analysis = _('Анализ данных')
    images_col_right[0].success(f"##### 🔍 {text_title_analysis}")
    text_analysis_desc = _('Раздел анализа данных предназначен для глубокого изучения временных рядов, выявления сезонных закономерностей и временных колебаний. Это инструмент для тех, кто хочет получить полное понимание динамики данных, оценить их структуру и прогнозируемость. С помощью мощных аналитических методов можно не только выявить тренды, но и глубже понять скрытые паттерны и сезонные эффекты, что помогает принимать более точные решения в бизнесе и стратегии. Анализ данных – это ключ к обоснованным выводам и эффективному управлению ресурсами.')
    images_col_right[0].write(f'{text_analysis_desc}')


    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(adv_forecast, use_container_width=True, caption="Демонстрация интерфейса")
    title_text_learn_model = _('Обучай свои модели')
    images_col_left[1].success(f"##### 📚 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
    images_col_left[1].write(f'{text_learn_model_desc}')

    images_col_right[1].image(analytics, use_container_width=True, caption="Демонстрация интерфейса")

    title_text_predict = _('Всегда будь в курсе прогноза')
    images_col_right[0].success(f"##### 💻 {title_text_predict}")
    text_predict_decs = _('Позволяет получать актуальную информацию о прогнозах прямо на почту или в корпоративный мессенджер. Пользователи могут настроить индивидуальные пороговые значения (трешхолды), которые автоматически отправят уведомления о возможных аномалиях в данных, что помогает оперативно реагировать на изменения и минимизировать риски. Такой подход обеспечивает постоянный контроль над процессом, позволяет своевременно выявлять отклонения и принимать меры, что особенно важно для эффективного управления бизнес-процессами.')
    images_col_right[0].write(f'{text_predict_decs}')

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
        # cur_show_page = option_menu(
        #     None,
        #     [_('Главная'), _('Исследования'), _('Команда'),],
        #
        #     icons=['house-door', 'search', 'people'],
        #     menu_icon="cast",
        #     default_index=0,
        #     orientation="horizontal",
        #     key="sidebar_menu",
        # )

        option_map = {
            0: _('Главная'),
            1: _('Исследования'),
            2: _('Команда'),
        }
        option = st.segmented_control(
            None,
            options=option_map.keys(),
            format_func=lambda option: option_map[option],
            selection_mode="single",
        )
        if option is not None:
            cur_show_page = option_map[option]
        else:
            cur_show_page = option_map[0]

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
            st.title('PowerPrognoz')
            title_text = _('PowerPrognoz - Система анализа, обработки данных и прогнозирования энергопотребления')
            st.write(f'### {title_text}')

            gap = 150

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

            # st.markdown(
            #     """
            #     <style>
            #     .st-emotion-cache-1ibsh2c {
            #         padding-top: 0 ; /* Устанавливаем верхний паддинг в 0 */
            #     }
            #     </style>
            #     """,
            #     unsafe_allow_html=True
            # )


            st.title("Advanced Modeling")
            st.write("""
            В основе нашей работы лежит убеждение, что для каждой задачи нужно использовать подходящий инструмент. Некоторые проблемы лучше всего решаются с помощью передовых технологий ИИ, другие — с помощью линейной регрессии, соответствующей текущим потребностям, а большинство задач находятся где-то посередине.
            """)



            st.markdown(
                f"""
                <div style="height: {gap}px;"></div>
                """,
                unsafe_allow_html=True
            )
            text_header = _('Прогнозируйте будущее, основываясь на данных')
            text_header = f'### {text_header}'
            st.write_stream(stream_data(text_header))

            text_dexc = _('Наш инструмент прогнозирования временных рядов предоставляет мощные возможности для предиктивной аналитики с особым акцентом на энергетический сектор. Он помогает предсказывать энергопотребление, оптимизировать распределение ресурсов и повышать устойчивость энергосистем. Благодаря глубокому анализу данных, инструмент также находит применение в производственных процессах, медицине и бизнесе, способствуя улучшению планирования, оптимизации и диагностики в различных отраслях.')
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

        with cols[1].container(height=height, border=True):
            col_0_title = 'Прогнозирование'

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

        with cols[0].container(height=height, border=True):

            cols_image = st.columns(spec=[1,width_image_col,1])
            with cols_image[1].container(height=height_image, border=False):
                image_path = 'src/ui/images/pngwing2.com.png'
                st.image(image_path, use_container_width=True)

            col_1_title = 'Анализ и обработка данных'
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
                image_path = 'src/ui/images/pngwing.com.png'
                st.image(image_path, use_container_width=True)

            col_2_title = 'Оптимизация процессов'
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
            title_mid = 'Преимущества нашего подхода'
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
            line_0_col_0_title = '⚡ Минимизация рисков'
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
            line_0_col_1_title = '🧠 Поддержка принятия решений'
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
            line_1_col_0_title = '🔗 Интеграция'
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
            line_1_col_1_title = '🔧 Гибкость и адаптивность'
            st.markdown(
                f"""
                <div style="text-align: center; margin: 0 auto;">
                    <span style="font-family: {font}; font-size: {font_size}; font-weight: {font_style};">{line_1_col_1_title}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(text)

        with cols[0].container(height=height, border=True):
            line_1_col_0_title = '⏳ Снижение затрат'
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
            line_1_col_1_title = '✨ Интуитивный интерфейс'
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

    st.markdown("---")
    text_last = _('2025 PowerPrognoz. Все права защищены.')
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

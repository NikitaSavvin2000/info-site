import os
import toml
import time
import asyncio
import gettext
import streamlit as st
import sys
sys.path.append(os.path.abspath("/Users/dmitrii/Desktop/PhD/Python/website_2/info-site/src"))

from ui.html.header_content import generate_html_with_base64_image, generate_html_info, generate_html_blocks, generate_html
from team_page import team_page
from PIL import Image, ImageDraw
from streamlit_option_menu import option_menu
from ui.pages.researches_page import show_articles
from streamlit.components.v1 import html
import time
import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded_string

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

config_path = '.streamlit/config.toml'

config = toml.load(config_path)

font = 'arial'


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


def show_content_level_0_container_0(st, _):
    caption = _('Демонстрация интерфейса')
    title_text = _('Прогнозирование 📈')
    st.write(f'# {title_text}')
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

    images_col_left[0].image(simple_forecast_2, use_container_width=True, caption=caption)
    text_simple_forecast = _('Простой прогноз')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
    # images_col_left[1].write(f'{text_simple_forecast_desc}')
    text_simple_forecast_2 = _('Делай простой прогноз просто загрузив данные')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_simple_forecast_desc}
    </div>
    """,
        unsafe_allow_html=True
    )


    images_col_right[1].image(adv_forecast_1, use_container_width=True, caption=caption)
    title_text_learn_model = _('Обучай свои модели')
    images_col_right[0].success(f"##### 📚 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
    images_col_right[0].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-right: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_learn_model_desc}
    </div>
    """,
        unsafe_allow_html=True
    )

    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(adv_forecast_2, use_container_width=True, caption=caption)
    text_simple_forecast = _('Оценивай точность самостоятельно')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Мы предоставляем широкий набор метрик, который позволяет вам проводить объективную оценку тестируемых моделей. Используйте метрики точности, ошибки, устойчивости и качества прогнозирования, чтобы понять, насколько эффективно работает ваша модель. Различные метрики – оценка ошибок (MSE, RMSE, MAE), коэффициент детерминации (R²) и другие. Гибкость в анализе – сравнивайте модели и выбирайте лучшие решения. Прозрачность – получите четкое представление о сильных и слабых сторонах модели. Доверьтесь данным, а не интуиции! 🚀')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_simple_forecast_desc}
    </div>
    """,
        unsafe_allow_html=True
    )


def show_content_level_0_container_1(st, _):
    caption = _('Демонстрация интерфейса')


    text_title = _('Анализ и обработка данных 🔍')
    st.write(f'# {text_title}')
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

    analytics_screenshot_2 = "src/ui/images/analysis_screenshot2.png"
    analytics_screenshot_2 = round_corners(analytics_screenshot_2, radius=50)

    analytics_screenshot_3 = "src/ui/images/analysis_screenshot3.png"
    analytics_screenshot_3 = round_corners(analytics_screenshot_3, radius=50)

    adv_forecast = "src/ui/images/adv_forecast_2.png"
    adv_forecast = round_corners(adv_forecast, radius=50)

    images_col_left[0].image(analytics_screenshot_1, use_container_width=True, caption=caption)
    text_simple_forecast = _('Интерактивный дашборд')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_simple_forecast_desc}
    </div>
    """,
        unsafe_allow_html=True
    )

    images_col_right[1].image(analytics_screenshot_2, use_container_width=True, caption=caption)
    text_title_analysis = _('Визуализация метрик')
    images_col_right[0].success(f"##### 🔍 {text_title_analysis}")
    text_analysis_desc = _('Раздел анализа данных предназначен для глубокого изучения временных рядов, выявления сезонных закономерностей и временных колебаний. Это инструмент для тех, кто хочет получить полное понимание динамики данных, оценить их структуру и прогнозируемость. С помощью мощных аналитических методов можно не только выявить тренды, но и глубже понять скрытые паттерны и сезонные эффекты, что помогает принимать более точные решения в бизнесе и стратегии. Анализ данных – это ключ к обоснованным выводам и эффективному управлению ресурсами.')
    images_col_right[0].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-right: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_analysis_desc}
    </div>
    """,
        unsafe_allow_html=True
    )


    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(analytics_screenshot_3, use_container_width=True, caption=caption)
    title_text_learn_model = _('Анализ сезонностей')
    images_col_left[1].success(f"##### 📚 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_learn_model_desc}
    </div>
    """,
        unsafe_allow_html=True
    )


def show_content_level_0_container_2(st, _):
    caption = _('Демонстрация интерфейса')

    text_title = _('Минимизация рисков 🔍')
    st.write(f'# {text_title}')
    st.markdown('---', unsafe_allow_html=True)


    simple_forecast_2 = "src/ui/images/level_0_container_2_image_1.png"
    simple_forecast_2 = round_corners(simple_forecast_2, radius=50)

    analysis_page_1 = "src/ui/images/analysis_screenshot3.png"
    analysis_page_1 = round_corners(analysis_page_1, radius=50)

    adv_forecast = "src/ui/images/level_0_container_2_image_2.png"
    adv_forecast = round_corners(adv_forecast, radius=50)

    scrin_4 = "src/ui/images/level_0_container_2_image_4.png"
    scrin_4 = round_corners(scrin_4, radius=50)

    scrin_5 = "src/ui/images/level_0_container_2_image_5.png"
    scrin_5 = round_corners(scrin_5, radius=50)

    analytics = "src/ui/images/level_0_container_2_image_3.png"
    analytics = round_corners(analytics, radius=50)

    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(simple_forecast_2, use_container_width=True, caption=caption)
    text_simple_forecast = _('Простой прогноз')
    images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
    text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_simple_forecast_desc}
    </div>
    """,
        unsafe_allow_html=True
    )

    # text_simple_forecast_2 = _('Делай простой прогноз просто загрузив данные')
    # images_col_left[1].write(f'{text_simple_forecast_2}')


    images_col_right[1].image(analysis_page_1, use_container_width=True, caption=caption)
    text_title_analysis = _('Анализ данных')
    images_col_right[0].success(f"##### 🔍 {text_title_analysis}")
    text_analysis_desc = _('Раздел анализа данных предназначен для глубокого изучения временных рядов, выявления сезонных закономерностей и временных колебаний. Это инструмент для тех, кто хочет получить полное понимание динамики данных, оценить их структуру и прогнозируемость. С помощью мощных аналитических методов можно не только выявить тренды, но и глубже понять скрытые паттерны и сезонные эффекты, что помогает принимать более точные решения в бизнесе и стратегии. Анализ данных – это ключ к обоснованным выводам и эффективному управлению ресурсами.')
    images_col_right[0].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-right: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_analysis_desc}
    </div>
    """,
        unsafe_allow_html=True
    )


    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(adv_forecast, use_container_width=True, caption=caption)
    title_text_learn_model = _('Обучай свои модели')
    images_col_left[1].success(f"##### 📚 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_learn_model_desc}
    </div>
    """,
        unsafe_allow_html=True
    )

    images_col_right[1].image(analytics, use_container_width=True, caption=caption)

    title_text_predict = _('Всегда будь в курсе прогноза')
    images_col_right[0].success(f"##### 💻 {title_text_predict}")
    text_predict_decs = _('Позволяет получать актуальную информацию о прогнозах прямо на почту или в корпоративный мессенджер. Пользователи могут настроить индивидуальные пороговые значения (трешхолды), которые автоматически отправят уведомления о возможных аномалиях в данных, что помогает оперативно реагировать на изменения и минимизировать риски. Такой подход обеспечивает постоянный контроль над процессом, позволяет своевременно выявлять отклонения и принимать меры, что особенно важно для эффективного управления бизнес-процессами.')
    images_col_right[0].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-right: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_predict_decs}
    </div>
    """,
        unsafe_allow_html=True
    )

    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(scrin_4, use_container_width=True, caption=caption)
    title_text_learn_model = _('Создание своих уведомлений')
    images_col_left[1].success(f"##### 📌 {title_text_learn_model}")
    text_learn_model_desc = _('Раздел создания уведомлений предназначен для настройки автоматических оповещений на основе прогнозных данных. Это позволяет оперативно реагировать на важные изменения и принимать обоснованные решения. Пользователь может задать условия и параметры уведомлений, чтобы получать своевременные сообщения при достижении критических значений или значимых тенденций. Гибкая система настройки обеспечивает адаптацию уведомлений под конкретные задачи, повышая удобство работы и эффективность мониторинга')
    images_col_left[1].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
            margin-left: 20px;
        }}
    </style>
    <div class="justified-text">
        {text_learn_model_desc}
    </div>
    """,
        unsafe_allow_html=True
    )

    images_col_right[1].image(scrin_5, use_container_width=True, caption=caption)
    title_text_predict = _('Получение уведомлений о превышении установенных значений на основвании прогноза')
    images_col_right[0].success(f"##### 📩 {title_text_predict}")
    text_predict_decs = _('Получение уведомлений о превышении установленных значений позволяет заранее реагировать на критические изменения, основываясь на прогнозных данных. Система автоматически отслеживает показатели и отправляет оповещения, если значения выходят за заданные границы. Это помогает оперативно принимать меры, снижать риски и эффективно управлять процессами. Гибкая настройка уведомлений позволяет адаптировать их под индивидуальные потребности, обеспечивая надежный контроль за ключевыми параметрами.')
    images_col_right[0].markdown(
        f"""
    <style>
        .justified-text {{
            text-align: justify;
            font-size: 17px; /* Измени размер по необходимости */
            font-family: monospace; /* Измени шрифт по необходимости */
        }}
    </style>
    <div class="justified-text">
        {text_learn_model_desc}
    </div>
    """,
        unsafe_allow_html=True
    )


st.set_page_config(
    page_title="Horizon Time Series Data",
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

    st.session_state.setdefault('bloc_1_select', False)
    st.session_state.setdefault('bloc_2_select', False)
    st.session_state.setdefault('bloc_3_select', False)

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



    text_analysis = _("Выявляем скрытые закономерности и тренды в электропотреблении с помощью передовых методов обработки временных рядов.")
    text_forecasting = _("Используем машинное обучение и глубокие нейросети для точного предсказания энергопотребления и предотвращения пиковых нагрузок.")
    text_optimization = _("Разрабатываем интеллектуальные решения для повышения эффективности использования ресурсов и снижения затрат.")

    # Определяем уникальные тексты для каждого блока
    text_risks = _("Снижаем неопределенность и помогаем избежать неожиданных скачков энергопотребления.")
    text_decision = _("Предоставляем точные данные и прогнозы для эффективного управления ресурсами.")
    text_integration = _("Легко интегрируемся в существующие промышленные и IT-экосистемы.")
    text_flexibility = _("Адаптируемся под любые задачи благодаря модульному подходу.")
    text_costs = _("Оптимизируем энергопотребление и сокращаем издержки бизнеса.")
    text_interface = _("Интуитивно понятный и удобный интерфейс для работы без сложного обучения.")

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

    back_buttom = _('Назад')

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

        image_1 = image_to_base64('src/ui/html/3d-windmill-project.jpg')
        image_2 = image_to_base64('src/ui/html/pexels-pok-rie-33563-157827.jpg')
        image_3 = image_to_base64('src/ui/html/jason-mavrommatis-nyL-rzwP-Mk-unsplash.jpg')
        image_4 = image_to_base64('src/ui/html/jason-mavrommatis--s1w1SguZTI-unsplash.jpg')
        image_5 = image_to_base64('src/ui/html/soren-h-omfN1pW-n2Y-unsplash.jpg')

        title = "Horizon Time Series Data"
        description = _("Horizon Time Series – энергия данных, точность прогнозов")
        html_output = generate_html_with_base64_image(
            title, description,
            image_1,
            image_2,
            image_3,
            image_4,
            image_5)
        
        with st.container(height=720, border=False, key='castom_header'):
            html(html_output, height=700)


        cols = st.columns(3)
        font_size = "30px"
        font_style = font
        gap = 0
        gap_2 = 70
        gap_2_castom = gap_2
        if st.session_state.language == 'ru':
            gap_2_castom = gap_2 - 26

        height = 520
        height_image = 190
        width_image_col = 5

        text_button_more = _('Подробнее')

        # with cols[0].container(height=height, border=True):
        #     cols_image = st.columns(spec=[1, width_image_col, 1])
        #     with cols_image[1].container(height=height_image, border=False):
        #         image_path = 'src/ui/images/pngwing2.com.png'
        #         st.image(image_path, use_container_width=True)
        #
        #     col_1_title = _('Анализ и обработка данных')
        #     st.markdown(f"<div style='text-align: center;'><span style='font-family: {font}; font-size: {font_size}; font-weight: {font_style};'>{col_1_title}</span></div>", unsafe_allow_html=True)
        #     st.markdown(f"<div style='height: {gap}px;'></div>", unsafe_allow_html=True)
        #     st.write(text_analysis)
        #     st.markdown(f"<div style='height: {gap_2}px;'></div>", unsafe_allow_html=True)
        #
        #     if st.button(text_button_more, type='primary', use_container_width=True, key='2'):
        #         st.session_state.content_container = 'level_0_container_1'
        #         st.write(f'# Нажато')
        #         st.rerun()
        #
        # with cols[1].container(height=height, border=True):
        #     col_0_title = _('Прогнозирование')
        #
        #     cols_image = st.columns(spec=[1, width_image_col, 1])
        #     with cols_image[1].container(height=height_image, border=False):
        #         image_path = 'src/ui/images/238-2383266_line-graph-png-transparent-line-graph-png.png'
        #         st.image(image_path, use_container_width=True)
        #
        #     st.markdown(f"<div style='text-align: center;'><span style='font-family: {font}; font-size: {font_size}; font-weight: {font_style};'>{col_0_title}</span></div>", unsafe_allow_html=True)
        #     st.markdown(f"<div style='height: {gap}px;'></div>", unsafe_allow_html=True)
        #     st.write(text_forecasting)
        #     st.markdown(f"<div style='height: {gap_2_castom}px;'></div>", unsafe_allow_html=True)
        #
        #     if st.button(text_button_more, type='primary', use_container_width=True, key='1'):
        #         st.session_state.content_container = 'level_0_container_0'
        #         st.rerun()
        #
        # with cols[2].container(height=height, border=True):
        #     cols_image = st.columns(spec=[1, width_image_col, 1])
        #     with cols_image[1].container(height=height_image, border=False):
        #         image_path = 'src/ui/images/pngwing.com.png'
        #         st.image(image_path, use_container_width=True)
        #
        #     col_2_title = _('Оптимизация процессов')
        #     st.markdown(f"<div style='text-align: center;'><span style='font-family: {font}; font-size: {font_size}; font-weight: {font_style};'>{col_2_title}</span></div>", unsafe_allow_html=True)
        #     st.markdown(f"<div style='height: {gap}px;'></div>", unsafe_allow_html=True)
        #     st.write(text_optimization)
        #     st.markdown(f"<div style='height: {gap_2}px;'></div>", unsafe_allow_html=True)
        #
        #     if st.button(text_button_more, type='primary', use_container_width=True, key='3'):
        #         st.session_state.content_container = 'level_0_container_2'
        #         st.rerun()

        cols = st.columns(3)
        height = 520
        html_content_height = height-40
        width_content = 360
        height_content = html_content_height-50
        width_button = 15
        border=False
        opacity = 0.8

        with cols[0].container(height=height, border=border, key='bloc_1'):
            html_content = generate_html(
                image_path='src/ui/html/pexels-rdne-7948058.jpg',
                title=_('Анализ и обработка данных'),
                text=text_analysis,
                opacity=opacity,
                width=width_content,
                height=height_content)
            html(html_content, height=html_content_height)
            cols_button = cols[0].columns(spec=[1,width_button,1])
            if cols_button[1].button(text_button_more, type='primary', use_container_width=True, key='1'):
                st.session_state.content_container = 'level_0_container_1'
                st.rerun()

        with cols[1].container(height=height, border=border, key='bloc_2'):
            html_content = generate_html(
                image_path='src/ui/html/pexels-n-voitkevich-6120208.jpg',
                title=_('Прогнозирование'),
                text=text_forecasting,
                opacity=opacity,
                width=width_content,
                height=height_content)
            html(html_content, height=html_content_height)
            cols_button = cols[1].columns(spec=[1,width_button,1])
            if cols_button[1].button(text_button_more, type='primary', use_container_width=True, key='2'):
                st.session_state.content_container = 'level_0_container_0'
                st.rerun()

        with cols[2].container(height=height, border=border, key='bloc_3'):
            html_content = generate_html(
                image_path='src/ui/html/pexels-artempodrez-5716032.jpg',
                title= _('Оптимизация процессов'),
                text=text_optimization,
                opacity=opacity,
                width=width_content,
                height=height_content)
            html(html_content, height=html_content_height)
            cols_button = cols[2].columns(spec=[1,width_button,1])
            if cols_button[1].button(text_button_more, type='primary', use_container_width=True, key='3'):
                st.session_state.content_container = 'level_0_container_2'
                st.rerun()


        gap = 100

        st.markdown(f"<div style='height: {gap}px;'></div>", unsafe_allow_html=True)


        image_1 = image_to_base64('src/ui/html/pexels-artempodrez-5716032.jpg')
        image_2 = image_to_base64('src/ui/html/pexels-rdne-7413936.jpg')
        image_3 = image_to_base64('src/ui/html/pexels-mikhail-nilov-6963017.jpg')
        image_4 = image_to_base64('src/ui/html/pexels-vlada-karpovich-7433837.jpg')
        image_5 = image_to_base64('src/ui/html/pexels-pavel-danilyuk-7868970.jpg')
        title_1 = _('Минимизация рисков')
        title_2 = _('Поддержка принятия решений')
        title_3 = _('Интеграция')
        title_4 = _('Гибкость и адаптивность')
        title_5 = _('Снижение затрат')
        title_6 = _('Интуитивный интерфейс')
        titles = [title_1, title_2, title_3, title_4, title_5, title_6]
        texts = [text_risks, text_decision, text_integration, text_flexibility, text_costs, text_interface]

        html_output = generate_html_info(
            image_1,
            image_2,
            image_3,
            image_4,
            image_5,
            titles,
            texts,
            'monospace')

        with st.container(height=720, border=False, key='castom_info'):
            html(html_output, height=700)



        text = _('Реализованный пример для University of Brescia')

        st.markdown("---")
        st.markdown(f"<div style='height: {50}px;'></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center;'><span style='font-family: {font}; font-size: {35}px;'>{text}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='height: {10}px;'></div>", unsafe_allow_html=True)

        cols = st.columns(3)
        cols[1].image("src/ui/images/new_logo_2022.svg")


        # text_link_button = _("Перейти")
        # cols[1].link_button(text_link_button, type="primary", url="http://77.37.136.11:8501", use_container_width=True)
        # st.markdown(f"<div style='height: {50}px;'></div>", unsafe_allow_html=True)


    st.markdown("---")
    st.write(' ')
    text_contact = _('Свяжитесь с нами:')
    st.markdown(f"### {text_contact}")
    text_question = _('Если у вас есть вопросы или вы хотите узнать больше, свяжитесь с нами:')
    text_phone = _('Телефон:')
    text_site = _('Веб-сайт:')
    st.write(f"""
    {text_question}
    📧 Email: savvin.nikita.work@yandex.ru
    📞 {text_phone} +7 (915) 548-88-52
    """)

    st.markdown("---")
    text_last = _('2025 Horizon Time Series')
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

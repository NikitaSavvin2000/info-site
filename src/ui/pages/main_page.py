import asyncio

import streamlit as st
from PIL import Image, ImageDraw
import time
from ui.pages.researches_page import show_articles
from team_page import team_page
import gettext
import os
from streamlit_option_menu import option_menu

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

# @check_authentication
async def main():

    st.session_state.setdefault('language', 'ru')
    st.session_state.setdefault('language_show', '🇷🇺 RU')

    cols = st.columns(spec=[10, 1])

    popover_lang = cols[1].popover(st.session_state.language_show, use_container_width=True)
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


    with cols[0]:
        cur_show_page = option_menu(
            None,
            [_('Главная'), _('Исследования'), _('Команда'),],

            icons=['house-door', 'search', 'people'],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            key="sidebar_menu"

        )



    if cur_show_page == _('Команда'):
        team_page()
    elif cur_show_page == _('Исследования'):
        show_articles()
    elif cur_show_page == _('Главная'):
        st.title('Horizon TSD')
        title_text = _('Horizon Time Series Data - Система прогнозирования временных рядов')
        st.write(f'### {title_text}')

        text_header = _('Прогнозируйте будущее, основываясь на данных')
        text_header = f'### {text_header}'
        st.write_stream(stream_data(text_header))

        text_dexc = _('Наш инструмент прогнозирования временных рядов предоставляет мощные возможности для предиктивной аналитики в производственных процессах, энергетике, медицине и бизнесе. Он помогает принимать обоснованные решения на основе данных, улучшая планирование, оптимизацию и диагностику в различных отраслях')
        text_dexc = f'##### {text_dexc}'
        st.write_stream(stream_data(text_dexc))

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

        images_col_left[0].image(simple_forecast_2, use_column_width=True, caption="Демонстрация интерфейса")
        text_simple_forecast = _('Простой прогноз')
        images_col_left[1].success(f"##### 📊 {text_simple_forecast}")
        text_simple_forecast_desc = _('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')
        images_col_left[1].write(f'{text_simple_forecast_desc}')
        text_simple_forecast_2 = _('Делай простой прогноз просто загрузив данные')
        images_col_left[1].write(f'{text_simple_forecast_2}')


        images_col_right[1].image(analysis_page_1, use_column_width=True, caption="Демонстрация интерфейса")
        text_title_analysis = _('Анализ данных')
        images_col_right[0].success(f"##### 🔍 {text_title_analysis}")
        text_analysis_desc = _('Раздел анализа данных предназначен для глубокого изучения временных рядов, выявления сезонных закономерностей и временных колебаний. Это инструмент для тех, кто хочет получить полное понимание динамики данных, оценить их структуру и прогнозируемость. С помощью мощных аналитических методов можно не только выявить тренды, но и глубже понять скрытые паттерны и сезонные эффекты, что помогает принимать более точные решения в бизнесе и стратегии. Анализ данных – это ключ к обоснованным выводам и эффективному управлению ресурсами.')
        images_col_right[0].write(f'{text_analysis_desc}')


        images_col_left = st.columns(spec=[3, 2])
        images_col_right = st.columns(spec=[2, 3])

        images_col_left[0].image(adv_forecast, use_column_width=True, caption="Демонстрация интерфейса")
        title_text_learn_model = _('Обучай свои модели')
        images_col_left[1].success(f"##### 📚 {title_text_learn_model}")
        text_learn_model_desc = _('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')
        images_col_left[1].write(f'{text_learn_model_desc}')

        images_col_right[1].image(analytics, use_column_width=True, caption="Демонстрация интерфейса")

        title_text_predict = _('Всегда будь в курсе прогноза')
        images_col_right[0].success(f"##### 💻 {title_text_predict}")
        text_predict_decs = _('Позволяет получать актуальную информацию о прогнозах прямо на почту или в корпоративный мессенджер. Пользователи могут настроить индивидуальные пороговые значения (трешхолды), которые автоматически отправят уведомления о возможных аномалиях в данных, что помогает оперативно реагировать на изменения и минимизировать риски. Такой подход обеспечивает постоянный контроль над процессом, позволяет своевременно выявлять отклонения и принимать меры, что особенно важно для эффективного управления бизнес-процессами.')
        images_col_right[0].write(f'{text_predict_decs}')

        text_main_func = _('Основные функции:')
        st.markdown(f"### {text_main_func}")
        text1 = _('Прогнозирование: Постоянные обновления и уведомления о прогнозах и аномалиях в корпоративные мессенджеры')
        st.write(f'##### - 🕒 {text1}')
        text2 = _('Высокая точность: Используем передовые алгоритмы машинного обучения и нейронные сети')
        st.write(f'##### - 🚀 {text2}')
        text3 = _('Глубокий анализ данных: Выявление ключевых факторов и разработка стратегий на основе временных рядов')
        st.write(f'##### - 📈 {text3}')
        text4 = _('Легкий доступ: Веб-интерфейс с минимальной настройкой')
        st.write(f'##### - 🌐 {text4}')
        text5 = _('Сбор данных: Автоматический сбор временных данных из различных источников')
        st.write(f'##### - 📥 {text5}')
        text6 = _('Модульность: Возможность адаптации модели под конкретные бизнес-задачи')
        st.write(f'##### - 🧩 {text6}')
        text7 = _('Настраиваемость: Широкие возможности настройки параметров модели и прогнозов')
        st.write(f'##### - 🔧 {text7}')

        text_adv = _('Преимущества:')
        st.markdown(f"### {text_adv}")
        cols = st.columns(2)
        text_adv_1 = _('Минимизация рисков благодаря качественным и оперативным прогнозам')
        text_adv_2 = _('Снижение затрат рабочего времени на анализ и прогноз')
        text_adv_3 = _('Интуитивно понятный и простой интерфейс')
        text_adv_4 = _('Поддержка принятия стратегических решений')
        text_adv_5 = _('Интеграция с корпоративными системами и мессенджерами')
        text_adv_6 = _('Гибкость и адаптивность под разные задачи')

        with cols[0]:
            st.success(f"⚡ {text_adv_1}")
            st.success(f"⏳ {text_adv_2}")
            st.success(f"✨ {text_adv_3}")
        with cols[1]:
            st.success(f"🧠 {text_adv_4}")
            st.success(f"🔗 {text_adv_5}")
            st.success(f"🔧 {text_adv_6}")

        text_try = _('Попробуйте сами:')
        st.markdown(f"### {text_try}")


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

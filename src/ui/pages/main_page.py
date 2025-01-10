import asyncio


from ui.utils.data_processing import check_authentication
import streamlit as st
from PIL import Image, ImageDraw
import time


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

# @check_authentication
async def main():

    st.title('Horizon TSD')
    st.write(f'### Horizon Time Series Data - Система прогнозирования временных рядов')

    text_header = '### Прогнозируйте будущее, основываясь на данных'
    st.write_stream(stream_data(text_header))

    text_dexc = '##### Наш инструмент прогнозирования временных рядов предоставляет мощные возможности для предиктивной аналитики в производственных процессах, энергетике, медицине и бизнесе. Он помогает принимать обоснованные решения на основе данных, улучшая планирование, оптимизацию и диагностику в различных отраслях'
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

    analytics = "src/ui/images/analytics.png"
    analytics = round_corners(analytics, radius=50)

    adv_forecast = "src/ui/images/adv_forecast_2.png"
    adv_forecast = round_corners(adv_forecast, radius=50)

    images_col_left[0].image(simple_forecast_2, use_column_width=True, caption="Демонстрация интерфейса")
    images_col_left[1].success("##### 📊 Простой прогноз")
    images_col_left[1].write('Простой прогноз создан для быстрого получения результатов с минимальными усилиями. Достаточно загрузить данные, выбрать горизонт прогноза, и инструмент автоматически выполнит расчет, используя модели, разработанные на основе научных исследований. Этот подход позволяет оперативно оценивать тенденции и принимать решения, даже если требуется предварительная оценка данных. Простой прогноз идеально подходит для случаев, когда важна скорость и удобство, а высокая точность не является ключевым требованием.')

    images_col_left[1].write('Делай простой прогноз просто загрузив данные')

    images_col_right[1].image(analysis_page_1, use_column_width=True, caption="Демонстрация интерфейса")
    images_col_right[0].success("##### 🔍 Анализ данных")
    images_col_right[0].write('Раздел анализа данных предназначен для глубокого изучения временных рядов, выявления сезонных закономерностей и временных колебаний. Это инструмент для тех, кто хочет получить полное понимание динамики данных, оценить их структуру и прогнозируемость. С помощью мощных аналитических методов можно не только выявить тренды, но и глубже понять скрытые паттерны и сезонные эффекты, что помогает принимать более точные решения в бизнесе и стратегии. Анализ данных – это ключ к обоснованным выводам и эффективному управлению ресурсами.')


    images_col_left = st.columns(spec=[3, 2])
    images_col_right = st.columns(spec=[2, 3])

    images_col_left[0].image(adv_forecast, use_column_width=True, caption="Демонстрация интерфейса")
    images_col_left[1].success("##### 📚 Обучай свои модели")
    images_col_left[1].write('Раздел обучения моделей предназначен для поиска оптимальных параметров, которые обеспечат наибольшую точность прогноза, настроенного под индивидуальные данные. Даже без навыков программирования, пользователь может легко подобрать параметры, которые улучшат работу модели, делая прогноз более точным и адаптированным к конкретным условиям. Этот процесс позволяет настроить модель для максимально эффективной работы с данными, обеспечивая гибкость и надежность прогноза, что особенно важно для принятия стратегических решений в динамичных и изменяющихся условиях.')

    images_col_right[1].image(analytics, use_column_width=True, caption="Демонстрация интерфейса")
    images_col_right[0].success("##### 💻 Всегда будь в курсе прогноза")
    images_col_right[0].write('Позволяет получать актуальную информацию о прогнозах прямо на почту или в корпоративный мессенджер. Пользователи могут настроить индивидуальные пороговые значения (трешхолды), которые автоматически отправят уведомления о возможных аномалиях в данных, что помогает оперативно реагировать на изменения и минимизировать риски. Такой подход обеспечивает постоянный контроль над процессом, позволяет своевременно выявлять отклонения и принимать меры, что особенно важно для эффективного управления бизнес-процессами.')




    st.markdown("### Основные функции:")
    st.write('##### - 🕒 **Прогнозирование:** Постоянные обновления и уведомления о прогнозах и аномалиях в корпоративные мессенджеры')
    st.write('##### - 🚀 **Высокая точность:** Используем передовые алгоритмы машинного обучения и нейронные сети')
    st.write('##### - 📈 **Глубокий анализ данных:** Выявление ключевых факторов и разработка стратегий на основе временных рядов')
    st.write('##### - 🌐 **Легкий доступ:** Веб-интерфейс с минимальной настройкой')
    st.write('##### - 📥 **Сбор данных:** Автоматический сбор временных данных из различных источников')
    st.write('##### - 🧩 **Модульность:** Возможность адаптации модели под конкретные бизнес-задачи')
    st.write('##### - 🔧 **Настраиваемость:** Широкие возможности настройки параметров модели и прогнозов')


    st.markdown("### Преимущества:")
    cols = st.columns(2)
    with cols[0]:
        st.success("⚡ Минимизация рисков благодаря качественным и оперативным прогнозам")
        st.success("⏳ Снижение затрат рабочего времени на анализ и прогноз")
        st.success("✨ Интуитивно понятный и простой интерфейс")
    with cols[1]:
        st.success("🧠 Поддержка принятия стратегических решений")
        st.success("🔗 Интеграция с корпоративными системами и мессенджерами")
        st.success("🔧 Гибкость и адаптивность под разные задачи")

    st.markdown("### Попробуйте сами:")


    cols = st.columns(3)
    cols[1].link_button(label='То как это может выглядеть у вас', url='http://77.37.136.11:8501', help=None, type="primary",  disabled=False, use_container_width=True)

    st.markdown("### Свяжитесь с нами:")
    st.write("""
    Если у вас есть вопросы или вы хотите узнать больше, свяжитесь с нами:
    📧 Email: support@forecastingtool.com
    📞 Телефон: +1 (123) 456-7890
    🌐 Веб-сайт: [forecastingtool.com](https://forecastingtool.com)
    """)

    # Подвал
    st.markdown("---")
    st.markdown("© 2025 Time Series Forecasting Tool. Все права защищены.")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

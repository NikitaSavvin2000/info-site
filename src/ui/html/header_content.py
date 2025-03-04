# def generate_html_with_base64_image(title, description, image_1, image_2, image_3, image_4, image_5):
#     html_content = f"""
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Slideshow Background</title>
#         <style>
#             html, body {{
#                 margin: 0;
#                 padding: 0;
#                 width: 100%;
#                 height: 100%;
#                 overflow: hidden;
#             }}
#
#             body {{
#                 font-family: Arial, sans-serif;
#                 color: white;
#                 text-align: center;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#             }}
#
#             .slideshow {{
#                 position: fixed;
#                 top: 0;
#                 left: 0;
#                 width: 100%;
#                 height: 100%;
#                 z-index: -5;
#                 background: transparent;
#                 overflow: hidden;
#             }}
#
#             /* Стиль для изображений */
#
#             .slideshow img {{
#                 position: absolute;
#                 top: 0;
#                 left: 0;
#                 width: 100%;
#                 height: 100%;
#                 object-fit: cover;
#                 opacity: 0;
#                 animation: fade 16s infinite;
#                 border-radius: 20px; /* Скругление углов */
#                 background: transparent; /* Убираем фон в углах */
#                 overflow: hidden;
#             }}
#             /* Задержка для каждого изображения */
#             .slideshow img:nth-child(1) {{
#                 animation-delay: 0s;
#             }}
#
#             .slideshow img:nth-child(2) {{
#                 animation-delay: 4s;
#             }}
#
#             .slideshow img:nth-child(3) {{
#                 animation-delay: 8s;
#             }}
#
#             .slideshow img:nth-child(4) {{
#                 animation-delay: 12s;
#             }}
#
#             .slideshow img:nth-child(5) {{
#                 animation-delay: 16s;
#             }}
#
#             @keyframes fade {{
#                 0% {{
#                     opacity: 0;
#                 }}
#                 20% {{
#                     opacity: 1;
#                 }}
#                 80% {{
#                     opacity: 1;
#                 }}
#                 100% {{
#                     opacity: 0;
#                 }}
#             }}
#
#             /* Текстовый блок */
#             .text-overlay {{
#                 position: relative;
#                 z-index: 1;
#             }}
#
#             .text-overlay h1 {{
#                 font-size: 3rem;
#                 margin: 0;
#             }}
#
#             .text-overlay p {{
#                 font-size: 1.5rem;
#                 margin-top: 1rem;
#             }}
#         </style>
#     </head>
#     <body>
#     <div class="slideshow">
#         <img src="data:image/jpeg;base64,{image_1}" alt="Image 1">
#         <img src="data:image/jpeg;base64,{image_2}" alt="Image 2">
#         <img src="data:image/jpeg;base64,{image_3}" alt="Image 3">
#         <img src="data:image/jpeg;base64,{image_4}" alt="Image 4">
#         <img src="data:image/jpeg;base64,{image_5}" alt="Image 5">
#     </div>
#
#     <div class="text-overlay">
#         <h1>{title}</h1>
#         <p>{description}</p>
#     </div>
#     </body>
#     </html>
#     """
#     return html_content
#

def generate_html_with_base64_image(title, description, image_1, image_2, image_3, image_4, image_5):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Slideshow Background</title>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
            }}

            body {{
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .slideshow {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -5;
                background: transparent;
                overflow: hidden;
            }}

            .slideshow img {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                object-fit: cover;
                opacity: 0;
                animation: fade 25s infinite;
                border-radius: 20px; /* Скругление углов */
#               background: transparent; /* Убираем фон в углах */
            }}

            .slideshow img:nth-child(1) {{ animation-delay: 0s; }}
            .slideshow img:nth-child(2) {{ animation-delay: 5s; }}
            .slideshow img:nth-child(3) {{ animation-delay: 10s; }}
            .slideshow img:nth-child(4) {{ animation-delay: 15s; }}
            .slideshow img:nth-child(5) {{ animation-delay: 20s; }}

            @keyframes fade {{
                0% {{ opacity: 0; }}
                10% {{ opacity: 1; }}
                30% {{ opacity: 1; }}
                40% {{ opacity: 0; }}
                100% {{ opacity: 0; }}
            }}

            .text-overlay {{
                position: relative;
                z-index: 1;
            }}

            .text-overlay h1 {{
                font-size: 3rem;
                margin: 0;
            }}

            .text-overlay p {{
                font-size: 1.5rem;
                margin-top: 1rem;
            }}
        </style>
    </head>
    <body>
    <div class="slideshow">
        <img src="data:image/jpeg;base64,{image_1}" alt="Image 1">
        <img src="data:image/jpeg;base64,{image_2}" alt="Image 2">
        <img src="data:image/jpeg;base64,{image_3}" alt="Image 3">
        <img src="data:image/jpeg;base64,{image_4}" alt="Image 4">
        <img src="data:image/jpeg;base64,{image_5}" alt="Image 5">
    </div>

    <div class="text-overlay">
        <h1>{title}</h1>
        <p>{description}</p>
    </div>
    </body>
    </html>
    """
    return html_content

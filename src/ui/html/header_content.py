
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


def generate_html_info(image_1, image_2, image_3, image_4, image_5, titles, texts, font_text="Arial"):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Blocks</title>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: {font_text};
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
                border-radius: 20px;
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

            .info-container {{
                position: absolute;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(2, 1fr);
                gap: 20px;
                width: 80%;
                height: 60%;
                z-index: 1;
            }}

            .info-block {{
                background: rgba(255, 255, 255, 0.85);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                transition: transform 0.3s ease-in-out;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                font-family: {font_text};
            }}

            .info-block:hover {{
                transform: scale(1.1);
            }}

            .info-title {{
                font-size: 1.7rem;
                font-weight: Semi Bold;
                color: #333;
                text-align: center;
            }}

            .info-description {{
                font-size: 1.4rem;
                color: #333;
                text-align: center;
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

    <div class="info-container">
        {''.join([f'<div class="info-block"><div class="info-title">{titles[i]}</div><br><div class="info-description">{texts[i]}</div></div>' for i in range(6)])}
    </div>
    </body>
    </html>
    """
    return html_content



def generate_html_blocks():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Выбор блока</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }

            .container {
                display: flex;
                gap: 20px;
            }

            .block {
                width: 200px;
                height: 200px;
                background-color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
                cursor: pointer;
            }

            .block:hover {
                transform: scale(1.1);
                box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
            }
        </style>
        <script>
            function blockClicked(blockId) {
                window.parent.postMessage({ blockId: blockId }, "*");
            }

            window.addEventListener("message", function(event) {
                if (event.data.blockId) {
                    document.querySelectorAll(".block").forEach(block => {
                        block.style.backgroundColor = "white";
                    });
                    document.getElementById(event.data.blockId).style.backgroundColor = "#ddd";
                }
            });
        </script>
    </head>
    <body>
        <div class="container">
            <div id="block1" class="block" onclick="blockClicked('block1')">Блок 1</div>
            <div id="block2" class="block" onclick="blockClicked('block2')">Блок 2</div>
            <div id="block3" class="block" onclick="blockClicked('block3')">Блок 3</div>
        </div>
    </body>
    </html>
    """
    return html_content


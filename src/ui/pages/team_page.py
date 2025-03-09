import streamlit as st
import base64
import asyncio

import gettext
import os
from streamlit.components.v1 import html


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


def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string


def display_team_member(photo, name, education, social_media, orcid, researchgate):
    photo = load_image_as_base64(photo)
    st.markdown(
        f"""
        <div style='border: 2px solid #D3D3D3; padding: 10px; border-radius: 10px; text-align: center;'>
            <img src='data:image/png;base64,{photo}' style='width: 200px; border-radius: 50%; margin-bottom: 10px;'/>
            <h3>{name}</h3>
            <p><strong>Education:</strong> {education}</p>
            <p><a href='{social_media}'>Social media</a></p>
            <p><a href='{orcid}'>ORCID</a></p>
            <p><a href='{researchgate}'>ResearchGate</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )


def generate_team_html(team_data):
    # Загружаем SVG-иконки в Base64
    telegram_icon = load_image_as_base64("src/ui/logos/telegram-svgrepo-com.svg")
    researchgate_icon = load_image_as_base64("src/ui/logos/researchgate-svgrepo-com.svg")
    orcid_icon = load_image_as_base64("src/ui/logos/orcid.logo.svg")

    html = """
    <style>
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            padding: 20px;
        }
        .team-card {
            width: 370px;
            border-radius: 12px;
            text-align: center;
            padding: 25px;
            transition: transform 0.3s, box-shadow 0.3s;
            background: rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(10px);
            font-family: Arial, sans-serif;
        }
        .team-card:hover {
            transform: scale(1.05);
        }
        .team-photo {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 15px;
        }
        .team-name {
            font-size: 32px;
            font-weight: Semi Bold;
            margin-bottom: 5px;
            color: dark;
            font-family: monospace;
        }
        .team-description {
            font-size: 18px;
            font-weight: normal;
            margin-bottom: 10px;
            color: dark;
            font-family: monospace;
        }
        .team-email {
            font-size: 20px;
            font-weight: normal;
            margin-bottom: 15px;
            color: dark;
        }
        .social-links {
            display: flex;
            justify-content: center;
            gap: 12px;
        }
        .social-links a {
            display: inline-block;
        }
        .social-links img {
            width: 50px;
            height: 50px;
            transition: transform 0.3s;
        }
        .social-links img:hover {
            transform: scale(1.2);
        }
    </style>
    <div class='team-container'>
    """

    for name, info in team_data.items():
        photo_base64 = load_image_as_base64(info['photo'])
        html += f"""
        <div class='team-card'>
            <img src='data:image/png;base64,{photo_base64}' class='team-photo' alt='{name}'>
            <h2 class='team-name'>{name}</h2>
            <h5 class='team-description'>{info['description']}</h5>
            <div class='social-links'>
                <a href='{info['telegram']}' target='_blank'>
                    <img src='data:image/svg+xml;base64,{telegram_icon}' alt='Telegram'>
                </a>
                <a href='{info['researchgate']}' target='_blank'>
                    <img src='data:image/svg+xml;base64,{researchgate_icon}' alt='ResearchGate'>
                </a>
                <a href='{info['orcid']}' target='_blank'>
                    <img src='data:image/svg+xml;base64,{orcid_icon}' alt='ORCID'>
                </a>
            </div>
            <p class='team-email'>📧 <a href='mailto:{info['email']}' style='color:#03118f; text-decoration: none;'>{info['email']}</a></p>

        </div>
        """

    html += "</div>"
    return html


def team_page():
    _ = set_language(st.session_state.language)
    team_text = _('Наша команда')
    st.markdown(f"<h1 style='text-align: center;'>{team_text}</h1>", unsafe_allow_html=True)
    st.write(' ')

    photo1 = "src/ui/logos/Savvin_Nikita.png"
    name1 = _("Никита Саввин")
    education1 = _("Магистр технологии искусственного интеллекта")
    social_media1 = "https://t.me/Nextian"
    orcid1 = "https://orcid.org/0009-0009-9163-6234"
    researchgate1 = "https://www.researchgate.net/profile/Nikita-Savvin-2"

    photo2 = "src/ui/logos/Dmitrii-Vasenin.jpg"
    name2 = _("Дмитрий Васенин")
    education2 = _("PhD. В области технологий для здравоохранения")
    social_media2 = "https://t.me/dvasenin"
    orcid2 = "https://orcid.org/0000-0002-7028-9984"
    researchgate2 = "https://www.researchgate.net/profile/Dmitrii-Vasenin?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InByb2ZpbGUiLCJwYWdlIjoicHJvZmlsZSJ9fQ"

    team_data = {
        name1: {
            "photo": photo1,
            "description": education1,
            "telegram": social_media1,
            "researchgate": researchgate1,
            "orcid": orcid1,
            'email': 'savvin.nikita.work@yandex.ru'
        },
        name2: {
            "photo": photo2,
            "description": education2,
            "telegram": social_media2,
            "researchgate": researchgate2,
            "orcid": orcid2,
            'email': 'vasenindmitrij01@gmail.com '
        }
    }

    html_output = generate_team_html(team_data)
    with st.container(height=720, border=False, key='castom_header'):
        html(html_output, height=700)

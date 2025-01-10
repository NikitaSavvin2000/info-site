import streamlit as st
import base64
import asyncio


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


def team_page():
    st.markdown("<h1 style='text-align: center;'>Наша команда</h1>", unsafe_allow_html=True)
    st.write(' ')

    photo1 = "src/ui/logos/Savvin_Nikita.png"
    name1 = "Никита Саввин"
    education1 = "Master of Computer Science"
    social_media1 = "https://twitter.com/Nextian"  # Используем ссылку вместо текста
    orcid1 = "https://orcid.org/0009-0009-9163-6234"
    researchgate1 = "https://www.researchgate.net/profile/Nikita-Savvin-2"

    photo2 = "src/ui/logos/Dmitrii-Vasenin.jpg"
    name2 = "Дмитрий Васенин"
    education2 = "PhD. Candidate in Technology for Health"
    social_media2 = "-"
    orcid2 = "https://orcid.org/0000-0002-7028-9984"
    researchgate2 = "https://www.researchgate.net/profile/Dmitrii-Vasenin?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InByb2ZpbGUiLCJwYWdlIjoicHJvZmlsZSJ9fQ"

    columns = st.columns(spec=[1, 8, 8, 1])
    col1 = columns[1]
    col2 = columns[2]

    with col1:
        display_team_member(photo1, name1, education1, social_media1, orcid1, researchgate1)
    with col2:
        display_team_member(photo2, name2, education2, social_media2, orcid2, researchgate2)

#
# if __name__ == "__main__":
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     try:
#         asyncio.run(team_page())
#     except KeyboardInterrupt:
#         pass
#     finally:
#         loop.close()

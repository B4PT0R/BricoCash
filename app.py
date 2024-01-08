import streamlit as st
import os
import json, toml
import base64

_root_=os.path.dirname(os.path.abspath(__file__))
def root_join(*args):
    return os.path.join(_root_,*args)


state=st.session_state

st.text("v0.1")

if not 'locations' in state:
    with open('locations.json','r') as f:
        state.locations=json.load(f)

if not 'theme' in state:
    with open(root_join(".streamlit/config.toml")) as f:
        data=toml.load(f)
        state.theme=data['theme']

def vspace():
    return st.markdown("""<p><br></p>""",unsafe_allow_html=True)

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_centered_image(image_path, **img_css_styles):
    # Convert image to base64
    base64_image = get_image_base64(image_path)

    # Convert the img styles dictionary to a CSS string
    img_style_string = '; '.join([f"{key}: {value}" for key, value in img_css_styles.items()])

    # Inject CSS with st.markdown, escaping curly braces for the CSS
    st.markdown(f"""
        <style>
        .centered-image-div {{
            width: 100%;
            display: flex;
            justify-content: center;
        }}
        </style>
        """, unsafe_allow_html=True)

    # Display the image as base64
    st.markdown(f"<div class='centered-image-div'><img src='data:image/png;base64,{base64_image}' style='{img_style_string}'></div>", unsafe_allow_html=True)

display_centered_image(root_join("app_images/bricocash_logo.png"),width='250px',height='150px')

st.write("---")

st.header("Brico Cash Yvetot vous souhaite la bienvenue !")

st.write("---")

st.subheader("Vous cherchez un rayon ?")
product=st.selectbox(label="Type de produit",options=["",*state.locations.keys()])

if product and (product in state.locations):
    st.write(f"Vous trouverez ce produit {state.locations[product]}.")




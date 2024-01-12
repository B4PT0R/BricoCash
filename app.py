import streamlit as st
import os
import json, toml
import base64
from objdict_bf import objdict
import time

_root_=os.path.dirname(os.path.abspath(__file__))
def root_join(*args):
    return os.path.join(_root_,*args)

state=st.session_state

st.set_page_config(page_title="Brico Cash", page_icon=root_join("app_images/bricocash_logo.png"), initial_sidebar_state='collapsed')

if not 'locations' in state:
    with open('locations.json','r') as f:
        state.locations=json.load(f)

if not 'theme' in state:
    with open(root_join(".streamlit/config.toml")) as f:
        data=toml.load(f)
        state.theme=data['theme']

if not 'page' in state:
    state.page='Accueil'

if not 'data' in state:
    state.data=objdict.load(_file=root_join("app_data/data.json"))


#............Utility functions----------------

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

#----------------------Layout functions---------------------


def make_welcome():
    display_centered_image(root_join("app_images/bricocash_logo.png"),width='250px',height='150px')
    st.write("---")
    st.header("Le Brico Cash d'Yvetot et toute son équipe vous souhaitent la bienvenue !")
    st.write("---")

    st.subheader("Comment utiliser l'appli:")
    st.write("Cette application a pour but de vous aider à trouver le produit qui vous intéresse dans le magasin.")
    st.write("Pour naviguez sur les différentes pages de l'appli, dépliez le bandeau latéral en cliquant sur le petit chevron en haut à gauche de la page.")

def make_menu():
    with st.sidebar:
        display_centered_image(root_join("app_images/bricocash_logo.png"),width='90px',height='60px')
        vspace()
        if st.button("Accueil",use_container_width=True):
            state.page="Accueil"
            st.rerun()
        if st.button("Rechercher",use_container_width=True):
            state.page="Recherche"
            st.rerun()
        if st.button("Plan du magasin",use_container_width=True):
            state.page="Plan"
            st.rerun()
        if st.button("Promos",use_container_width=True):
            state.page="Promos"
            st.rerun()

def make_content():
    st.header("Vous cherchez un produit ?")
    st.write('---')
    st.subheader("Recherche par code EAN (code barre)")
    st.text_input("Entrez le code à EAN à 13 chiffres:",key="EAN")
    if 'EAN' in state and state.EAN:
        if len(state.EAN)!=13 or not all(c in [str(i) for i in range(10)] for c in state.EAN):
            st.warning("Le code EAN doit comporter 13 chiffres.")
    st.button("Rechercher", key="EAN_search")
    if 'EAN_search' in state and state.EAN_search:
        st.info("Votre produit se trouve: ICI")

    st.write('---')
    st.subheader("Recherche par secteurs/rayon")
    product=st.selectbox(label="Type de produit",options=["",*state.locations.keys()])

    if product and (product in state.locations):
        st.write(f"Vous trouverez ce produit {state.locations[product]}.")

def make_promo():
    st.subheader("Profitez toute l'année de nos offres à prix imbattable !")
    st.write("---")
    for promo in state.data.promos:
        with st.container(border=True):
            if promo.title:
                st.subheader(promo.title)
            if promo.image:
                display_centered_image(promo.image,width='75%')
            if promo.content:
                st.write(promo.content)
            if promo.price:
                st.metric("Prix:",promo.price)
    



def make_plan():
    st.subheader("Consulter un plan :")
    with st.expander("Cliquez pour ouvrir le plan."):
        st.image(root_join("app_images/plan.png"))


make_menu()

st.subheader(state.page)

e=st.empty()
with e.container(height=800):
    if state.page=="Accueil":
        make_welcome()
    elif state.page=="Recherche":
        make_content()
    elif state.page=="Promos":
        make_promo()
    elif state.page=="Plan":
        make_plan()

st.caption("©Brico Cash Yvetot 2024 v0.1")
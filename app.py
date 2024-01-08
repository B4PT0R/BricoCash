import streamlit as st
import os
import json

_root_=os.path.dirname(os.path.abspath(__file__))
def root_join(*args):
    return os.path.join(_root_,*args)


state=st.session_state

if not 'locations' in state:
    with open('locations.json','r') as f:
        state.locations=json.load(f)

def vspace():
    return st.markdown("""<p><br></p>""",unsafe_allow_html=True)

_,c,_=st.columns([27,46,27])
with c:
    st.image(root_join("app_images/bricocash_logo.png"),width=200)

st.write("---")

st.header("Brico Cash Yvetot vous souhaite la bienvenue !")

st.write("---")

st.write("Vous cherchez un rayon ?")
product=st.selectbox(label="Type de produit",options=["","peinture","quincaillerie","électro-portatif"])



if product and (product in state.locations):
    st.write(f"Vous trouverez ce produit {state.locations[product]}.")




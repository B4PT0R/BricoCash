import streamlit as st
import os
from objdict_bf import objdict

_root_=os.path.dirname(os.path.abspath(__file__))
def root_join(*args):
    return os.path.join(_root_,*args)

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

location=objdict.load("locations.json")

if product and (product in location):
    st.write(f"Vous trouverez ce produit {location[product]}.")




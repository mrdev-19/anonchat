import streamlit as st
from streamlit_option_menu import option_menu
import database as db
# import validations as val
import time
#---------------------------------------------------

page_title="Anonymous Chat Room"
page_icon=""
layout="centered"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)

#--------------------------------------------------
#hide the header and footer     

hide_ele="""
        <style>
        #Mainmenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """
st.markdown(hide_ele,unsafe_allow_html=True)

#--------------------------------------------------


#--------------------------------------------------


def main():
        with st.form("room",clear_on_submit=True):  
            roomname=st.text_input("Enter/Create a Room >> ")
            sub=st.form_submit_button("Submit")
            if(sub):
                if(db.check_room(roomname)):
                    st.session_state["roomname"]=roomname
                    st.session_state["key"]="room"
                    st.experimental_rerun() 
                else:
                    db.create_room(roomname)
                    st.session_state["key"]="room"
                    st.session_state["roomname"]=roomname
                    st.experimental_rerun()

def room():
    for i in db.getmsgstack(st.session_state["roomname"]):
         st.write(i)
    er=st.button("Exit Room")
    if(er):
         st.session_state["roomname"]=""
         st.session_state["key"]="main"
         st.experimental_rerun()

if "key" not in st.session_state:
   st.session_state["key"]="main"

if(st.session_state["key"]=="main"):
     main()
else:
     room()
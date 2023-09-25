import streamlit as st
import random
import time

st.set_page_config(page_title="GPI Test",
                   page_icon="🧪",
                   layout="centered")

if 'page' not in st.session_state:
    st.session_state['page'] = 0


if st.session_state['page'] == 0:

    st.header(":blue[Welcome to `GPI` Test]")
    st.caption("an image for information")
    st.caption("Some Description about the test")


    st.divider()
    st.subheader(":one: Personal Details")
    personalinfo = {}

    personalinfo['name'] = st.text_input("Name")
    personalinfo['phone'] = st.text_input("Phone")
    personalinfo['roll'] = st.text_input("Roll")

    def nextpage():
        st.session_state['page']+=1
    st.button("Go to Next Page",on_click=nextpage)

elif st.session_state['page'] == 1:
    
    st.header(":two: GPI Test")
    
    options=['option-1','option-2','option-3','option-4']
    st.radio("Single Choice Question",options=options)
    
    st.write("Multiple choice Question")
    for o in options:
        st.checkbox(o)
    
    st.text_input("One Line Answers")
    st.text_area("Answer in Paragraph")

    value=st.slider("Question like on a scale of 0 to 10",min_value=0,max_value=10)
    
    def next():
        st.session_state['page'] += 1
    st.button("Next",on_click=next)

elif st.session_state['page'] == 2:
    st.header(":three: Result")
    left,right = st.columns(2)
    with left:
        st.metric(f"GPI Score",value=random.randint(0,100))
    with right:
        st.caption("Here we can display typical GPI Scores and some comments")
    st.divider()
    st.subheader("What Next")

    st.checkbox("I Wish to improve my GPI")
    st.radio("Frequency of Session I can attend",
             options=['Weekly once',
                      'Once in Two Week',
                      'Monthly Once'])
    def invite():
        st.session_state['page']  +=1
    st.button("Invite me as per above options",on_click=invite)

elif st.session_state['page'] ==3:
    st.header("Thank You for Participating")
    st.balloons()
    time.sleep(2)
    st.snow()
    time.sleep(2)
    # st.image("https://ih1.redbubble.net/image.3230143366.1259/poster,504x498,f8f8f8-pad,600x600,f8f8f8.u1.jpg",
    #          width=500)
    # st.balloons()
    # time.sleep(2)
    # st.balloons()
    # time.sleep(2)
    # st.balloons()
    # time.sleep(2)
    # st.balloons()
import streamlit as st
import random
import time
import pandas as pd

from helper_google import append_data

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

    personalinfo = {'valid_input':False}
    
    personalinfo['name'] = st.text_input("Name")
    personalinfo['phone'] = st.text_input("Whatsapp Number")
    personalinfo['email'] = st.text_input("Email")
    personalinfo['branch'] = st.text_input("Branch")
    personalinfo['Year of Study'] = st.selectbox("Year of Stuy",
                                                 options=['1st Year',
                                                          '2nd Year',
                                                          '3rd Year',
                                                          '4th Year',
                                                          '5th Year'],
                                                          index=0)
    st.subheader(":two: Goodness Passion Ignorance")
    if 'questions' not in st.session_state:
        question_data = pd.read_excel('./question.xlsx',sheet_name='Sheet1')
        qbank = []
        for index,row in question_data.iterrows():
            qbank.append({'question':row['Questions'],
                            'goodness':row['Goodness'],
                            'passion':row['Passion'],
                            'ignorance':row['Ignorance']})
        st.session_state['questions'] = qbank
    
    user_answer = ""
    answer_to_submit = {}
    for i,item in enumerate(st.session_state['questions'],start=1):
        answer = st.radio(f") {i}. :green[{item['question']}]",
                 options=['',
                          item['goodness'],
                          item['passion'],
                          item['ignorance']],
                          index=0)
        if answer == item['goodness']:
            user_answer += 'g'
        elif answer == item['passion']:
            user_answer += 'p'
        elif answer == item['ignorance']:
            user_answer += 'i'
        else:
            user_answer += 'n'
        answer_to_submit[item['question']] = answer
        st.caption(user_answer[-1])
    
    st.checkbox("I Would Like To attend such sessions in future")
    



    total_length = len(user_answer)
    goodness_component = user_answer.count('g')/total_length
    passion_component = user_answer.count('p')/total_length
    ignorance_component = user_answer.count('i')/total_length
    notsure_component = user_answer.count('n')/total_length

    
    st.divider()
    left,middle,right = st.columns(3)
    
    with left:
        st.markdown("#### Goodness")
        st.metric("",f'{goodness_component:.2%}')
    with middle:
        st.markdown("#### Passion")
        st.metric("",f'{passion_component:.2%}')
    with right:
        st.markdown("#### Ignorance")
        st.metric("",f'{ignorance_component:.2%}')

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
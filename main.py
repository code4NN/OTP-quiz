import streamlit as st
import random
import time
import re
import pandas as pd

from helper_google import append_data

st.set_page_config(page_title="GPI Test",
                   page_icon="🧪",
                   layout="centered")

st.markdown("""<style>[data-testid="stHeader"]{
            display:none
                }
            footer{
            display:none
            }
            a[href="https://streamlit.io/cloud"]{
            display:none
            }
            </style>""",unsafe_allow_html=True)


if 'page' not in st.session_state:
    st.session_state['page'] = 0

def is_valid_mobile_number(number):
    # Regular expression to match a 10-digit mobile number starting with digits 6-9
    pattern = r'^[6-9][0-9]{9}$'

    # Check if the input matches the pattern
    if re.match(pattern, number):
        return [True,-1]
    else:
        if len(number)!=10:
            return [False,"Should Be of 10 Digit"]
        elif number[0] not in '6789':
            return [False,'Indian Number cannot start with ' + number[0]]
        else:
            return [False,"Not a Valid Number"]
def is_valid_gmail(email):
    # Regular expression to match a Gmail address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the input matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False



if st.session_state['page'] == 0:

    st.header(":blue[Welcome to GPI(]Goodness :red[Passion] :violet[Ignorance] :blue[index) Self Assessment]")
    # st.caption("an image for information")
    # st.markdown(":one: Fill In Personal Details")
    # st.markdown(":two: Answer Some Questions")
    # st.markdown(":three: Evaluate Your GPI Score")

    DISABLED = True if 'form_submitted' in st.session_state else False

    st.divider()
    # st.subheader(":one: Personal Details")

    personalinfo = {'valid_input':True}
    incomplete_field = []
    FINAL_SUBMIT = []
    st.markdown(
            '<div id="incomplete-1" style="height: 0;"></div>',
            unsafe_allow_html=True,
        )
    personalinfo['name'] = st.text_input("Name",disabled=DISABLED)
    FINAL_SUBMIT.append(personalinfo['name'])
    if not personalinfo['name']:
        st.caption("Please Enter Name")
        personalinfo['valid_input'] = False
        incomplete_field.append("Name")
    st.markdown("")
    st.markdown("")

    personalinfo['phone'] = st.text_input("Whatsapp Number",disabled=DISABLED)
    personalinfo['phone'] = personalinfo['phone'].strip()
    FINAL_SUBMIT.append(personalinfo['phone'])
    if not personalinfo['phone']:
        st.caption("Please Enter Whatsapp Number without +91")
        personalinfo['valid_input'] = False
        incomplete_field.append("Number")

    elif not is_valid_mobile_number(personalinfo['phone'])[0]:
        st.markdown(f":red[{is_valid_mobile_number(personalinfo['phone'])[1]}]")
        if st.checkbox("I Want to Proceed Anyway",key='valid phone'):
            personalinfo['valid_input'] = True and personalinfo['valid_input']
        else:
            personalinfo['valid_input'] = False
            incomplete_field.append("Number")
    st.markdown("")
    st.markdown("")

    personalinfo['email'] = st.text_input("Email",disabled=DISABLED)
    personalinfo['email'] = personalinfo['email'].strip()
    FINAL_SUBMIT.append(personalinfo['email'])
    if not personalinfo['email']:
        st.caption("Please Enter Email")
        personalinfo['valid_input'] = False
        incomplete_field.append("Email")
    elif not is_valid_gmail(personalinfo['email']):
        st.markdown(":red[Not a Valid Email]")        
        if st.checkbox("I want to Proceed Anyway",key='valid email'):
            personalinfo['valid_input'] = personalinfo['valid_input'] and True
        else:
            personalinfo['valid_input'] = False
            incomplete_field.append("Email")
    st.markdown("")
    st.markdown("")

    personalinfo['degree'] = st.radio("Degree",
                                      options=['B. Tech',
                                               'M. Tech',
                                               'Dual Degree',
                                               'B. S',
                                               'PhD',
                                               'Staff',
                                               'Other'],
                                               index=0,
                                               disabled=DISABLED,
                                               horizontal=True)
    FINAL_SUBMIT.append(personalinfo['degree'])
    st.markdown("")
    st.markdown("")

    personalinfo['branch'] = st.text_input("Branch",disabled=DISABLED)
    FINAL_SUBMIT.append(personalinfo['branch'])
    if not personalinfo['branch']:
        st.caption("Please Enter Branch")
        personalinfo['valid_input'] = False
        incomplete_field.append("Branch")
    st.markdown("")
    st.markdown("")
    personalinfo['Year of Study'] = st.selectbox("Year of Stuy",
                                                 options=['1st Year',
                                                          '2nd Year',
                                                          '3rd Year',
                                                          '4th Year',
                                                          '5th Year'],
                                                          index=0,disabled=DISABLED)
    st.markdown("")
    st.markdown("")
    FINAL_SUBMIT.append(personalinfo['Year of Study'])

    if False:
        st.markdown("#### :red[Please Complete Personal Details to Proceed]")
    else:

        st.subheader("Goodness Passion Ignorance")

        if 'questions' not in st.session_state:
            question_data = pd.read_excel('./question.xlsx',sheet_name='Sheet1')
            qbank = []
            for index,row in question_data.iterrows():
                qbank.append({
                    'qid': row['order'],
                    'question':row['Question'],
                    'goodness':row['Goodness'],
                    'passion':row['Passion'],
                    'ignorance':row['Ignorance'],
                    'options': random.sample([row['Goodness'],
                                              row['Passion'],
                                              row['Ignorance']],3)})
            random.shuffle(qbank)
            st.session_state['questions'] = qbank
        
        user_answer = ""
        answer_to_submit = []
        not_answered = []
        for i,item in enumerate(st.session_state['questions'],start=1):
            st.markdown(f"##### :orange[{i}.] :blue[{item['question']}]")
            answer = st.radio(f"### ) {i}. :green[{item['question']}]",
                    options=[
                            *item['options'],
                            ""],
                            index=3,
                            label_visibility='hidden',
                            disabled=DISABLED)
            if answer == item['goodness']:
                user_answer += 'g'
            elif answer == item['passion']:
                user_answer += 'p'
            elif answer == item['ignorance']:
                user_answer += 'i'
            else:
                user_answer += 'n'
                not_answered.append(i)
            # st.caption(answer)
            answer_to_submit.append({'qid':item['qid'],
                                    'response':answer})
            # st.caption(user_answer[-1])
        answer_to_submit.sort(key=lambda x: x['qid'],reverse=False)

        FINAL_SUBMIT.extend([item['response'] for item in answer_to_submit])
        
        st.markdown("##### :blue[I Would Like to Attend Such Discussions in Future]")
        interest = st.radio("asdf",
                            options=['Yes, Eagerly Looking for It',
                                     'Yes, sometimes',
                                     'Maybe, Need to think',
                                     'Other'
                                     ],
                                     label_visibility='hidden',
                                     disabled=DISABLED)
        if interest =='Other':
            interest = st.text_input("Please Mention",disabled=DISABLED)
            if not interest:
                incomplete_field.append("I Would Like to ...")
            FINAL_SUBMIT.append(interest)
        else :
            FINAL_SUBMIT.append(interest)

        st.markdown("##### :blue[Please Share Your Comments/Appreciations/Suggestions] :orange[Can also mention striking points you learnt today]")
        comments=st.text_area(":blue[Please give if any comments/appreciations/suggestions regarding session. :orange[Also can share striking points you learnt today]]",
                     height=180
                     ,disabled=DISABLED,
                     label_visibility='hidden')
        if not comments:
            comments = "No Comments"
        FINAL_SUBMIT.append(comments)
        
        
        # st.write(FINAL_SUBMIT)

        def form_submit(responses):
            result = append_data(FINAL_SUBMIT)
            if result =='success':
                st.session_state['form_submitted'] = True
        if 'form_submitted' not in st.session_state:
            if incomplete_field:
                st.divider()
                st.markdown(":red[Please Complete These Fields[Click To Scroll](#incomplete-1) to Continue]")
                # st.caption("Incomplete Fields")
                for i in incomplete_field:
                    st.markdown(f':green[{i}]')
            if not_answered:
                st.divider()
                st.error("Please Answer All the Questions to Evaluate")
                st.markdown(f"##### :blue[You have Not Answered for Following :orange[{len(not_answered)}] Questions]")
                st.caption("Question Numbers")
                st.caption('-----'.join([str(i) for i in not_answered]))
                # for i in not_answered:
                #     st.write(i)

            elif (not incomplete_field) and (not not_answered):
                st.button("Evaluate my Scores",on_click=form_submit,
                    args=[FINAL_SUBMIT])

        total_length = len(user_answer)
        goodness_component = user_answer.count('g')/total_length
        passion_component = user_answer.count('p')/total_length
        ignorance_component = user_answer.count('i')/total_length
        notsure_component = user_answer.count('n')/total_length

        
        st.divider()
        left,middle,right = st.columns(3)
        if 'form_submitted' in st.session_state:
            st.header("Components of your personality")
            with left:
                st.markdown("#### Goodness")
                st.metric("",f'{goodness_component:.2%}')
            with middle:
                st.markdown("#### Passion")
                st.metric("",f'{passion_component:.2%}')
            with right:
                st.markdown("#### Ignorance")
                st.metric("",f'{ignorance_component:.2%}')
            
            st.header("Thank You for Participating")
            st.balloons()
            time.sleep(2)
            st.snow()
            time.sleep(2)
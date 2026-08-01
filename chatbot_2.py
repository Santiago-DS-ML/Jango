
import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title='Jango')
st.title('JANGO')
st.markdown("Discutez avec votre chatbot **JANGO**. Posez toutes vos questions. ")

#Création du client gemini
client=genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

#création de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages=[]

#Affichage de l'historique
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

#Gestion de l'input utilisateur
if user_question := st.chat_input('Poser une question'):
    with st.chat_message('user'):
        st.markdown(user_question)
    st.session_state.messages.append({'role': 'user', 'content': user_question})

#Gestion de la réponse llm
  #conversion de l'historique adapté au llm
    system_prompt = """XHDFLJVJSJK"""
    history=[]
    for msg in st.session_state.messages:
        history.append({
        'role': msg['role'],
        'parts':[{'text':msg['content']}]
    })

    #Réponse en streaming
    stream= client.models.generate_content_stream(
    model= "gemini-2.5-flash",
    content= history,
    config= {
        "system_instruction": system_prompt,
        "temperature":0.3,
        "max_output_tokens":200
    })

    response = st.write_stream(
        chunk.text for chunk in stream
    )
    with st.chat_message('assistant'):
        st.markdown(response)
    st.session_state.messages.append(
    {"role": "assistant", "content": response})

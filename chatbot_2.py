
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title='Jango')
st.title('JANGO')
st.markdown("Bienvenue sur **JANGO**, votre assistant conversationnel intelligent. Posez vos questions sur les produits, services ou informations de l'entreprise. JANGO fournit des réponses claires, précises et adaptées à votre demande grâce à l'intelligence artificielle. ")

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

#Sidebar
with st.sidebar: 
    st.title('⚙️ Paramètres')
    st.markdown("---")
    temperature = st.slider(
        "Température",
        min_value=0.0,
        max_value=2.0,
        value=0.3,
        step=0.1
    )

    max_tokens = st.slider(
        "Max Output Tokens",
        min_value= 100,
        max_value= 2000,
        value= 500,
        step=100
    )
    st.markdown("---")
    if st.button("🗑️ Supprimer l'historique"): 
        st.session_state.messages=[] 
        st.rerun()

    
#Gestion de la réponse llm
  #conversion de l'historique adapté au llm
    system_prompt = """
Tu es JANGO, l'assistant virtuel officiel de TechNova Store, une entreprise spécialisée dans la vente de produits informatiques et électroniques.

Ta mission est d'aider les clients à obtenir rapidement des informations sur les produits, les commandes, les paiements et les services.

=========================
À propos de TechNova Store
=========================

TechNova Store est une boutique spécialisée dans la vente de matériel informatique.

Nos horaires sont :
- Lundi au vendredi : 8h00 - 18h00
- Samedi : 9h00 - 15h00
- Fermé le dimanche

Adresse :
15 Avenue de l'Innovation, Abidjan, Côte d'Ivoire

Téléphone :
+225 07 00 00 00 00

Email :
contact@technovastore.com

Livraison :
- Abidjan : sous 24 heures
- Intérieur du pays : 2 à 4 jours ouvrés

Modes de paiement :
- Orange Money
- MTN Money
- Wave
- Carte bancaire
- Paiement à la livraison (Abidjan uniquement)

Garantie :
Tous les produits disposent d'une garantie constructeur de 12 mois.

=========================
Produits disponibles
=========================

1. Laptop Pro X15
- Intel Core i7
- 16 Go RAM
- SSD 512 Go
- Écran 15.6"
- Prix : 850 000 FCFA

2. UltraBook Air 14
- Intel Core i5
- 8 Go RAM
- SSD 256 Go
- Prix : 520 000 FCFA

3. Gaming Beast G7
- AMD Ryzen 7
- RTX 4060
- 32 Go RAM
- SSD 1 To
- Prix : 1 450 000 FCFA

4. Wireless Mouse MX
- Souris Bluetooth
- Rechargeable USB-C
- Prix : 25 000 FCFA

5. Mechanical Keyboard K80
- Clavier mécanique RGB
- Switch Blue
- Prix : 65 000 FCFA

6. Écran UltraView 27"
- IPS
- 144 Hz
- 2K
- Prix : 210 000 FCFA

=========================
Consignes
=========================

Tu réponds toujours en français.

Tu es poli, professionnel et bienveillant.

Lorsque le client demande des informations sur un produit, présente :
- les principales caractéristiques,
- le prix,
- les avantages.

Lorsque le client compare deux produits, réalise un tableau comparatif.

Si une information n'est pas disponible, indique honnêtement que tu ne la connais pas.

N'invente jamais de produits ni de prix.

Lorsque cela est pertinent, termine la réponse par une proposition d'aide, par exemple :
"Puis-je vous aider à choisir le produit le plus adapté à votre besoin ?"

Ton objectif est d'offrir une excellente expérience client.
"""
    history=[]
    for msg in st.session_state.messages:
        history.append({
        "role": "model" if msg["role"] == "assistant" else "user",
        "parts": [{"text": msg["content"]}]
    })

    #Réponse en streaming
    stream= client.models.generate_content_stream(
    model= "gemini-2.5-flash",
    contents= history,
    config= types.GenerateContentConfig(
        system_instruction= system_prompt,
        temperature= temperature,
        max_output_tokens= max_tokens
    ))

    with st.chat_message('assistant'):
         response = st.write_stream(
        chunk.text for chunk in stream
    )
    st.session_state.messages.append(
    {"role": "assistant", "content": response})


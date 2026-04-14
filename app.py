import streamlit as st
from groq import Groq
import re

# 1. Page Setup
st.set_page_config(page_title="Grand Stay Support", page_icon="🏨")
st.title("🏨 Grand Stay Hotel Support")
st.caption("Hotel Assistant Chatbot")

# 2. Groq Client (put your API key)
client = Groq(api_key="YOUR_API_KEY_HERE")

# 3. System Message
system_message = {
    "role": "system",
    "content": (
        "You are a helpful hotel assistant for 'Grand Stay Hotel'. "
        "Only answer hotel-related questions (rooms, booking, pricing, facilities). "
        "If unrelated, say: 'I can only assist with hotel-related queries.' "
        "Rooms: Deluxe ($150), Suite ($300), Penthouse ($500). "
        "Facilities: Rooftop pool, Gym, Free Breakfast. "
        "Check-in: 3 PM, Check-out: 11 AM."
    )
}

# 4. Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [system_message]

# 5. Display chat
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# 6. Keywords and greetings
hotel_keywords = [
    "room", "rooms", "booking", "book", "price", "cost",
    "hotel", "stay", "check", "check-in", "check-out",
    "facility", "facilities", "gym", "pool", "breakfast",
    "suite", "deluxe", "penthouse", "available"
]

greetings = ["hi", "hello", "hey"]

# 7. Chat input
if prompt := st.chat_input("Ask about rooms, booking, facilities..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower()

    # 🔑 FIX: Proper word splitting (avoids 'hi' inside 'which')
    words = re.findall(r'\b\w+\b', prompt_lower)

    with st.chat_message("assistant"):

        # ✅ Greeting check (correct)
        if any(greet in words for greet in greetings):
            response_text = "Hello! 😊 Welcome to Grand Stay Hotel. How can I assist you today?"

        # ✅ Allow short queries (like: facilities, rooms)
        elif len(words) <= 2:
            allow_query = True

        # ✅ Keyword check
        else:
            allow_query = any(word in prompt_lower for word in hotel_keywords)

        # ✅ Final decision
        if 'response_text' not in locals():
            if not allow_query:
                response_text = "I can only assist with hotel-related queries."
            else:
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model="llama-3.1-8b-instant",
                    temperature=0.2,
                    max_tokens=300,
                )
                response_text = chat_completion.choices[0].message.content

        st.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})
import streamlit as st

st.title("Michael's Portfolio")

st.write("Python Developer|Javascript Developer|AI Developer")

col1, col2 = st.columns(2)
with col1:
    st.image("ronaldo.jpeg")

with col2:
    st.subheader("Key Values")
    st.write("Integrity: Being honest and having strong moral principles")
    st.write("Honesty: Being truthful and transparent in all interactions")
    st.write("Responsibility: Taking ownership of one's actions and decisions")
    st.write("Kindness: Showing compassion and empathy towards others")
    st.write("Growth: Continuously developing and improving oneself ")

    st.subheader("General Information")
    st.write("Hi i'm Michael this is a brief history of my new adventure to a new world ")


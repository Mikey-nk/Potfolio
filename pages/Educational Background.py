import streamlit as st

st.title("Educational Background")

col1, col2 = st.columns(2)
with col1:
    st.subheader("1")
    st.subheader("Bachelor of Science")
with st.expander("Click to see more details"):
    st.write("Summit Grove School")
    st.write("Riverstone Academy")
    st.write("Willowbrook Institute")
    st.write("Starlight Academy")

with col2:
    st.subheader("2")
    st.subheader("Bootcamp")
with st.expander("Click to see more details"):
    st.write("Blue Sky Institute")
    st.write("Clearview Academy")
    st.write("Pine Valley Academy")
    st.write("Sunrise Learning Institute")



coll1, coll2 = st.columns(2)
with coll1:
    st.subheader("3")
    st.subheader("High-school")
with st.expander("Click to see more details"):
    st.write("Evergreen Hills School")
    st.write("Harborview School")
    st.write("Mountain Peak Academy")
    st.write("New Horizons School")

with coll2:
    st.subheader("4")
    st.subheader("Primary-school")
with st.expander("Click to see more details"):
    st.write("Bright Path School")
    st.write("Redwood Academy")
    st.write("Golden Fields Academy")
    st.write("Clear Sky School")
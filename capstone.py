import streamlit as st

# Title
st.title("🧠 Capstone TEST")

# Description
st.markdown("Welcome! Please enter customer name and describe the situation.")

# Input fields
name = st.text_input("👤 Customer Name:")
user_input = st.text_area("📝 Describe the situation:")

# Submit button
if st.button("Submit"):
    if name and user_input:
        st.success("✅ Submission received!")
        st.write(f"**Name:** {name}")
        st.write(f"**Input:** {user_input}")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")





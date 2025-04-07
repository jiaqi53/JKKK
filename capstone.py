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



import streamlit as st
import mysql.connector

# Title
st.title("🧠 Capstone TEST")

# Description
st.markdown("Welcome! Please enter customer name and describe the situation.")

# Input fields
name = st.text_input("👤 Customer Name:")
user_input = st.text_area("📝 Describe the situation:")

# ✅ 定義資料庫寫入 function（修正欄位名稱）
def insert_to_db(name, user_input):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aa53123405",  
            database="capstone"
        )
        cursor = conn.cursor()
        query = "INSERT INTO assessment (UserName, input_text) VALUES (%s, %s)"
        values = (name, user_input)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        st.error(f"❌ Database Error: {e}")
        return False

# Submit button
if st.button("Submit"):
    if name and user_input:
        success = insert_to_db(name, user_input)
        if success:
            st.success("✅ Submission received and saved to database!")
            st.write(f"**Name:** {name}")
            st.write(f"**Input:** {user_input}")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")

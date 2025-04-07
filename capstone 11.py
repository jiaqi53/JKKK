

import streamlit as st
import mysql.connector

# 🔁 Simulated AI function for testing without OpenAI credits
def categorize_input(text):
    # Fake AI logic based on keywords — can be replaced later with OpenAI
    if "trust" in text.lower():
        return "Category: Leadership\nTags: [trust, communication, teamwork]"
    elif "strategy" in text.lower():
        return "Category: Strategy\nTags: [alignment, goals, planning]"
    elif "stress" in text.lower():
        return "Category: Mindset\nTags: [stress, burnout, resilience]"
    else:
        return "Category: General\nTags: [reflection, feedback, personal growth]"

# 💾 Save data to MySQL
def insert_to_db(name, input_text, category, tags):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aa53123405",  # Replace with your actual password
            database="capstone"     # Make sure this DB exists and has the 'assessment' table
        )
        cursor = conn.cursor()
        query = """
            INSERT INTO assessment (UserName, input_text, category, tags)
            VALUES (%s, %s, %s, %s)
        """
        values = (name, input_text, category, tags)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        st.success("✅ Data saved to the database!")
    except Exception as e:
        st.error(f"❌ Database Error: {e}")

# 🌐 Streamlit UI
st.title("🧠 AssessMate!")
st.title("Data categorize and storage system driven by AI!")

name = st.text_input("Customer Name:")
user_input = st.text_area("Describe your coaching challenge or reflection:")

if st.button("Categorize and Save"):
    if name and user_input:
        st.info("🔍 Analyzing your input...")

        # Generate result using mock AI
        result = categorize_input(user_input)

        # Extract category and tags
        try:
            category_line = result.split("\n")[0].replace("Category:", "").strip()
            tags_line = result.split("\n")[1].replace("Tags:", "").strip()
        except IndexError:
            st.error("⚠️ Unable to parse result. Please check the format.")
        else:
            st.success("✅ Categorized Result:")
            st.write(f"**Category:** {category_line}")
            st.write(f"**Tags:** {tags_line}")

            # Save to MySQL
            insert_to_db(name, user_input, category_line, tags_line)
    else:
        st.warning("⚠️ Please enter your name and reflection before submitting.")


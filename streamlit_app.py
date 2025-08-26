import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("🎓 Student Management System")

menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add a new student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    grade = st.text_input("Grade")
    if st.button("Add"):
        res = requests.post(f"{API_URL}/students", json={"name": name, "age": age, "grade": grade})
        if res.status_code == 201:
            st.success("✅ Student added successfully!")
        else:
            st.error("❌ Error adding student")

elif choice == "View Students":
    st.subheader("All Students")
    res = requests.get(f"{API_URL}/students")
    if res.status_code == 200:
        students = res.json()
        if students:
            for s in students:
                st.write(f"ID: {s['id']} | {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
        else:
            st.info("No students found.")

elif choice == "Update Student":
    st.subheader("Update Student")
    student_id = st.number_input("Enter Student ID", min_value=1)
    new_name = st.text_input("New Name")
    new_age = st.number_input("New Age", min_value=1, max_value=100)
    new_grade = st.text_input("New Grade")
    if st.button("Update"):
        res = requests.put(f"{API_URL}/students/{student_id}", 
                           json={"name": new_name, "age": new_age, "grade": new_grade})
        if res.status_code == 200:
            st.success("✅ Student updated successfully!")
        else:
            st.error("❌ Student not found")

elif choice == "Delete Student":
    st.subheader("Delete Student")
    student_id = st.number_input("Enter Student ID to delete", min_value=1)
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/students/{student_id}")
        if res.status_code == 200:
            st.success("✅ Student deleted successfully!")
        else:
            st.error("❌ Student not found")
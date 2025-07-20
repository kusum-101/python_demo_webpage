import streamlit as st
st.title("Welcome to python")
st.header("Python")
st.subheader("This is a python demo page")
st.code(""" for i in range(1,10):
            print("Hello")
        """)
name = st.text_input("Enter the name: ")
fname= st.text_input("Enter the father name: ")
adr=st.text_area("Enter your address: ")
course=st.selectbox("Enter your course: ",("Btech","Mtech","BCA","MCA"))
button= st.button("Submit")
if button:
    st.markdown(f"""
            Name:{name}
            Father Name:{fname}
            Address: {adr}
            Course: {course}

                """)

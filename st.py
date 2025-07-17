import streamlit as st
from gpt import marketcopy_generator 

st.title("Marketing Copy Generator")

brand = st.text_input("What's your brand name? ")
product_name = st.text_input("What's your product? ")
usp = st.text_area("What is the USP of your product? ")
target = st.text_input("Who is your Target Audience? ")

if st.secrets["OPENROUTER_API_KEY"]:
    api_key = st.secrets["OPENROUTER_API_KEY"]
    # st.write(api_key)
else:
    st.error("No API Key!!!")

if st.button("Generate Market Copy"):
    if product_name and usp and target and brand:
        with st.spinner("Generating marketing Copy"):
            marketcopy = marketcopy_generator(product_name,usp,target,brand,api_key)

            if marketcopy.startswith("Error"):
                st.error(marketcopy)
            else:
                st.success("Here is the generated Market Copy: ")
                st.write(marketcopy)
    else:
        st.warning("Please Fill in all the blanks...")







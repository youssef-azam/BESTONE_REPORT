import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your App", page_icon=":rocket:", layout="wide")

# Define the new Power BI dashboard URL
march_sales_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=9e25f385-722d-48c4-86f0-acccb34fc03a&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"

# HTML code for embedding the new Power BI dashboard
march_sales_html_code = f'<iframe title="مارس" width="1140" height="541.25" src="{march_sales_dashboard_url}" frameborder="0" allowFullScreen="true"></iframe>'

# Use Streamlit to display the new Power BI dashboard using HTML
st.markdown(march_sales_html_code, unsafe_allow_html=True)

# Additional Streamlit app code can be added here

# Run the Streamlit app
if __name__ == "__main__":
    st.write('Hello in my report Powered by Eng: Youssef Azam 👨‍💻, for Manager Eng: Salem 🚀')

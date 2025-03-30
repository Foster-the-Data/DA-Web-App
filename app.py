import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(
    page_title="Excel File Data Analysis",
    layout="wide",  # Set the layout to 'wide'
    initial_sidebar_state="expanded"  # Expand the sidebar initially
)

st.title('Excel File Data Analysis')

st.write("""
This app allows users to upload an Excel file and view data analytics dashboards and visualizations.
""")

# Function to load data
def load_data(file):
    try:
        return pd.read_excel(file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Function to display data preview
def display_data_preview(data):
    st.write("### Data Preview")
    st.dataframe(data.head())
    st.write("### Basic Data Analytics")
    st.write("Descriptive Statistics")
    st.write(data.describe())
    st.write("Column Names")
    st.write(data.columns.tolist())
    st.write("Data Types")
    st.write(data.dtypes)

# Function to display correlation heatmap
def display_correlation_heatmap(data):
    st.write("### Correlation Heatmap")
    corr = data.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Function to display bar chart
def display_bar_chart(data):
    st.write("### Bar Chart Example")
    if st.checkbox("Show Bar Chart"):
        column = st.selectbox("Select column for Bar Chart", data.columns)
        bar_fig, bar_ax = plt.subplots()
        data[column].value_counts().plot(kind='bar', ax=bar_ax)
        st.pyplot(bar_fig)

# Sidebar for file upload
with st.sidebar:
    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    if df is not None:
        display_data_preview(df)
        # Create two columns for dashboards
        dashboard_col1, dashboard_col2 = st.columns(2)
        with dashboard_col1:
            display_correlation_heatmap(df)
        with dashboard_col2:
            display_bar_chart(df)

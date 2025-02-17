# -*- coding: utf-8 -*-
"""Credit card part 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rbkM323cjQaGJCQg19zZKECnLOuVrvyY
"""

# !pip install streamlit

# pip install matplotlib



# pip install --upgrade streamlit

import warnings
warnings.filterwarnings("ignore", message="missing ScriptRunContext")

from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading

# Create a thread object (e.g., a dummy thread)
thread = threading.current_thread()

# Or, if you intend to use a specific thread later:
# thread = threading.Thread(target=your_function)
# thread.start()

# For threads
add_script_run_ctx(thread)

def main():
    import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Set page configuration
st.set_page_config(page_title="Credit Card Fraud Analysis", page_icon="💳", layout="wide")

# Load custom CSS
st.markdown("""
<style>
    .main {background-color: #f5f5f5;}
    .reportview-container .main .block-container {padding-top: 2rem;}
    .st-bw {background-color: #ffffff;}
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("Credit Card Fraud Detection Analysis")
st.markdown("""
### Exploratory Analysis of Credit Card Fraud Dataset
This interactive dashboard helps analyze patterns in credit card fraud transactions.
""")

# File upload
uploaded_file = st.file_uploader("Upload your credit card transactions CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data Overview Section
    st.header("Data Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("First 5 rows")
        st.write(df.head())
    with col2:
        st.subheader("Dataset Shape")
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Basic Stats
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Check for null values
    st.subheader("Missing Values Check")
    st.write(df.isnull().sum().to_frame(name="Missing Values"))

    # Class Distribution Analysis
    st.header("Class Distribution Analysis")

    # Calculate class distribution
    fraud = df[df['Class'] == 1]
    normal = df[df['Class'] == 0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Transactions", len(df))
    with col2:
        st.metric("Normal Transactions", len(normal))
    with col3:
        st.metric("Fraud Transactions", len(fraud))

    # Class distribution plot
    fig, ax = plt.subplots()
    sns.countplot(x='Class', data=df, ax=ax)
    ax.set_title('Class Distribution (0: Normal vs 1: Fraud)')
    st.pyplot(fig)

    # Transaction Visualizations
    st.header("Transaction Patterns")

    # Time and Amount distributions
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    sns.distplot(df['Amount'], ax=ax1, color='r')
    ax1.set_title('Distribution of Transaction Amount')

    sns.distplot(df['Time'], ax=ax2, color='b')
    ax2.set_title('Distribution of Transaction Time')

    st.pyplot(fig)

    # Preprocessing Section
    st.header("Data Preprocessing")

    # StandardScaler for Amount
    scaler = StandardScaler()
    df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1,1))
    df.drop(['Amount'], axis=1, inplace=True)

    # Show scaling results
    st.subheader("Amount Scaling Results")
    st.write(df[['scaled_amount']].describe())

    # Handle class imbalance
    if st.checkbox("Show subsampled data (Class Balance)"):
        # Subsample normal transactions
        normal_sub = normal.sample(len(fraud))
        combined = pd.concat([normal_sub, fraud])

        st.write("Subsampled Dataset Shape:", combined.shape)

        fig, ax = plt.subplots()
        sns.countplot(x='Class', data=combined, ax=ax)
        ax.set_title('Balanced Class Distribution')
        st.pyplot(fig)

else:
    st.warning("Please upload a CSV file to begin analysis")

# Add sidebar with info
st.sidebar.markdown("""
## About
This dashboard analyzes credit card fraud patterns using:
- Data exploration
- Visualizations
- Basic preprocessing

Upload a CSV file with credit card transaction data to begin analysis.
""")

st.sidebar.markdown("""
## Dataset Requirements
Data should contain:
- Time: Transaction timestamp
- V1-V28: PCA transformed features
- Amount: Transaction amount
- Class: 0 for normal, 1 for fraud
""")

if __name__ == "__main__":
    main()

# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split

# # Set page configuration
# st.set_page_config(page_title="Credit Card Fraud Analysis", page_icon="💳", layout="wide")

# # Load custom CSS
# st.markdown("""
# <style>
#     .main {background-color: #f5f5f5;}
#     .reportview-container .main .block-container {padding-top: 2rem;}
#     .st-bw {background-color: #ffffff;}
# </style>
# """, unsafe_allow_html=True)

# # Title and description
# st.title("Credit Card Fraud Detection Analysis")
# st.markdown("""
# ### Exploratory Analysis of Credit Card Fraud Dataset
# This interactive dashboard helps analyze patterns in credit card fraud transactions.
# """)

# # File upload
# uploaded_file = st.file_uploader("Upload your credit card transactions CSV", type="csv")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     # Data Overview Section
#     st.header("Data Overview")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("First 5 rows")
#         st.write(df.head())
#     with col2:
#         st.subheader("Dataset Shape")
#         st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

#     # Basic Stats
#     st.subheader("Basic Statistics")
#     st.write(df.describe())

#     # Check for null values
#     st.subheader("Missing Values Check")
#     st.write(df.isnull().sum().to_frame(name="Missing Values"))

#     # Class Distribution Analysis
#     st.header("Class Distribution Analysis")

#     # Calculate class distribution
#     fraud = df[df['Class'] == 1]
#     normal = df[df['Class'] == 0]

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("Total Transactions", len(df))
#     with col2:
#         st.metric("Normal Transactions", len(normal))
#     with col3:
#         st.metric("Fraud Transactions", len(fraud))

#     # Class distribution plot
#     fig, ax = plt.subplots()
#     sns.countplot(x='Class', data=df, ax=ax)
#     ax.set_title('Class Distribution (0: Normal vs 1: Fraud)')
#     st.pyplot(fig)

#     # Transaction Visualizations
#     st.header("Transaction Patterns")

#     # Time and Amount distributions
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

#     sns.distplot(df['Amount'], ax=ax1, color='r')
#     ax1.set_title('Distribution of Transaction Amount')

#     sns.distplot(df['Time'], ax=ax2, color='b')
#     ax2.set_title('Distribution of Transaction Time')

#     st.pyplot(fig)

#     # Preprocessing Section
#     st.header("Data Preprocessing")

#     # StandardScaler for Amount
#     scaler = StandardScaler()
#     df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1,1))
#     df.drop(['Amount'], axis=1, inplace=True)

#     # Show scaling results
#     st.subheader("Amount Scaling Results")
#     st.write(df[['scaled_amount']].describe())

#     # Handle class imbalance
#     if st.checkbox("Show subsampled data (Class Balance)"):
#         # Subsample normal transactions
#         normal_sub = normal.sample(len(fraud))
#         combined = pd.concat([normal_sub, fraud])

#         st.write("Subsampled Dataset Shape:", combined.shape)

#         fig, ax = plt.subplots()
#         sns.countplot(x='Class', data=combined, ax=ax)
#         ax.set_title('Balanced Class Distribution')
#         st.pyplot(fig)

# else:
#     st.warning("Please upload a CSV file to begin analysis")

# # Add sidebar with info
# st.sidebar.markdown("""
# ## About
# This dashboard analyzes credit card fraud patterns using:
# - Data exploration
# - Visualizations
# - Basic preprocessing

# Upload a CSV file with credit card transaction data to begin analysis.
# """)

# st.sidebar.markdown("""
# ## Dataset Requirements
# Data should contain:
# - Time: Transaction timestamp
# - V1-V28: PCA transformed features
# - Amount: Transaction amount
# - Class: 0 for normal, 1 for fraud
# """)

# # pip install streamlit

# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split


# import warnings
# warnings.filterwarnings("ignore")

# # writefile app.py
# # Set page configuration
# st.set_page_config(page_title="Credit Card Fraud Analysis", page_icon="💳", layout="wide")

# # Load custom CSS
# st.markdown("""
# <style>
#     .main {background-color:rgb(243, 243, 243);}
#     .reportview-container .main .block-container {padding-top: 2rem;}
#     .st-bw {background-color: #ffffff;}
# </style>
# """, unsafe_allow_html=True)

# # Title and description
# st.title("Credit Card Fraud Detection Analysis")
# st.markdown("""
# ### Exploratory Analysis of Credit Card Fraud Dataset
# This interactive dashboard helps analyze patterns in credit card fraud transactions.
# """)

# # File upload
# uploaded_file = st.file_uploader("Upload your credit card transactions CSV", type="csv")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     # Data Overview Section
#     st.header("Data Overview")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("First 5 rows")
#         st.write(df.head())
#     with col2:
#         st.subheader("Dataset Shape")
#         st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

#     # Basic Stats
#     st.subheader("Basic Statistics")
#     st.write(df.describe())

#     # Check for null values
#     st.subheader("Missing Values Check")
#     st.write(df.isnull().sum().to_frame(name="Missing Values"))

#     # Class Distribution Analysis
#     st.header("Class Distribution Analysis")

#     # Calculate class distribution
#     fraud = df[df['Class'] == 1]
#     normal = df[df['Class'] == 0]

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("Total Transactions", len(df))
#     with col2:
#         st.metric("Normal Transactions", len(normal))
#     with col3:
#         st.metric("Fraud Transactions", len(fraud))

#     # Class distribution plot
#     fig, ax = plt.subplots()
#     sns.countplot(x='Class', data=df, ax=ax)
#     ax.set_title('Class Distribution (0: Normal vs 1: Fraud)')
#     st.pyplot(fig)

#     # Transaction Visualizations
#     st.header("Transaction Patterns")

#     # Time and Amount distributions
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

#     sns.distplot(df['Amount'], ax=ax1, color='r')
#     ax1.set_title('Distribution of Transaction Amount')

#     sns.distplot(df['Time'], ax=ax2, color='b')
#     ax2.set_title('Distribution of Transaction Time')

#     st.pyplot(fig)

#     # Preprocessing Section
#     st.header("Data Preprocessing")

#     # StandardScaler for Amount
#     scaler = StandardScaler()
#     df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1,1))
#     df.drop(['Amount'], axis=1, inplace=True)

#     # Show scaling results
#     st.subheader("Amount Scaling Results")
#     st.write(df[['scaled_amount']].describe())

#     # Handle class imbalance
#     if st.checkbox("Show subsampled data (Class Balance)"):
#         # Subsample normal transactions
#         normal_sub = normal.sample(len(fraud))
#         combined = pd.concat([normal_sub, fraud])

#         st.write("Subsampled Dataset Shape:", combined.shape)

#         fig, ax = plt.subplots()
#         sns.countplot(x='Class', data=combined, ax=ax)
#         ax.set_title('Balanced Class Distribution')
#         st.pyplot(fig)

# else:
#     st.warning("Please upload a CSV file to begin analysis")

# # Add sidebar with info
# st.sidebar.markdown("""
# ## About
# This dashboard analyzes credit card fraud patterns using:
# - Data exploration
# - Visualizations
# - Basic preprocessing

# Upload a CSV file with credit card transaction data to begin analysis.
# """)

# st.sidebar.markdown("""
# ## Dataset Requirements
# Data should contain:
# - Time: Transaction timestamp
# - V1-V28: PCA transformed features
# - Amount: Transaction amount
# - Class: 0 for normal, 1 for fraud
# """)

# # from pyngrok import ngrok

# # # Start Streamlit in background
# # import subprocess
# # process = subprocess.Popen(["streamlit", "run", "fraud_dashboard.py"])

# # # Setup ngrok tunnel
# # # public_url = ngrok.connect(addr="8501")
# # # print("Public URL:", public_url.public_url)










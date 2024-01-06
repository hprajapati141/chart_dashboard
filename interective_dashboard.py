import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import yfinance as yf
import mplfinance as mpl
import math
st.write("Hello")
# Create a sample DataFrame
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Streamlit app
st.title('Clickable DataFrame Rows')

# Display the DataFrame as a custom table with HTML
st.markdown("""
    <style>
        .custom-table tr:hover {
            background-color: lightgray;
            cursor: pointer;
        }
        .selected {
            background-color: lightblue !important;
        }
    </style>
""", unsafe_allow_html=True)

# Display the DataFrame as a custom table using HTML
st.markdown("""
    <table class="custom-table">
        <thead>
            <tr>
                <th>Column1</th>
                <th>Column2</th>
            </tr>
        </thead>
        <tbody>
""", unsafe_allow_html=True)

# Populate the table rows
for index, row in df.iterrows():
    st.markdown(f"""
        <tr onclick="highlightRow(this)">
            <td>{row['Column1']}</td>
            <td>{row['Column2']}</td>
        </tr>
    """, unsafe_allow_html=True)

st.markdown("""
        </tbody>
    </table>
""", unsafe_allow_html=True)

# JavaScript function to highlight the clicked row
st.markdown("""
    <script>
        function highlightRow(row) {
            row.classList.toggle('selected');
        }
    </script>
""", unsafe_allow_html=True)


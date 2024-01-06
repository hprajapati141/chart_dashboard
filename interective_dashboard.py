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
st.write("""
    <style>
        .custom-table tr:hover {
            background-color: lightgray;
            cursor: pointer;
        }
        .selected {
            background-color: lightblue !important;
        }
    </style>
""")

# Display the DataFrame as a custom table using HTML
st.write("""
    <table class="custom-table">
        <thead>
            <tr>
                <th>Column1</th>
                <th>Column2</th>
            </tr>
        </thead>
        <tbody>
""")

# Populate the table rows
for index, row in df.iterrows():
    st.write(f"""
        <tr onclick="highlightRow(this)">
            <td>{row['Column1']}</td>
            <td>{row['Column2']}</td>
        </tr>
    """)

st.write("""
        </tbody>
    </table>
""")

# JavaScript function to highlight the clicked row
st.write("""
    <script>
        function highlightRow(row) {
            row.classList.toggle('selected');
        }
    </script>
""")

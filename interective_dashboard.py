import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import yfinance as yf
import mplfinance as mpl
import math
st.write("Hello")
import streamlit as st
import pandas as pd
from streamlit import scripts

# Create a sample DataFrame
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Streamlit app
st.title('Clickable DataFrame Rows')

# Display the DataFrame as a table
table = st.table(df)

# Add a custom JavaScript function to capture row clicks
scripts(scripts="""
    <script>
        const table = document.querySelector('.css-1uvh92h table');

        table.addEventListener('click', function(event) {
            const targetRow = event.target.closest('tr');
            if (targetRow) {
                const rowIndex = Array.from(targetRow.parentNode.children).indexOf(targetRow);
                const selectedRow = document.querySelector(`.css-1uvh92h table tr:nth-child(${rowIndex + 1})`);
                selectedRow.classList.toggle('selected');
            }
        });
    </script>
""")

# Get the selected rows
selected_rows = [row for i, row in enumerate(df.iterrows()) if table.row(i).get_class_list().contains('selected')]

# Display selected rows
if selected_rows:
    st.write("Selected Rows:")
    for index, row in selected_rows:
        st.write(f"Index: {index}, Data: {row}")


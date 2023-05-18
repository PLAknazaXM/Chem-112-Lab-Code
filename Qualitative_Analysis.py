import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

st.set_page_config(page_title="Qualitative Analysis Lab",
                   page_icon=":test_tube:", layout="wide")

st.sidebar.success("Select a page above")

st.title('Qualitative Analysis Labs')

st.subheader('''Select lab being done on the side.''')

st.subheader('''WARNING!

The lab pages on this site do not remember your findings!  This is not to replace your lab notebook, rather to supplement with the interface.''')

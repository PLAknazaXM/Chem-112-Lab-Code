import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

st.set_page_config(page_title="Lab 33",
                   page_icon=":test_tube:", layout="wide")

st.title('Lab 33: The Soluble Group')

Ions_found = 'Ions found: '

st.text('''This lab tests for Ammonium and Sodium Ions.''')

st.subheader('''Ammonium Test:

Warning!  When completing a stiff test, heated chemicals can splatter out!''')

st.text('''1: Moisten a strip of red litmus paper with distilled water, place on bottom of watch glass.
2: Place 3mL of test solution in evaporation dish, add 1-2 mL of 6M NaOH.
3: Quickly cover dish with watch glass, gently warm with hand or warm water bath.
   Check for a blue spot on the litmus paper.
   
Result: If a blue spot on litmus paper forms or the smell of ammonia is present, ammonium was in the compound.''')

Ammonium = st.text_input('Did the red litmus paper turn blue or was there an ammonia smell present? [y/n]')

st.subheader('''Sodium Test:

Notice: Test is very sensitive, let nothing come into contact with wire after cleaning!''')

st.text('''
1: Use 6M HCl to clean a nickel-chromium alloy wire until no color is present in a flame test.
2: Dip clean wire into test solution, hold to outer region of flame.

Result: If a luminous, fluffy, yellow-orage flame is persistent for around 30 seconds, sodium ions are present.''')

Sodium = st.text_input('Was there a persistent yellow-orange flame? [y/n]')

if (Ammonium == 'y' or Ammonium == 'Y' or Ammonium == 'yes' or Ammonium == 'Yes'):
    Ions_found = Ions_found + '''
    - Ammonium'''
if (Sodium == 'y' or Sodium == 'Y' or Sodium == 'yes' or Sodium == 'Yes'):
    Ions_found = Ions_found + '''
    - Sodium'''

st.text(Ions_found)

import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

st.set_page_config(page_title="Lab 34",
                   page_icon=":test_tube:", layout="wide")

st.title('Lab 34: The Chloride Group')

st.text('''This lab tests for Lead, Mercury, and Silver Ions.''')

Ions_found = 'Ions found: '

st.subheader('Preparation:')

st.text('''-Add 3 drops of 6M HCl to 3mL of test solution, mixing thoroughly with glass stirring rod.
-A precipitate will form is any of the ions above are present.
-Centifuge the mixture, and pour solution (S1) into another test tube, check for any more precipitate (P1).
-S1 may be discarded if this lab is the end of your experiment.
-Add 1-3mL of distilled water, centrifuge, then discard wash liquid.

Proceed to Lead test.''')

st.subheader('Lead Ion Test')

st.text('''
1: Add 3-4mL of distilled water to P1 and heat mixture to near boiling, stir.
2: Centrifuge and separate solution (S2) from the precipitate (P2).
Note: If there is no precipitate, there will be no mercury or silvar ions!
3: Wash P2 using the same procedures listed in preparation through 10mL of water.
4: In S2, add several drops of 1M K2CrO4.  Observe for a yellow precip.''')

Lead = st.text_input('Was there a yellow precipitate? [y/n]')

st.subheader('Mercury Ion Test')

st.text('''
1: To P2, and 1mL of 6M NH3 and 2mL of water while stirring. If present, any AgCl should dissolve.
2: Centrifuge and remove solution (S3) fromprecipitate (P3).  S3 should be completely clear.
   If S3 is not completely clear, re-centifuge S3 until clear.
   Observe for a gray to black residue.''')

Mercury = st.text_input('Was there a gray to black solid residue in the precipitate? [y/n]')

st.subheader('Silver Ion Test')

st.text('''
1: Acidify S3 with 6M HCl drop-wise while stirring.  Continue until blue litmus turns  red.
   Observe for a white precipitate.''')

Silver = st.text_input('Was there a white precipitate? [y/n]')

if (Lead == 'y' or Lead == 'Y' or Lead == 'yes' or Lead == 'Yes'):
    Ions_found = Ions_found + '''
    - Lead'''
if (Mercury == 'y' or Mercury == 'Y' or Mercury == 'yes' or Mercury == 'Yes'):
    Ions_found = Ions_found + '''
    - Mercury'''
if (Silver == 'y' or Silver == 'Y' or Silver == 'yes' or Silver == 'Yes'):
    Ions_found = Ions_found + '''
    - Silver'''


st.text(Ions_found)

import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

st.set_page_config(page_title="Lab 35",
                   page_icon=":test_tube:", layout="wide")

st.title('Lab 35: The Hydrogen Sulfide Group')

st.text('''This lab tests for Lead, Copper, Bismuth, Mercury, and Tin Ions.''')

Ions_found = 'Ions found: '

st.subheader('Preparation:')

st.text('''-Neutralize S1 from Lab 34 with 6M NH3 until red litmus paper turns blue.
-Add 6M HCl by drop until solution is acidic and any precipitates from NH3 dissolve.''')

st.subheader('Subgroup Separation:')

st.text('''
1: Add 10-12 drops of 1M thioacetamide, and heat for 10 minutes in a hot water bath.
2: Centrifuge and decant solution (S3A) form precipitate (P3).
3: Add a few drops of 1M thioacetamide to verify completeness of precipitation.
4: If not checking for group IV or V ions, discard S3A.
5: Wash with 4mL of distilled water and 4mL of 6M HCl. Decant.
6: Add 5 drops of 6M NaOH nd 1mL of water.  Stir well and warm in hot water bath for 2-3 minutes.
7: Cool, add 5 drops of 3% H2O2.  Stir again and heat for 5 minutes until effervescence ceases.
Note: Any dark colored precipitates can be Cu, Pb, Bi, or Hg Ion indicators.
8: Add 5 drops of 1M thioacetamide and 6M NaOH.  Stir, warm for 2-3 minutes, centrifuge.
Note: Solution (S4) will be used to test for the tin subgroup.
9: Wash precipitate (P4) with 3mL water, and a drop of 1M thioacetamide and 6M NaOH.

Proceed to Copper Subgroup''')

st.subheader('Copper Subgroup')

st.text('''
1: To P4, and 1mL water and 1mL 6M NHO3, warm and stir for several minutes.
2: Centrifuge and decant to small beaker (precipitate unwanted).
WARNING: DO NEXT STEP UNDER FUME HOOD!
3: Add 2mL  3M H2SO4, evaporate to near dryness until choking white fumes evolve.
4: Still in fume hood, cool beaker, transfer to small test tube, centrifuge.

S5 will be tested for copper and bismuth ions.
P5 will be tested for lead ions.''')

st.subheader('Lead Ion Test')

st.text('''
1: Add 1mL 3M NH4C2H3O2 to P5, stir and warm if needed..
2: Add 1mL of 1M K2CrO4, centrifuge.  Observe for a yellow precip.''')

Lead = st.text_input('Was there a yellow precipitate? [y/n]')

st.subheader('Copper Ion Test')

st.text('''
1: To S5, add 6M NH3 to make solution basic.  Darker blue-violet color shows copper.
2: If a precipiate is seen, centrifuge and decant for precipitate (P6).
Note: If no precipitate forms, there will be no bismuth.
''')

Copper = st.text_input('Did S5 turn a darker blue-violet? [y/n]')

st.subheader('Bismuth Ion Test')

st.text('''
1: Add one drop of 6M NaOH and .1M SnCl2 to P6, stir well, centrifuge.
Note: Look for a gray-black residue''')

Bismuth = st.text_input('Was there a gray-black residue found in P6? [y/n]')

st.subheader('''Tin Subgroup:

WARNING: WORK UNDER A FUME HOOD!''')

st.text('''
1: Add 3M H2SO4 to S4 by drop until solution turns blue litmus to red.
   Stir well after each drop, note the volume of acid used.
2: Add  an excess of 3M H2SO4 equal to 33% of the acid needed for neutralization.
3: Centrifuge and decant.  S7 can be discarded.
Note: If P7 is dark or colored, a tin subgroup ion is present.  If white, can skip
      the tin subgroup.  White or very pale yellow is likely sulfur ions S2-
4: Wash P7 with water, stir well, centrifuge, then decant wash liquid.  Then add 1mL water,
   10 drops 6M NaOH, 6 drops of 30% H2O2.  Heat to decompose excess H2O2.
5: Centrifuge mixure and decant.  S8 will be tested for tin, P8 for Mercury.''')

st.subheader('Mercury Ion Test')

st.text('''
1: Wash P8 with water, centrifuge, decant.
2: Dissolve P8 with 5 drops 6M HCl and 6M NaOH, heat to boil for 1 minute.
3: Once dissolved, add 1mL of water, then  2-3 drops .1M SnCl2.
Note: Look for silky white precipitate turning dark''')

Mercury = st.text_input('Was there a silky white precipitate that turned dark? [y/n]')

st.subheader('Tin Ion Test')

st.text('''
1: Add 6M HCl to S8 by drop until blue litmus turns red, then one extra drop.
2: Evaporate to 3 drops volume, then add .5 inch iron brad or 1cm iron wire.
3: Let stand several minutes to reduce, then add 1-2 mL water.
4: On a spot plate or small test tube, mix several drops of reduced test solution and
   about 1mL diazine green reagent.  A blue to violet or blue to violet test indicated tin.''')

Tin = st.text_input('Did the diazine green reagent turn violet or red? [y/n]')

if (Lead == 'y' or Lead == 'Y' or Lead == 'yes' or Lead == 'Yes'):
    Ions_found = Ions_found + '''
    - Lead'''
if (Copper == 'y' or Copper == 'Y' or Copper == 'yes' or Copper == 'Yes'):
    Ions_found = Ions_found + '''
    - Copper'''
if (Bismuth == 'y' or Bismuth == 'Y' or Bismuth == 'yes' or Bismuth == 'Yes'):
    Ions_found = Ions_found + '''
    - Bismuth'''
if (Mercury == 'y' or Mercury == 'Y' or Mercury == 'yes' or Mercury == 'Yes'):
    Ions_found = Ions_found + '''
    - Mercury'''
if (Tin == 'y' or Tin == 'Y' or Tin == 'yes' or Tin == 'Yes'):
    Ions_found = Ions_found + '''
    - Tin'''

st.text(Ions_found)
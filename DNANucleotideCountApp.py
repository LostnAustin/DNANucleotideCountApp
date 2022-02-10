import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

##
# import and set image, create banner
image = Image.open('dna-logo.jpeg')
st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")


###
# create input box
###
st.header('Enter DNA sequence')


sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=25
)
sequence = sequence.splitlines()
sequence = sequence[1:] #begin at second line in order to skip the sequence name
sequence = ''.join(sequence)

st.write("""
***
""")

## Print the entered DNA sequence
st.header('INPUT (DNA Query)')
sequence

## Nucelotide count response
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])

    return d
x = DNA_nucleotide_count(sequence)

x_label = list(x)
x_values = list(x.values())

x

### 2. Print Text Result
st.subheader('2. Print text')
st.write('There are ' + str(x['A']) + ' adenine (A)')
st.write('There are ' + str(x['T']) + ' Thymine (T)')
st.write('There are ' + str(x['G']) + ' Guanine (G)')
st.write('There are ' + str(x['C']) + ' Cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'Nucleotide'})
st.write(df)

### 4. Display Bar chart with Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='count'
)
#controls width of the bar. Increasing the size in this case.
p = p.properties(
width=alt.Step(80)   
)
st.write(p)
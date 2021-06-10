import streamlit as st
import ipywidgets as widgets
from IPython.display import display
import urllib.request
import numpy as np
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Check whether a Matrix is nilpotent or not")
st.write("This is part of ACS(EE-3002) Course")

introduction_str = 'This is a pet breed classifier.  It was made with 7349 images corresponding to 37 breeds, \
taken from The Oxford-IIIT Pet Dataset. It was done by transfer of learning using the resnet34 model from Pytorch and the Fastai libraries. \
    In the validation of the model, the training error was 5%. '

st.markdown(introduction_str)
st.markdown("If the interface hasn't loaded below it's because it's still loading the model across from GitHub, it can take a few seconds.")
'''
m=[]
n=st.number_input('Shape of matrix')
for i in range(int(n)):
    print(f'enter n values of row{i+1}')
    l=[]
    for j in range(n):
        a=st.number_input('Enter int value')
        l.append(a)
    m.append(l)

st.write(pd.DataFrame(m))'''

def check_nilpotent(m):
    O=np.zeros((n,n), dtype=int)
    m=np.array(m)
    R=np.array(m)
    k=1
    print(f'M :')
    print(pd.DataFrame(R))
    if np.array_equal(R,O):
        return m, 'Nilpotent matrix with index: 1'
    else:
        while k<n:
            R= np.dot(R,m)
            print(f'M^{k+1} : ')
            print(pd.DataFrame(R))
            if np.array_equal(R,O):
                return m, f'Nilpotent matrix with index:{k+1}'
                #break
            k+=1
        if k==n:
            return m, 'Not a Nilpotent matrix'
def main():
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;"> Check Nilpotent </h2>
    </div>
    """
    

    st.markdown(html_temp,unsafe_allow_html=True)
    #st.write(m)
    m=[]
    n=st.number_input('Shape of matrix')
    for i in range(int(n)):
        print(f'enter n values of row{i+1}')
        l=[]
        for j in range(n):
            a=st.number_input('Enter int value')
            l.append(a)
        m.append(l)

    st.write(pd.DataFrame(m))
        
        #img_pil = PIL.Image.open(img_bytes)
        #img = pil2fast(img_pil)
        #img = open_image(BytesIO(img_bytes))
        
    if st.button("Check "):
        #st.write("Classifying...")
        with st.spinner('Checking...'):
            m,pred = check_nilpotent(m)
        #out_label = f'Prediction: {pred_class};\n\n Probability: {outputs[pred_idx]:.03f}'
        st.success(pred)
        #st.success('The output is {}'.format(result))
if __name__=='__main__':
    main() 

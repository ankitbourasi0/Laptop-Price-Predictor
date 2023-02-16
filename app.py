import streamlit as st
import numpy as np
import pickle 


pipe = pickle.load(open('pipe.pkl','rb'))
laptop = pickle.load(open('laptop.pkl','rb'))


st.title("Laptop price predictor")
company = st.selectbox('Brand',laptop['Company'].unique())
laptop_type = st.selectbox("Type",laptop["TypeName"].unique())
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])
weight = st.number_input("Weight of the laptop")
touchscreen = st.selectbox("Touchscreen",["No","Yes"])
ips= st.selectbox("IPS display",["No","Yes"])
screensize = st.number_input("Screen size")
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU',laptop['Cpu Brand'].unique())
hdd = st.selectbox("Hard disk drive(HDD) in GB",[0,128,256,512,1024,2048])
ssd = st.selectbox("Solid state drive(SSD) in GB",[0,8,128,256,512,1024])
gpu = st.selectbox("GPU",laptop["Gpu Brand"].unique())
os = st.selectbox("Operating System",laptop["OpSys"].unique())
ok = st.button("Predict Price")
if ok:
    ppi = None
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == "Yes":
        ips = 1
    else:
        ips = 0
    if screensize != 0:
        X = int(resolution.split('x')[0])
        Y = int(resolution.split('x')[1])
        ppi = ((X**2) + (Y**2))**0.5/screensize
        res = np.array([company,laptop_type,ram,os,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu])
        res = res.reshape(1,12)
        st.title("The predicted price of this configurations is: ₹" +str(int(np.exp(pipe.predict(res)[0]))))
        
    else:
        st.error("Screen size must be given")

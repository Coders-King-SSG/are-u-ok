import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg
import time
import datetime as dt
st.set_page_config(page_title="Are You Ok?",
    page_icon="🩺",
    layout = "centered")

st.set_option('deprecation.showPyplotGlobalUse', False)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    st.write('Timed out!!')
st.header('Health Monitor 🩺')
name = st.text_input("Enter name:")
age = st.number_input("Enter age:")
sex = st.selectbox('Enter Gender',
    ('Male', 'Female'))
if sex == 'Male':
    bfpsex = 16.2
else:
    bfpsex = 5.4

we = st.number_input('Enter your weight (in kg)')
hg = st.number_input('Enter your height (in inch)')
hg*=0.0254

wl = st.number_input('Enter your waist measurement (in inch)')
hl = st.number_input('Enter your hip measurement (in inch)')
wl*=2.54
hl*=2.54
whr = hl/wl
st.text("Count your pulse rate (number of heart beat) by placing the first two fingers of your right hand on the inside of your left wrist just below your thumb.")
if st.button("Start Timer"):
    countdown(10)
pr = st.number_input('Enter your pulse rate', step = 1)
pr*=6
st.text("Sit on the floor with your back straight, legs together, and arms out in front of you at shoulder level. Mark on the floor (beside your legs) the point directly below your fingertips, then slowly reach forward, keeping your legs straight. Mark where your fingertips reach, then measure the distance between the two marks (in centimetres).")
sit = st.number_input("Enter here (in cm.)")
pp = st.number_input("Do as many modified pushups (on your knees) as you can without stopping, as shown below, keeping your body in a straight line and lowering your chest within four inches of the floor.", step = 1)
img = mpimg.imread('pushup.png')
imgplot = plt.imshow(img)
imgplot.axes.get_xaxis().set_visible(False)
imgplot.axes.get_yaxis().set_visible(False)
st.pyplot()
nofmeals = st.number_input('I typically eat____times a day (including snacks):', step = 1, min_value = 1, max_value = 20)
ff = st.number_input('''I eat high-fat or fried snacks____:
1 for Regularly (7 or more times a week)
2 for Sometimes (4-6 times a week)
3 for Rarely (0-3 times a week)
4 for Never''', step = 1, min_value = 1, max_value = 4)

vg = st.number_input('''I eat meals or snacks that include fruits or vegetables____:
1 for Regularly (10 or more times a week)
2 for Sometimes (6-9 times a week)
3 for Rarely (1-5 times a week)
4 for Never''', step = 1, min_value = 1, max_value = 4)

fattyfood = st.number_input('''I____avoid processed foods that contain trans fat, saturated fat, and large amounts of sodium, nitrates, food chemicals and sugar:
1 for Regularly (I purposely avoid buying or eating foods that contain these things)
2 for Sometimes (I try to buy and eat the right thing, but sometimes I slip)
3 for Rarely (it doesn’t alter my buying or eating habits)
4 for Never''', step = 1, min_value = 1, max_value = 4)

exercise = st.number_input('''I____exercise:
1 for Regularly (5 or more times a week)
2 for Sometimes (3-4 times)
3 for Rarely (1-2 times)
4 for Never''', step = 1, min_value = 1, max_value = 4)
hypt = st.number_input("Do you suffer from hypertension, anxiety etc.?\n1 for Yes\n0 for No", step = 1, min_value = 0, max_value = 1)
dis = st.number_input("Do you have a family history og diabetes type 2, High blood pressure, heart attack, stroke etc.?\n1 for Yes\n0 for No", step = 1, min_value = 0, max_value = 1)
smdr = st.number_input("Do you smoke or drink?\n1 for Yes\n0 for No", step = 1, min_value = 0, max_value = 1)
if st.button("Intepret my Health!!"):
    bmi = we/(hg*hg)
    st.subheader("Your BMI = "+str(round(bmi,2)))
    img = mpimg.imread('bmi.jpg')
    imgplot = plt.imshow(img)
    st.pyplot()
    st.caption(str(round(whr*10,2))+"% visceral mass")
    bfp = (1.20 *bmi) + (0.23 * age) - bfpsex
    st.caption(str(round(bfp,2))+"% body fat")
    bodyage = age

    if whr < 0.816:
        bodyage+=4

    if (pr >=54)&(pr<=59):
        bodyage+=4
    elif (pr >=60)&(pr<=64):
        bodyage+=2
    elif (pr >=65)&(pr<=72):
        bodyage-=1
    elif (pr >=73):
        bodyage-=2

    if (sit >=0)&(sit<=25):
        bodyage+=3
    elif (sit >=26)&(sit<=37):
        bodyage+=2
    elif (sit >=38)&(sit<=40):
        bodyage-=2
    elif (sit >=41):
        bodyage-=3

    po = 0
    if nofmeals <=2:
        po+=1
    elif nofmeals ==3:
        po+=2
    elif nofmeals ==4:
        po+=3
    elif nofmeals ==5:
        po+=4
    if ff ==1:
        po+=1
    elif ff ==2:
        po+=2
    elif ff ==3:
        po+=3
    elif ff ==4:
        po+=4
    if vg ==1:
        po+=4
    elif vg ==2:
        po+=3
    elif vg ==3:
        po+=2
    elif vg ==4:
        po+=1
    if fattyfood ==1:
        po+=4
    elif fattyfood ==2:
        po+=3
    elif fattyfood ==3:
        po+=2
    elif fattyfood ==4:
        po+=1
    #123
    if (po >=0)&(po<=9):
        bodyage+=3
    elif (po >=10)&(po<=12):
        bodyage+=2
    elif (po >=13)&(po<=15):
        bodyage-=2
    elif (po >=16):
        bodyage-=3
    #Pushup
    if (pp >=0)&(pp<=30):
        bodyage+=2
    elif (pp >=31)&(pp<=60):
        bodyage+=1
    elif (pp >=61)&(pp<=90):
        bodyage-=1
    elif (pp >=91):
        bodyage-=2

    if exercise ==1:
        bodyage-=4
    elif exercise ==2:
        bodyage-=3
    elif exercise ==3:
        bodyage-=1
    elif exercise ==4:
        bodyage+=2

    if hypt == 1:
        bodyage+=4
    else:
        bodyage-=2

    if dis == 1:
        bodyage+=2
    else:
        bodyage-=1
    if smdr == 1:
        bodyage+=4
    else:
        bodyage-=1

    st.subheader("Your actual age is "+str(age)+" years and you body age is "+str(bodyage)+" years.")
    
    dataobj = {
    'Name':name,
    'Age':age,
    'Test taken on':dt.datetime.now(),
    'BMI':round(bmi,2),
    'BodyAge':bodyage,
    'Visceral Mass':str(round(whr*10, 2))+"%",
    'Body Fat Percentage':bfp
    }
    df = pd.DataFrame(dataobj, index=[0])
    def convert_df(data):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)

    st.download_button(
        label="Download health data as CSV",
        data=csv,
        file_name=f'{name} Health Info.csv',
        mime='text/csv',
    )
    st.subheader("Thank you!")
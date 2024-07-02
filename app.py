import streamlit as st 
import pandas as pd
import numpy as np
import pickle
import time

image_path=".\logos\download.png"
teams=pickle.load(open('clubs.pkl','rb'))
model=pickle.load(open('model1.pkl','rb'))
ranking=pickle.load(open('rankings.pkl','rb'))
ranking_df=pd.DataFrame(ranking)
cols=pickle.load(open('columns.pkl','rb'))

col1, col2 = st.columns([2, 2])

with col2:
    st.title("Premier League Match Prediction")


with col1:
    
    st.image(image_path, use_column_width='auto') 


col3,col4,col5 = st.columns(3)
with col3:
    team_1 = st.selectbox(
        'Select home team',
        teams,
        index=None,
        placeholder="Select home team..",
    )
with col4:
    kick_off = st.selectbox(
        'Kick-off timing',
        ("Early", "Middle", "Late")
    )
with col5:
    team_2 = st.selectbox(
        'Select away team',
        teams,
        index=None,
        placeholder="Select away team..",
    )


def predict_match(team1,team2,venue,kickoff):
    idx=0
    if(kickoff in cols):   
        idx = np.where(cols==kickoff)[0][0]
    rank1=ranking_df[ranking_df["Team"]==team1].Rank
    rank2=ranking_df[ranking_df["Team"]==team2].Rank
    x=np.zeros(len(cols))
    x[0]=venue
    x[1]=rank1.values[0]
    x[2]=rank2.values[0]
    if idx>0:
        x[idx]=1
    xg1=model.predict([x])[0]

    x2=np.zeros(len(cols))
    if(venue==0):
        x2[0]=1
    else:
        x2[0]=0
    x2[1]=rank2.values[0]
    x2[2]=rank1.values[0]
    if idx>0:
        x2[idx]=1
    xg2=model.predict([x2])[0]
    if(abs(xg1-xg2) <0.1):
        winner="Draw"
    else:
        if(xg1>xg2):
            winner=(f"{team1} wins!")
        else:
            winner=(f"{team2} wins!")
    return xg1,xg2,winner        
    
    
   
        
if team_1 is not None:
    team1_img= "logos\\" + team_1 + ".png"

if team_2 is not None:
    team2_img= "logos\\" + team_2 +".png"

if(team_1 is not None and team_2 is not None and team_2!=team_1):    
    col6,col7,col8 = st.columns([1,3,1])   
    with col6:
        st.image(team1_img)
    with col8:
        st.image(team2_img)
        
    if st.button("Predict"):
        xg1,xg2,winner=predict_match(team_1,team_2,1,kick_off)
        xg1=round(xg1,2)
        xg2=round(xg2,2)
        # st.title("Expected xG")
        st.markdown("<h1 style='text-align: center;'>Expected xG</h1>", unsafe_allow_html=True)
        col9,col10,col11=st.columns([1,10,1])
        with col9:
            st.write(xg1)    
        with col11:
            st.write(xg2)        
        # st.write(xg1," **Expected xG**  ",xg2) 
        # st.title(winner)
        winner_text=f"<h3 style='text-align: center; background-color: white; color: black'>{winner}</h3>"
        st.markdown(winner_text, unsafe_allow_html=True)          
elif(team_2==team_1):
    st.info("Pick a different away team! ")

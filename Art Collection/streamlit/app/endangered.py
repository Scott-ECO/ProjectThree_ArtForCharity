################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################
# Endangered Animals Information

# Database of Endangered Animals including their name, open sea address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
animals_database = {
    "Javan rhino": ["Javan Rhino", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/0/", "> 1000", "Natural catastrophes, habitat loss, diseases, poaching, and potential inbreeding", "https://campaign.awf.org/support-african-elephants/?utm_source=semgpbrbr&utm_medium=cpc&utm_campaign=sem&gclid=Cj0KCQjwuuKXBhCRARIsAC-gM0ivmnnvs3ll6gNVFog4z4LyGq5xA9hBDt1Zv0r7jZ_n-Ba4cCYwinsaAvhEEALw_wcB", "../images/rhino.jpg", "../graphs/JavanRhino.png"],
    "Mountain gorilla": ["Mountain Gorilla", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/1", "> 1000", "Habitat loss, disease, charcoal making, war", "https://support.worldwildlife.org/site/Donation2?df_id=14650&14650.donation=form1&s_src=AWE2010OQ18507A04091RX&gclid=Cj0KCQjwuuKXBhCRARIsAC-gM0gRsaKEIVJcLVtU0qppI9s1dmfg3yrxFT4sbA9SXg7d0ZW9_YwBzdoaAmnaEALw_wcB", "../images/gorilla.jpg", "../graphs/MountainGorilla.png"],
    "Tiger": ["Tiger", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/2", "> 5000", "Over 95 percent of their habitat has been lost to clearing of forests and building of road networks.", "https://support.worldwildlife.org/site/Donation2?df_id=14650&14650.donation=form1&s_src=AWE2010OQ18507A04091RX&gclid=Cj0KCQjwuuKXBhCRARIsAC-gM0gRsaKEIVJcLVtU0qppI9s1dmfg3yrxFT4sbA9SXg7d0ZW9_YwBzdoaAmnaEALw_wcB", "../images/tiger.jpg", "../graphs/Tiger.png"],
    "Polar bear": ["Polar Bear", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/3/", "20,000-30,000", "Climate warming, polution, disease, overharvesting, sea ice loss", "https://polarbearsinternational.org/", "../images/polarbear.jpg", "../graphs/PolarBear.png"],
    "Plains bison": ["Plains Bison", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/4/", "30,000-40,000", "Habitat loss, hunting, genetic modification to to domestication", "https://support.worldwildlife.org/site/Donation2?df_id=14650&14650.donation=form1&s_src=AWE2010OQ18507A04091RX&gclid=Cj0KCQjwuuKXBhCRARIsAC-gM0gRsaKEIVJcLVtU0qppI9s1dmfg3yrxFT4sbA9SXg7d0ZW9_YwBzdoaAmnaEALw_wcB", "../images/plains bison.jpg", "../graphs/PlainsBison.png"],
    "African forest elephant": ["African Forest Elephant", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/5/", "30,000-40,000", "Habitat loss, fragmentation, deforestation, poaching", "https://elephantconservation.org/", "../images/elephant.jpg", "../graphs/AfricanElephant.png"],
    "Monarch butterfly": ["Monarch Butterfly", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/6/", "250,000-275,000", "Habitat loss, Climate change, Increased herbicide use", "https://support.worldwildlife.org/site/Donation2?df_id=14650&14650.donation=form1&s_src=AWE2010OQ18507A04091RX&gclid=Cj0KCQjwuuKXBhCRARIsAC-gM0gRsaKEIVJcLVtU0qppI9s1dmfg3yrxFT4sbA9SXg7d0ZW9_YwBzdoaAmnaEALw_wcB", "../images/butterfly.jpg", "../graphs/MonarchButterfly.png"],
    "Sea turtle": ["Sea Turtle", "https://testnets.opensea.io/assets/rinkeby/0xbe53f18f7288216c7ae03753b188626ceca5e50c/7/", "6,500,000-6,600,000", "Poaching, habitat destruction and accidential capture in fishing gear, and pollution.", "https://support.worldwildlife.org/site/Donation2?df_id=14650&14650.donation=form1&s_src=AWE2010OQ18507A04091RX&gclid=Cj0KCQjwuuKXBhCRARIsAC-gM0gRsaKEIVJcLVtU0qppI9s1dmfg3yrxFT4sbA9SXg7d0ZW9_YwBzdoaAmnaEALw_wcB", "../images/seaturtle.jpg", "../graphs/SeaTurtleNests.png"]
}

# A list of the FinTech Finder candidates first names
animals = ["Javan rhino", "Mountain gorilla", "Tiger", "Polar bear", "Plains bison", "African forest elephant", "Monarch butterfly", "Sea turtle"]

st.sidebar.markdown("## Quick Purchase Navigation")
animal = st.sidebar.selectbox('Select an Animal', animals)
user_choice = animals_database[animal][1]
st.sidebar.write(user_choice)

def get_people():
    db_list = list(animals_database.values())

    for number in range(len(animals)):
        st.write("Name: ", db_list[number][0])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("")
        with col2:
            st.image(db_list[number][5], width=200)
        with col3:
            st.write("")
        st.write("2022 Population: ", db_list[number][2])
        col4, col5, col6 = st.columns(3)
        with col4:
            st.write("")
        with col5:
            st.image(db_list[number][6], width=200)
        with col6:
            st.write("")
        st.write("Cause of Status: ", db_list[number][3])
        st.write("Leading Organizations: ", db_list[number][4])
        st.text(" \n")
        st.text(" \n")
        st.text(" \n")
        st.text(" \n")
        st.text(" \n")

        


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("<h1 style='text-align: center; color: white;'>Endangered NFTs</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>A charity NFT project </h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Scott Phillips, a renowned artist from Colorado has created a new collection in order to save endangered animals. Endangered NFTs is an exclusive collection that features endangered animals. This one time auction will have the profits sent directly to the World Wildlife Fund as donation.</h3>", unsafe_allow_html=True)
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
################################################################################
# Streamlit Sidebar Code - Start


get_people()
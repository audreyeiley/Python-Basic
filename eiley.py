# to run,copy, and paste the code below
# streamlit run eiley.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link
# https://docs.streamlit.io/

import streamlit as st
    
title = "Catching trash"

st.title(title)


description = """
This game is about catching pollution/trash from the ocean. 
Its like a fishing game, you need to put your rod in the water and in the water there will be  moving fish and trash,
what you need to do is with the fishing rod grab the trash, the levels get harder as you play (It gets faster) 
If you catch the fish then it will be game over, and as you grab the trash you will get better fishing rods
"""
st.write(description)


st.image("1.png")
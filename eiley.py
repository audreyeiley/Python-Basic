# to run,copy, and paste the code below
# streamlit run eiley.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link
# https://docs.streamlit.io/

import streamlit as st

                                
st.title(" How the world was saved from the  :blue[Evil coding teacher] :sunglasses:")

story = """
Chapter 1: The Disappearance of Elena

It was an ordinary morning in Codeville when the unthinkable happened: Elena, a talented coder known for her clever solutions and quick thinking, vanished. For days, there was no sign of her. Her friends—Eiley, Eugenia, Tara, Yuna, and Alice—searched high and low, but their friend had disappeared without a trace.

Then, one evening, a mysterious message appeared on all their screens, written in cryptic code:

"If you wish to see Elena again, you must solve my riddles, defeat my traps, and prove you are worthy of her freedom. Welcome to my domain... The Lair of Eternal Code."

The message was from none other than the evil Professor Debug, the notorious coding teacher who had tormented students for years with his cruel challenges and sinister algorithms. Elena had been caught in his clutches, and now it was up to the Code Avengers to rescue her.

...

(The rest of the story continues in the same format)
"""

st.write(story)

name = st.text_input("Enter your name")
st.write(name)
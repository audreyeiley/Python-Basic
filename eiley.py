# to run,copy, and paste the code below
# streamlit run eiley.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link
# https://docs.streamlit.io/

import streamlit as st
    
title = "How the world was saved from the evil coding teacher"
st.title(title)


story = """
In the heart of Code Academy, where the greatest young programmers trained, 
five students—Eiley, Eugenia, Tara, Yuna, and Alice—faced their greatest challenge yet. 
Elena, one of the best coders, had been kidnapped by the feared Professor Debug!

The academy’s systems were compromised, strange glitches appearing everywhere. 
Time was running out. If they didn’t act fast, Elena might be lost forever inside Debug’s corrupted code.

Professor Debug smirked as he locked Elena in his Digital Dungeon.
 "Your code is impressive, Elena, but not as powerful as my corrupted algorithms!" he sneered.

Elena remained calm, scanning the digital prison’s code structure. 
There had to be a loophole... "I won’t let you win, Debug. My friends will come for me."

Determined to save their friend, the five students gathered in their secret lab.
 Eiley studied the logic gates, Eugenia analyzed the encryption, Tara worked on hacking the firewall, 
 Yuna built a distraction program, and Alice scanned the data streams.

"If we combine our skills, we can outcode him!" Eiley declared.

Tara pulled up a map of Debug’s lair, coded entirely in complex algorithms and digital traps.
 "This isn’t just a simple hack. We’ll need to outsmart his defenses step by step."

The team sneaked into Debug’s lair, facing a maze of deadly code traps. Red warning messages flashed: "ACCESS DENIED!"

Tara quickly rewrote the web scripts to bypass security.
 Eugenia cracked a complex encryption lock while Alice decoded a shifting firewall. 
 Yuna’s distraction program sent thousands of fake data packets, confusing Debug’s security AI.

"We’re in!" Tara whispered triumphantly.

As they reached Elena’s chamber, Professor Debug appeared, laughing maniacally. 
"You think you can defeat me? My code is unbreakable!" he roared.

A battle of coding skills erupted! Segfaults! Infinite loops! Stack overflows!

Debug unleashed a powerful AI virus, trying to delete the team’s programs.
 Eiley countered with a recursive function, trapping the virus in an endless loop!
   Alice deployed a self-learning algorithm to counteract Debug’s firewall! Tara wrote a script to slow Debug’s processing power, 
   buying them time. Yuna injected a beautiful yet chaotic code, breaking Debug’s structured algorithms.

Elena, now free, joined the fight. "Professor, you forgot one thing..." she said, smirking. "Teamwork always wins."

With a final powerful function, the team deleted Debug’s control over the system! The lair’s corrupted code began collapsing,
 lines of red text crumbling into nothingness.

Professor Debug’s code collapsed. His lair flickered and glitched into nothingness! 
The six friends cheered as they walked back to Code Academy, victorious.

Elena smiled. "I couldn’t have done it without you all."

And from that day on, no code was too tough for the greatest team of young coders. 
The academy restored its systems, and a new legend was written in the world of programming.

Or so they thought...

Deep inside the digital void, where Debug’s code once ruled...

A single corrupted line of code flickered back to life.

"SYSTEM REBOOTING..."

To be continued...

"""

st.write(story)

name = st.text_input("Continue the story")
st.write(name)
# to run,copy, and paste the code below
# streamlit run eiley.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link
# https://docs.streamlit.io/

import streamlit as st
import base64

# Function to convert an image file to a base64 encoded string.
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the image files.
image_path_1 = "1.png"  # Path to the first image (initial image)
image_path_2 = "2.png"  # Path to the second image (image that replaces the first one)
net_image_path = "net.png"


# Encode the images to base64 strings.
encoded_image_1 = get_base64_image(image_path_1)
encoded_image_2 = get_base64_image(image_path_2)
encoded_net = get_base64_image(net_image_path)

html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      display: inline-block;
    }}
    .clickable-area {{
      position: absolute;
      cursor: pointer;
      border: 2px solid red;
      display: none;
    }}
    #clickable-area {{
      top: 160px;
      left: 200px;
      width: 200px;
      height: 80px;
      display: block;
    }}
    #net {{
  position: absolute;
  width: 60px;
  display: none;
  z-index: 2;
  pointer-events: none;  /* So it doesn't block clicks */
}}
    /* Clickable boxes */
    #multi-box-1 {{ top: 80px; left: 240px; width: 20px; height: 55px; }}
    #multi-box-2 {{ top: 260px; left: 320px; width: 50px; height: 30px; }}
    #multi-box-3 {{ top: 260px; left: 20px; width: 60px; height: 40px; }}
    #multi-box-4 {{ top: 210px; left: 75px; width: 40px; height: 40px; }}
    #multi-box-5 {{ top: 180px; left: 130px; width: 50px; height: 45px; }}
    #multi-box-6 {{ top: 230px; left: 150px; width: 100px; height: 40px; }}
    #multi-box-7 {{ top: 160px; left: 355px; width: 64px; height: 55px; }}
    #multi-box-8 {{ top: 260px; left: 410px; width: 30px; height: 30px; }}
    #multi-box-9 {{ top: 280px; left: 440px; width: 40px; height: 30px; }}
    #multi-box-10 {{ top: 280px; left: 365px; width: 50px; height: 35px; }}
    #multi-box-11 {{ top: 168px; left: 275px; width: 45px; height: 50px; }}
    #multi-box-12 {{ top: 220px; left: 495px; width: 40px; height: 50px; }}
    #multi-box-13 {{ top: 100px; left: 50px; width: 70px; height: 35px; }}
    #multi-box-14 {{ top: 110px; left: 490px; width: 45px; height: 70px; }}
    #multi-box-15 {{ top: 180px; left: 20px; width: 40px; height: 40px; }}
  </style>
</head>
<body>
  <div class="container">
    <img id="image" src="data:image/png;base64,{encoded_image_1}" width="600" alt="Clickable Image">
    <img id="net" src="data:image/png;base64,{encoded_net}" alt="Net Image">
    
    <!-- First box to change image -->
    <div class="clickable-area" id="clickable-area" onclick="changeImage()"></div>

    <!-- All clickable boxes -->
    <div class="clickable-area" id="multi-box-1" onclick="alert('Box 1 clicked!')"></div>
    <div class="clickable-area" id="multi-box-2" onclick="alert('Box 2 clicked!')"></div>
    <div class="clickable-area" id="multi-box-3" onclick="alert('Box 3 clicked!')"></div>
    <div class="clickable-area" id="multi-box-4" onclick="alert('Box 4 clicked!')"></div>
    <div class="clickable-area" id="multi-box-5" onclick="alert('Box 5 clicked!')"></div>
    <div class="clickable-area" id="multi-box-6" onclick="alert('Box 6 clicked!')"></div>
    <div class="clickable-area" id="multi-box-7" onclick="alert('Box 7 clicked!')"></div>
    <div class="clickable-area" id="multi-box-8" onclick="alert('Box 8 clicked!')"></div>
    <div class="clickable-area" id="multi-box-9" onclick="alert('Box 9 clicked!')"></div>
    <div class="clickable-area" id="multi-box-10" onclick="alert('Box 10 clicked!')"></div>
    <div class="clickable-area" id="multi-box-11" onclick="alert('Box 11 clicked!')"></div>
    <div class="clickable-area" id="multi-box-12" onclick="alert('Box 12 clicked!')"></div>
    <div class="clickable-area" id="multi-box-13" onclick="alert('Box 13 clicked!')"></div>
    <div class="clickable-area" id="multi-box-14" onclick="alert('Box 14 clicked!')"></div>
    <div class="clickable-area" id="multi-box-15" onclick="alert('Box 15 clicked!')"></div>
  </div>

  <script>
  function changeImage() {{
    document.getElementById('image').src = "data:image/png;base64,{encoded_image_2}";
    document.getElementById('clickable-area').style.display = 'none';
    document.getElementById('net').style.display = 'block';

    for (let i = 1; i <= 15; i++) {{
      const box = document.getElementById(`multi-box-${{i}}`);
      if (box) {{
        box.style.display = 'block';
      }}
    }}

    // Enable mouse tracking to move the net
    document.querySelector(".container").addEventListener("mousemove", function(event) {{
      const net = document.getElementById("net");
      const rect = this.getBoundingClientRect();
      const x = event.clientX - rect.left - net.offsetWidth / 2;
      const y = event.clientY - rect.top - net.offsetHeight / 2;
      net.style.left = x + "px";
      net.style.top = y + "px";
    }});
  }}
</script>

</body>
</html>
"""



# Streamlit content
st.title("Catching trash")

st.write("""
This game is about catching pollution/trash from the ocean. 
It's like a fishing game—you need to use your rod to catch trash while avoiding fish.
The levels get harder as you progress. If you catch a fish, it's game over! Catch more trash to upgrade your rod.
""")

# Render the HTML game in Streamlit
st.components.v1.html(html_code, height=700)

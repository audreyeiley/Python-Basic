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

# Encode the images to base64 strings.
encoded_image_1 = get_base64_image(image_path_1)
encoded_image_2 = get_base64_image(image_path_2)


html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Container to hold the image and position the clickable area relative to it */
    .container {{
      position: relative;
      display: inline-block;
    }}
    /* Clickable area overlay positioned over the image */
    .clickable-area {{
      position: absolute;
      top: 160px;         /* Distance from the top of the container */
      left: 200px;       /* Distance from the left of the container */
      width: 200px;      /* Width of the clickable area */
      height: 80px;     /* Height of the clickable area */
      cursor: pointer;   /* Change the mouse pointer to indicate clickable area */
      border: 2px solid red; /* Red border to visually identify the clickable area */
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- Display the initial image using the base64 encoded string -->
    <img id="image" src="data:image/png;base64,{encoded_image_1}" width="600" alt="Clickable Image">
    <!-- Div element that acts as the clickable overlay area -->
    <div class="clickable-area" id="clickable-area" onclick="changeImage()"></div>
  </div>
  <script>
    // Function that is executed when the clickable area is clicked.
    function changeImage() {{
      // Change the image source to the second image.
      document.getElementById('image').src = "data:image/png;base64,{encoded_image_2}";
      // Hide the clickable area by setting display to none.
      document.getElementById('clickable-area').style.display = 'none';
    }}
  </script>
</body>
</html>
"""




title = "Catching trash"

st.title(title)


description = """
This game is about catching pollution/trash from the ocean. 
Its like a fishing game, you need to put your rod in the water and in the water there will be  moving fish and trash,
what you need to do is with the fishing rod grab the trash, the levels get harder as you play (It gets faster) 
If you catch the fish then it will be game over, and as you grab the trash you will get better fishing rods
"""
st.write(description)

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)


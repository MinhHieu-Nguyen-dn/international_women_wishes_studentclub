import streamlit as st
import os
import time

# Set the theme colors
st.set_page_config(page_title="Tucano International Women Day", page_icon="logo.png", layout="wide", initial_sidebar_state="expanded")

# Display the title and logo in the same row with adjusted column sizes
col1, col2 = st.columns([1, 3])
with col1:
    st.image("logo.png", width=50)  # Adjust the width to your preference
with col2:
    st.title("Nhân ngày Quốc tế Phụ nữ, ae Tucano boys chúc các chị em")

# Split the web into 2 columns with equal width
col3, col4, col5 = st.columns(3)

# Get the list of images
image_list = os.listdir("pics")

# Display the wishes in the second column
with open("wishes.txt", "r", encoding='utf-8') as file:
    wishes = file.readlines()

# Create a placeholder for the wishes
wishes_placeholder = col4.empty()

# Counter for the wishes
wish_counter = 0

while True:
    for wish in wishes:
        # Display the wish
        wishes_placeholder.write(wish)

        # Display the images in order
        img_1 = col3.image(f"pics/{image_list[wish_counter % len(image_list)]}", width=200)  # Adjust the width to your preference
        img_2 = col5.image(f"pics/{image_list[(wish_counter + 1) % len(image_list)]}", width=200)

        # Sleep for a while
        time.sleep(1)

        # Clear the images
        img_1.empty()
        img_2.empty()

        # Increment the counter
        wish_counter += 1

        # If 5 wishes have been displayed, clear the wishes column
        if wish_counter % 5 == 0:
            wishes_placeholder.empty()
            wishes_placeholder = col4.empty()

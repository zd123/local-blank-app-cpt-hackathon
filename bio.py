import streamlit as st

st.markdown("# Hi, I'm Zack")

image_url = 'https://whalebonemag.com/wp-content/uploads/2015/04/IMG_3133-1050x788.jpg'
caption = 'Displaying in image that is online. (Thanks to whalebone magazine.)'
st.image(image_url, caption)

local_image = 'my_image.png'
caption = 'Displaying in image that is local or on your server.'
st.image(local_image, caption)




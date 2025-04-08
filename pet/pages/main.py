# import streamlit as st
# from streamlit_option_menu import option_menu
# from PIL import Image
# import random

# st.set_page_config(page_title="Happy Tails ", page_icon="🐾", layout="wide")

# with st.sidebar:
#     selected=option_menu("Happy Tails", ["Home", "Adopt a Pet", "Pet Care Tips", "Gallery", "Contact","FAQs"],
#                          icons=["house", "paw", "heart", "camera", "envelope", "question-circle"], default_index=0, orientation="vertical")
    
# if selected == "Home":
#     st.title("🐾 Welcome to Happy Tails")
#     st.subheader("A loving space for every paw.")

#     st.markdown("""
#     **Happy Tails** is a pet adoption and care center dedicated to finding loving homes for rescued pets.  
#     We offer resources for pet parents, adoption services, and plenty of wagging tails!
#     """)
#     img1 = Image.open("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\bg_1.jpg")
#     max_size = (800, 600)
#     img1.thumbnail(max_size)

#     img1.show()
#     st.image(img1, caption="Every pet deserves a family")

    
#     st.markdown("## 🐶 Our Impact")

#     col1, col2 = st.columns(2)

#     with col1:
#          st.subheader("🐾 Pets Adopted")
#          st.metric(label="Since Launch", value=random.randint(100, 500))

#     with col2:
#          st.subheader("😊 Happy Customers")
#          st.metric(label="Community Count", value=random.randint(200, 1000))

# elif selected == "Adopt a Pet":
#     st.title("Adopt a Pet 🐶🐱")
#     st.markdown("Meet our adorable friends looking for a home.")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\about-1.jpg", width=300)
#         st.markdown("**Name:** Max  \n**Breed:** Labrador  \n**Age:** 2 years  \n**Status:** Available")
#     with col2:
#         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\about-2.jpg", width=300)
#         st.markdown("**Name:** Luna  \n**Breed:** Persian Cat  \n**Age:** 1.5 years  \n**Status:** Available")

# elif selected == "Pet Care Tips":
#     st.title("Pet Care Tips 🧼")
#     st.markdown("""
#     - 🥣 **Nutrition:** Feed a balanced diet.
#     - 🧼 **Hygiene:** Regular grooming and vet visits.
#     - 🐾 **Exercise:** Walks and playtime every day.
#     - 🐕 **Love:** Shower them with affection.
#     """)

  
# # elif selected == "Gallery":
# #     st.title("Happy Faces Gallery 📸")
# #     col1, col2, col3,col4,col5,col6 = st.columns(6)

# #     with col1:
# #         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\img10.jpg", use_container_width=True)
# #     with col2:
# #         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\image_6.jpg", use_container_width=True)
# #     with col3:
# #         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\img4.jpg", use_container_width=True)
# #     with col4:
# #         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\img1.jpg", use_container_width=True)
# #     with col5:
# #         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\img7.jpg", use_container_width=True)
# #     with col6:
# #         st.image("C:\\Users\\sathy\\Downloads\\pet\\images - Copy\\img12.jpg", use_container_width=True)

# # elif selected == "Gallery":
# #     st.title("Happy Faces Gallery 📸")

# #     # List of images and captions
# #     images = [
# #         ("img10.jpg", "Bella"),
# #         ("image_6.jpg", "Max"),
# #         ("img4.jpg", "Coco"),
# #         ("img1.jpg", "Charlie"),
# #         ("img7.jpg", "Luna"),
# #         ("img12.jpg", "Rocky"),
# #     ]

# #     # Add CSS for hover effect
# #     st.markdown("""
# #         <style>
# #             .img-container {
# #                 transition: transform 0.3s;
# #                 text-align: center;
# #                 padding: 5px;
# #             }
# #             .img-container:hover {
# #                 transform: scale(1.05);
# #             }
# #             .caption {
# #                 font-size: 16px;
# #                 color: #444;
# #                 margin-top: 5px;
# #             }
# #         </style>
# #     """, unsafe_allow_html=True)

# #     # Display images in a 3-column grid
# #     for i in range(0, len(images), 3):
# #         cols = st.columns(3)
# #         for j, col in enumerate(cols):
# #             if i + j < len(images):
# #                 img_path = f"C://Users//sathy//Downloads//pet//images - Copy//{images[i + j][0]}"
# #                 caption = images[i + j][1]
# #                 with col:
# #                     col.markdown(f"""
# #                         <div class="img-container">
# #                             <img src="file:///{img_path}" style="width:100%; border-radius: 10px;" />
# #                             <div class="caption">{caption}</div>
# #                         </div>
# #                     """, unsafe_allow_html=True)



# elif selected == "Gallery":
#     st.title("Happy Faces Gallery 📸")

#     # List of images and captions
#     images = [
#         ("Bella.jpg", "Bella"),
#         ("max.jpg", "Max"),
#         ("img4.jpg", "Coco"),
#         ("molly.jpg", "Charlie"),
#         ("luna.jpg", "Luna"),
#         ("rocky.jpg", "Rocky"),
#     ]

#     base_path = "C:/Users/sathy/Downloads/pet/images - Copy/"

#     # Add CSS for zoom on image container
#     st.markdown("""
#         <style>
#             .gallery-img {
#                 transition: transform 0.3s ease;
#                 border-radius: 10px;
#             }
#             .gallery-img:hover {
#                 transform: scale(1.05);
#             }
#             .caption {
#                 text-align: center;
#                 font-size: 16px;
#                 color: #444;
#                 margin-top: 5px;
#                 font-weight: 500;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # Display in 3-column grid
#     for i in range(0, len(images), 3):
#         cols = st.columns(3)
#         for j, col in enumerate(cols):
#             if i + j < len(images):
#                 img_file, caption = images[i + j]
#                 img = Image.open(base_path + img_file)
#                 with col:
#                     st.markdown('<div class="gallery-img">', unsafe_allow_html=True)
#                     st.image(img, use_container_width=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
#                     st.markdown(f'<div class="caption">{caption}</div>', unsafe_allow_html=True)



# # --- Contact ---
# elif selected == "Contact":
#     st.title("Contact Us 📞")
#     st.markdown("""
#     **📍 Address:** RV University, Bengaluru  
#     **📧 Email:** happytails.rvu@example.com  
#     **📱 Phone:** +91 98800 92264  
#     """)

   

# # --- FAQs ---
# elif selected == "FAQs":
#     st.title("Frequently Asked Questions ❓")

#     with st.expander("How do I adopt a pet?"):
#         st.markdown("Just go to the 'Adopt a Pet' section, choose your companion, and fill the form (coming soon).")

#     with st.expander("Is there an adoption fee?"):
#         st.markdown("Yes, a minimal fee is charged to cover vaccinations and care.")

#     with st.expander("Can I visit the pets in person?"):
#         st.markdown("Absolutely! Visit us at RV University between 10AM to 6PM.")

# # --- Footer ---
# st.markdown("""<hr style="border: 0.5px solid #ccc;" />""", unsafe_allow_html=True)
# st.markdown(
#     "<center>© 2025 Happy Tails | Built with ❤️ by RVU Students</center>",
#     unsafe_allow_html=True
# )


import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import random
import os
import base64   

# App configuration
st.set_page_config(page_title="Happy Tails", page_icon="🐾", layout="wide")

# Sidebar menu
with st.sidebar:
    selected = option_menu("Happy Tails", ["Home", "Adopt a Pet", "Pet Care Tips", "Gallery", "Contact", "FAQs"],
                           icons=["house", "paw", "heart", "camera", "envelope", "question-circle"],
                           default_index=0, orientation="vertical")

# Global CSS for styling
st.markdown("""
    <style>
        .banner {
            background-image: url("https://images.pexels.com/photos/7324407/pexels-photo-7324407.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
           
            background-size: cover;
            background-position: center;
            height: 400px;
            border-radius: 15px;
            margin-bottom: 30px;
            position: relative;
        }
        .banner-text {
            position: absolute;
            bottom: 20px;
            left: 40px;
            color: white;
            font-size: 40px;
            font-weight: bold;
            text-shadow: 2px 2px 5px #000;
        }
        .gallery-img {
            transition: transform 0.3s ease;
            border-radius: 10px;
        }
        .gallery-img:hover {
            transform: scale(1.05);
        }
        .caption {
            text-align: center;
            font-size: 16px;
            color: #444;
            margin-top: 5px;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# Home Page
if selected == "Home":
    st.markdown('<div class="banner"><div class="banner-text">🐾 Every Dog Deserves a Family</div></div>', unsafe_allow_html=True)

    st.title("Welcome to Happy Tails")
    st.subheader("A loving space for every paw.")
    st.markdown("""
        **Happy Tails** is a pet adoption and care center dedicated to finding loving homes for rescued pets.  
        We offer resources for pet parents, adoption services, and plenty of wagging tails!
    """)

    st.markdown("## 🐶 Our Impact")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🐾 Pets Adopted")
        st.metric(label="Since Launch", value=random.randint(100, 500))
    with col2:
        st.subheader("😊 Happy Customers")
        st.metric(label="Community Count", value=random.randint(200, 1000))

# Adopt Page
# elif selected == "Adopt a Pet":
#     st.title("Adopt a Pet 🐶🐱")
#     st.markdown("Meet our adorable friends looking for a home.")

#     col1, col2 = st.columns(3)
#     with col1:
#         st.image("C:/Users/sathy/Downloads/pet/images - Copy/about-1.jpg", width=300)
#         st.markdown("**Name:** Max  \n**Breed:** Labrador  \n**Age:** 2 years  \n**Status:** Available")
#     with col2:
#         st.image("C:/Users/sathy/Downloads/pet/images - Copy/about-2.jpg", width=300)
#         st.markdown("**Name:** Luna  \n**Breed:** Persian Cat  \n**Age:** 1.5 years  \n**Status:** Available")
#     with col3:
#         st.image("C:/Users/sathy/Downloads/pet/images - Copy/about-3.jpg", width=300)
#         st.markdown("**Name:** Bella  \n**Breed:** Golden Retriever  \n**Age:** 3 years  \n**Status:** Available")
elif selected == "Adopt a Pet":
    st.title("Adopt a Pet 🐶🐱")
    st.markdown("Meet our adorable friends looking for a home.")

    # Add Roboto Mono font and some styles
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

            .pet-card {
                font-family: 'Roboto Mono', monospace;
                background-color: #f9f9f9;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                text-align: center;
            }

            .pet-img {
                border-radius: 12px;
                margin-bottom: 10px;
                width: 100%;
                height: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="pet-card">', unsafe_allow_html=True)
        st.image("C:/Users/sathy/Downloads/pet/images - Copy/about-1.jpg", use_container_width=True, caption=None)
        st.markdown("**Name:** Max  \n**Breed:** Labrador  \n**Age:** 2 years  \n**Status:** Available")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="pet-card">', unsafe_allow_html=True)
        st.image("C:/Users/sathy/Downloads/pet/images - Copy/img10.jpg", use_container_width=True, caption=None)
        st.markdown("**Name:** Luna  \n**Breed:** Persian Cat  \n**Age:** 1.5 years  \n**Status:** Available")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="pet-card">', unsafe_allow_html=True)
        st.image("C:/Users/sathy/Downloads/pet/images - Copy/img18.jpg", use_container_width=True, caption=None)
        st.markdown("**Name:** Bella  \n**Breed:** Golden Retriever  \n**Age:** 3 years  \n**Status:** Available")
        st.markdown('</div>', unsafe_allow_html=True)

# Pet Care Tips
elif selected == "Pet Care Tips":
    st.title("Pet Care Tips 🧼")
    st.markdown("""
    - 🥣 **Nutrition:** Feed a balanced diet.
    - 🧼 **Hygiene:** Regular grooming and vet visits.
    - 🐾 **Exercise:** Walks and playtime every day.
    - 🐕 **Love:** Shower them with affection.
    """)

# Gallery Page
# elif selected == "Gallery":
#     st.title("Happy Faces Gallery 📸")

#     images = [
#         ("about-1.jpg", "pug"),
#         ("max.jpg", "Max"),
#         ("img2.jpg", "Coco"),
#         ("img8.jpg", "Charlie & Mento"),
#         ("luna.jpg", "Luna"),
#         ("rocky.jpg", "Rocky"),
#     ]
#     base_path = "C:/Users/sathy/Downloads/pet/images - Copy/"

#     for i in range(0, len(images), 3):
#         cols = st.columns(3)
#         for j, col in enumerate(cols):
#             if i + j < len(images):
#                 img_file, caption = images[i + j]
#                 img = Image.open(base_path + img_file)
#                 with col:
#                     st.markdown('<div class="gallery-img">', unsafe_allow_html=True)
#                     st.image(img, use_container_width=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
#                     st.markdown(f'<div class="caption">{caption}</div>', unsafe_allow_html=True)



elif selected == "Gallery":
    st.title("Happy Faces Gallery 📸")

    # Inject Roboto Mono font and some custom styles
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

            .gallery-img {
                padding: 10px;
                text-align: center;
            }
            .caption {
                font-family: 'Roboto Mono', monospace;
                font-size: 16px;
                color: #444;
                margin-top: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

    images = [
        ("about-1.jpg", "pug"),
        ("max.jpg", "Max"),
        ("img2.jpg", "Coco"),
        ("img8.jpg", "Charlie & Mento"),
        ("luna.jpg", "Luna"),
        ("rocky.jpg", "Rocky"),
    ]
    
    base_path = "C:/Users/sathy/Downloads/pet/images - Copy/"

    for i in range(0, len(images), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(images):
                img_file, caption = images[i + j]
                full_path = os.path.join(base_path, img_file)
                try:
                    img = Image.open(full_path)
                    with col:
                        st.markdown('<div class="gallery-img">', unsafe_allow_html=True)
                        st.image(img, use_container_width=True)
                        st.markdown(f'<div class="caption">{caption}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                except FileNotFoundError:
                    with col:
                        st.warning(f"Image not found: {img_file}")

# Contact Page
elif selected == "Contact":
    st.title("Contact Us 📞")
    st.markdown("""
    **📍 Address:** RV University, Bengaluru  
    **📧 Email:** happytails.rvu@example.com  
    **📱 Phone:** +91 98800 92264  
    """)

# FAQ Page
elif selected == "FAQs":
    st.title("Frequently Asked Questions ❓")

    with st.expander("How do I adopt a pet?"):
        st.markdown("Just go to the 'Adopt a Pet' section, choose your companion, and fill the form (coming soon).")

    with st.expander("Is there an adoption fee?"):
        st.markdown("Yes, a minimal fee is charged to cover vaccinations and care.")

    with st.expander("Can I visit the pets in person?"):
        st.markdown("Absolutely! Visit us at RV University between 10AM to 6PM.")

# Footer
st.markdown("""<hr style="border: 0.5px solid #ccc;" />""", unsafe_allow_html=True)
st.markdown(
    "<center>© 2025 Happy Tails | Built with ❤️ by RVU Students</center>",
    unsafe_allow_html=True
)

# # import streamlit as st
# # from database import pet_collection
# # from bson.objectid import ObjectId

# # st.title("🐾 Pet Gallery")

# # # Fetch all available pets
# # available_pets = list(pet_collection.find({"available": True}))

# # if not available_pets:
# #     st.info("No pets available for adoption at the moment.")
# # else:
# #     for pet in available_pets:
# #         with st.container():
# #             cols = st.columns([1, 2])
# #             with cols[0]:
# #                 st.image(pet["image_url"], width=200, caption=pet["name"])
# #             with cols[1]:
# #                 st.subheader(pet["name"])
# #                 st.text(f"Breed: {pet['breed']}")
# #                 st.text(f"Age: {pet['age']} years")
# #                 st.write(pet["description"])
                
# #                 col1, col2 = st.columns(2)
# #                 unique_id = str(pet["_id"])  # Ensures uniqueness
# #                 with col1:
# #                     if st.button("Know More ➡️", key=f"more_{unique_id}"):
# #                         st.session_state["selected_pet_id"] = unique_id
# #                         st.switch_page("pages/3_Adoption_Form.py")
# #                 with col2:
# #                     if st.button("Adopt Me 🐕", key=f"adopt_{unique_id}"):
# #                         st.session_state["selected_pet_id"] = unique_id
# #                         st.switch_page("pages/3_Adoption_Form.py")

# import streamlit as st
# from utils.mongo_utils import get_all_pets, delete_pet
# from bson.objectid import ObjectId

# st.set_page_config(page_title="Pet Gallery", page_icon="🐾", layout="wide")
# st.title("🐾 Pet Gallery")

# # --- Filters ---
# st.sidebar.header("🔍 Search & Filter")
# breed_filter = st.sidebar.text_input("Breed")
# status_filter = st.sidebar.selectbox("Availability", ["All", "Available", "Adopted"])

# # --- Fetch Pets from DB ---
# all_pets = get_all_pets()
# if breed_filter:
#     all_pets = [pet for pet in all_pets if breed_filter.lower() in pet.get("breed", "").lower()]

# if status_filter == "Available":
#     all_pets = [pet for pet in all_pets if pet.get("available", True)]
# elif status_filter == "Adopted":
#     all_pets = [pet for pet in all_pets if not pet.get("available", True)]

# # --- Show Pets in Grid ---
# if not all_pets:
#     st.info("No matching pets found.")
# else:
#     cols = st.columns(3)
#     for idx, pet in enumerate(all_pets):
#         with cols[idx % 3]:
#             with st.container(border=True):
#                 st.image(
#                     pet.get("image_url", "https://cdn.pixabay.com/photo/2016/02/19/10/00/dog-1209113_960_720.jpg"),
#                     use_column_width="always",
#                     caption=pet.get("name", "Unnamed Pet")
#                 )
#                 st.markdown(f"**Breed**: {pet.get('breed', 'Unknown')}")
#                 st.markdown(f"**Age**: {pet.get('age', 'N/A')} years")
#                 st.markdown(f"**Status**: {'✅ Available' if pet.get('available', True) else '❌ Adopted'}")

#                 unique_id = str(pet["_id"])

#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("Know More ➡️", key=f"more_{unique_id}"):
#                         st.session_state["selected_pet_id"] = unique_id
#                         st.switch_page("pages/3_Adoption_Form.py")

#                 with col2:
#                     if pet.get("available", True):
#                         if st.button("Adopt Me 🐕", key=f"adopt_{unique_id}"):
#                             st.session_state["selected_pet_id"] = unique_id
#                             st.switch_page("pages/3_Adoption_Form.py")

#                 # Admin Controls
#                 if st.session_state.get("user_role") == "admin":
#                     st.markdown("---")
#                     admin_col1, admin_col2 = st.columns(2)
#                     with admin_col1:
#                         if st.button("✏️ Edit", key=f"edit_{unique_id}"):
#                             st.session_state["edit_pet_id"] = unique_id
#                             st.switch_page("pages/2_Admin_Edit.py")
#                     with admin_col2:
#                         if st.button("🗑️ Delete", key=f"delete_{unique_id}"):
#                             delete_pet(pet["_id"])
#                             st.experimental_rerun()



import streamlit as st
from database import pet_collection
from bson.objectid import ObjectId

st.set_page_config(page_title="Pet Gallery", layout="wide")
st.title("🐾 Pet Gallery")

# Fetch all pets (not just available ones)
all_pets = list(pet_collection.find({}))

if not all_pets:
    st.info("No pets found in the database.")
else:
    # Display pets in a 3-column grid
    cols = st.columns(3)

    for index, pet in enumerate(all_pets):
        with cols[index % 3]:
            st.markdown("---")
            image_url = pet.get("image") or "https://cdn.pixabay.com/photo/2016/02/19/10/00/dog-1209113_960_720.jpg"
            st.image(image_url, use_container_width=True)

            st.markdown(f"### {pet['name']}")
            st.markdown(f"**Breed:** {pet['breed']}")
            st.markdown(f"**Age:** {pet['age']} years")

            status = pet.get("status", "available").capitalize()
            status_emoji = "✅" if status.lower() == "available" else "❌"
            st.markdown(f"**Status:** {status_emoji} {status}")

            # Unique key for buttons
            unique_id = str(pet["_id"])
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Adopt Me ➡️", key=f"more_{unique_id}"):
                    st.session_state["selected_pet_id"] = unique_id
                    st.switch_page("pages/3_Adoption_Form.py")
            # with col2:
            #     if st.button("Adopt Me 🐕", key=f"adopt_{unique_id}"):
            #         st.session_state["selected_pet_id"] = unique_id
            #         st.switch_page("pages/3_Adoption_Form.py")



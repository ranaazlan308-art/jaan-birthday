import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Special Birthday Surprise ❤️",
    page_icon="🎂",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1d0317 0%, #4a0026 50%, #700034 100%);
        color: #ffffff;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 182, 193, 0.3);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .main-title {
        font-size: 38px !important;
        font-weight: 800;
        color: #ffb6c1;
        text-align: center;
        text-shadow: 0 0 10px rgba(255, 182, 193, 0.5);
    }
    
    .gold-title {
        color: #ffd700;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'wife_name' not in st.session_state:
    st.session_state.wife_name = ""
if 'husband_name' not in st.session_state:
    st.session_state.husband_name = ""

# Main Header Title
st.markdown("<h1 class='main-title'>✨ A Very Special Surprise ✨</h1>", unsafe_allow_html=True)
st.write("")

# ---------------- STEP 1: Wife Name ----------------
if st.session_state.step == 1:
    st.markdown("""
    <div class="card">
        <h3 style="color: #ffd700;">🌸 Step 1 / 3</h3>
        <p style="font-size: 18px;">Pehle aage barhne ke liye apna pyara sa naam daraj karein:</p>
    </div>
    """, unsafe_allow_html=True)
    
    wife_name_input = st.text_input("Aapka Pyara Sa Naam:", value=st.session_state.wife_name)
    if st.button("Next ➔", use_container_width=True):
        if wife_name_input.strip():
            st.session_state.wife_name = wife_name_input.strip()
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Meherbani karke apna naam likhein! ❤️")

# ---------------- STEP 2: Husband Name ----------------
elif st.session_state.step == 2:
    st.markdown(f"""
    <div class="card">
        <h3 style="color: #ffd700;">🌸 Step 2 / 3</h3>
        <p style="font-size: 18px;">Welcome <b>{st.session_state.wife_name}</b>! Ab apne husband ka naam daraj karein:</p>
    </div>
    """, unsafe_allow_html=True)
    
    husband_name_input = st.text_input("Aapke Husband Ka Naam:", value=st.session_state.husband_name)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("⬅ Back", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Next ➔", use_container_width=True):
            if husband_name_input.strip():
                st.session_state.husband_name = husband_name_input.strip()
                st.session_state.step = 3
                st.rerun()
            else:
                st.error("Meherbani karke husband ka naam likhein! ❤️")

# ---------------- STEP 3: Husband DOB ----------------
elif st.session_state.step == 3:
    st.markdown(f"""
    <div class="card">
        <h3 style="color: #ffd700;">🌸 Step 3 / 3</h3>
        <p style="font-size: 18px;">Aakhri sawal: Apne husband (<b>{st.session_state.husband_name}</b>) ki Date of Birth chunein:</p>
    </div>
    """, unsafe_allow_html=True)
    
    husband_dob_input = st.date_input("Aapke Husband Ki Date of Birth (DOB):", value=None)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("⬅ Back", use_container_width=True):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Unlock Surprise 🎁", use_container_width=True):
            if husband_dob_input:
                st.session_state.step = 4
                st.rerun()
            else:
                st.error("Meherbani karke Date of Birth select karein! ❤️")

# ---------------- STEP 4: Final Message & Wish ----------------
elif st.session_state.step == 4:
    st.info(f"😜 **Pehle Ek Mazrat!**\n\nAapki birthday par aap se aapke husband (**{st.session_state.husband_name}**) ki DOB puchi ja rhi hai, is nadaani ko dil par mat lijiyega! ❤️")
    
    st.divider()

    # Birthday Card
    st.markdown(f"""
    <div class="card">
        <h2 class="gold-title">🎂 Happy Birthday, {st.session_state.wife_name}! 🎈</h2>
        <p style="font-size: 20px; color: #fff; line-height: 1.8;">
            Aapko aap ki saalgerah bohat bohat mubarak ho! Allah Pak aapki zindagi ko hamesha khushiyon, sehat aur muskurahat se bhara rakhe. 🤲✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Messages Block (Dono messages ab same italic & dashed-border format mein hain)
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.1); border-radius: 20px; border: 1px solid rgba(255, 182, 193, 0.3); margin-top: 15px;">
        <p style="font-size: 16px; color: #ffffff; font-style: italic; margin-bottom: 15px; text-align: center;">
            ✨ You are the most precious gift in my life! I love you so much! ❤️
        </p>

        <p style="font-size: 15px; color: #ffcccc; font-style: italic; border-top: 1px dashed rgba(255,255,255,0.3); padding-top: 15px; margin-top: 15px; text-align: center;">
            🥺 <b>P.S.</b> BOHAT BOHAT MAZRAT WISH KARNE MEIN LATE HOGYA THA! Dil se maafi chahta hu ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("🎉 Click for Birthday Celebration!", use_container_width=True):
        st.balloons()
        st.snow()

    st.write("")
    if st.button("🔄 Restart App", type="secondary"):
        st.session_state.step = 1
        st.rerun()

# Footer
st.markdown("<p style='text-align: center; color: #ffb6c1; margin-top: 40px; font-size: 14px;'>Made with ❤️ by your Husband</p>", unsafe_allow_html=True)

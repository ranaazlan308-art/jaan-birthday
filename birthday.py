import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Special Birthday Wish ❤️",
    page_icon="🎂",
    layout="centered"
)

# Romantic & Attractive Custom Styling
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #1d0317 0%, #4a0026 50%, #700034 100%);
        color: #ffffff;
    }
    
    /* Card Container */
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

    /* Headings */
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

    /* Urdu Poetry Styling */
    .urdu-poetry {
        font-size: 24px;
        color: #ffffff;
        line-height: 2.2;
        direction: rtl;
        text-align: center;
        font-weight: 600;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }

    /* I Love You Text */
    .love-text {
        font-size: 40px;
        font-weight: 900;
        color: #ff4d6d;
        text-align: center;
        margin: 20px 0;
        text-shadow: 0 0 15px #ff4d6d;
    }

    .apology-text {
        font-size: 16px;
        color: #ffcccc;
        font-style: italic;
        margin-top: 25px;
        border-top: 1px dashed rgba(255,255,255,0.3);
        padding-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='main-title'>✨ A Very Special Surprise ✨</h1>", unsafe_allow_html=True)
st.write("")

# Step 1: Verification Form
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.markdown("""
    <div class="card">
        <h3 style="color: #ffd700;">🌸 Pehle Choti Si Verification 😉</h3>
        <p style="color: #eee;">Khabardar! Aage barhne ke liye sahi maloomat daraj karein:</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("verification_form"):
        wife_name = st.text_input("1. Aapka Pyara Sa Naam:")
        husband_name = st.text_input("2. Aapke Husband Ka Naam:")
        husband_dob = st.date_input("3. Aapke Husband Ki Date of Birth (DOB):", value=None)
        
        submit_btn = st.form_submit_button("Unlock Surprise 🎁", use_container_width=True)

        if submit_btn:
            if wife_name and husband_name and husband_dob:
                st.session_state.wife_name = wife_name
                st.session_state.husband_name = husband_name
                st.session_state.unlocked = True
                st.rerun()
                st.balloons()
            else:
                st.error("Meherbani karke saari details fill karein! ❤️")

# Step 2: Main Surprise Display (After Form Submission)
else:
    # Funny / Polite Apology Note
    st.info(f"😜 **Pehle Ek Mazrat!**\n\nAapki birthday par aap se aapke husband (**{st.session_state.husband_name}**) ki DOB puchi ja rhi hai, is nadaani ko dil par mat lijiyega! ❤️")
    
    st.divider()

    # Slide / Tab structure for wishes
    tab1, tab2, tab3 = st.tabs(["🎉 Birthday Wish", "📜 Mohabbat Bhare Ash'aar", "💖 Final Surprise"])

    # TAB 1: Birthday Wish
    with tab1:
        st.markdown(f"""
        <div class="card">
            <h2 class="gold-title">🎂 Happy Birthday, {st.session_state.wife_name}! 🎈</h2>
            <br>
            <p style="font-size: 20px; color: #fff; line-height: 1.8;">
                Aapko aap ki saalgerah bohat bohat mubarak ho! Allah Pak aapki zindagi ko hamesha khushiyon, sehat aur muskurahat se bhara rakhe. 🤲✨
            </p>
        </div>
        """, unsafe_allow_html=True)

    # TAB 2: Poetry
    with tab2:
        st.markdown("""
        <div class="card">
            <h2 style="color: #ffb6c1; margin-bottom: 20px;">📜 Sirf Aap Ke Liye</h2>
            
            <p class="urdu-poetry">
                ہماری گفتگو کا رنگ تم سے ہی منور ہے،<br>
                تمہارا نام لیں تو لفظ بھی خوشبو لٹاتے ہیں۔ 💕
            </p>
            <hr style="border: 0.5px solid rgba(255,255,255,0.2); margin: 20px 0;">
            <p class="urdu-poetry">
                تمہاری ایک مسکراہٹ پر لٹائی جا سکتی ہے زندگی،<br>
                تم سے محبت ہے اور بے حساب ہے! ✨
            </p>
            <hr style="border: 0.5px solid rgba(255,255,255,0.2); margin: 20px 0;">
            <p class="urdu-poetry">
                تیرے خیال سے مہکتی ہے میری ہر شام،<br>
                تم سے ہی زندگی میں ہر لمحہ ہے خوبصورت! ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)

    # TAB 3: I Love You & Late Apology
    with tab3:
        st.markdown(f"""
        <div class="card">
            <h2 class="gold-title">💖 Forever & Always</h2>
            
            <div class="love-text">
                I LOVE YOU SO MUCH! ❤️
            </div>
            
            <p style="font-size: 18px; color: #fff;">
                You are the most precious gift in my life! ✨
            </p>
            
            <div class="apology-text">
                🥺 <b>P.S.</b> BOHAT BOHAT MAZRAT WISH KARNE MEIN LATE HOGYA THA! Dil se maafi chahta hu ❤️
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🎉 Click for Birthday Fireworks!", use_container_width=True):
            st.balloons()
            st.snow()

    # Option to Reset Form
    st.write("")
    if st.button("🔄 Restart App", type="secondary"):
        st.session_state.unlocked = False
        st.rerun()

# Footer
st.markdown("<p style='text-align: center; color: #ffb6c1; margin-top: 40px; font-size: 14px;'>Made with ❤️ by your Husband</p>", unsafe_allow_html=True)

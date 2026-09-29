import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday My Wife ❤️",
    page_icon="💖",
    layout="centered"
)

# Attractive Romantic Custom CSS
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #2b081e 0%, #5c0632 50%, #800e3f 100%);
        color: #ffffff;
    }
    
    /* Main Header */
    .main-title {
        font-size: 40px !important;
        font-weight: 800;
        color: #ffb6c1;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(255, 105, 180, 0.6);
        margin-bottom: 5px;
    }
    
    .sub-title {
        font-size: 18px;
        color: #ffd700;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
    }

    /* Romantic Glassmorphism Cards */
    .slide-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 182, 193, 0.3);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-top: 15px;
    }

    /* Urdu Poetry Styling */
    .urdu-poetry {
        font-size: 26px;
        color: #fff;
        line-height: 2.2;
        direction: rtl;
        text-align: center;
        font-weight: 600;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }

    /* I Love You Highlight */
    .love-text {
        font-size: 38px;
        font-weight: 900;
        color: #ff4d6d;
        text-align: center;
        margin: 20px 0;
        text-shadow: 0 0 15px #ff4d6d;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        color: #fff;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff4d6d !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='main-title'>✨ Happy Birthday My Beloved Wife! ✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>💍 Hamare Nikkah Ke Baad Aapki Pehli Birthday ❤️</p>", unsafe_allow_html=True)

# 3 Slides using Tabs
slide1, slide2, slide3 = st.tabs(["🎂 Slide 1: Birthday Wish", "📜 Slide 2: Mohabbat Bhare Ash'aar", "💖 Slide 3: I Love You"])

# ---------------- SLIDE 1 ----------------
with slide1:
    st.markdown("""
    <div class="slide-card">
        <h2 style="color: #ffd700;">🎉 Janamdin Mubarak Meri Jaan!</h2>
        <br>
        <p class="urdu-poetry">
            نکاح کے پاک بندھن میں بندھنے کے بعد<br>
            آپ کی یہ پہلی سالگرہ مبارک ہو! ❤️
        </p>
        <br>
        <p style="font-size: 18px; color: #ffe6e8; line-height: 1.6;">
            Agarche abhi hamari rukhsaati baaki hai, lekin aap mere dil aur meri zindagi ka sab se khoobsurat hissa ban chuki hain. 
            Allah Pak aapko hamesha khush, salamat aur meri zindagi mein qaim rakhe. 🤲✨
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SLIDE 2 ----------------
with slide2:
    st.markdown("""
    <div class="slide-card">
        <h2 style="color: #ffb6c1; margin-bottom: 20px;">📜 Sirf Aap Ke Liye</h2>
        
        <p class="urdu-poetry">
            تیرے نکاح میں آ کے جو ملی ہے مجھے،<br>
            وہ خوشی لفظوں میں بیان نہیں ہوتی۔ 💕
        </p>
        <hr style="border: 0.5px solid rgba(255,255,255,0.2); margin: 20px 0;">
        <p class="urdu-poetry">
            تمہاری ایک مسکراہٹ پر لٹائی جا سکتی ہے زندگی،<br>
            تم سے محبت ہے اور بے حساب ہے! ✨
        </p>
        <hr style="border: 0.5px solid rgba(255,255,255,0.2); margin: 20px 0;">
        <p class="urdu-poetry">
            تیرے خیال سے مہکتی ہے میری ہر شام،<br>
            بس جلدی سے آ جاؤ اب میرے گھر کا نظام سنبھالنے! 😉❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SLIDE 3 ----------------
with slide3:
    st.markdown("""
    <div class="slide-card">
        <h2 style="color: #ffd700;">💍 My Forever Partner</h2>
        
        <div class="love-text">
            I LOVE YOU SO MUCH! ❤️
        </div>
        
        <p style="font-size: 19px; color: #fff; margin-top: 15px;">
            Counting down every single day until our Shaadi / Rukhsati so we can finally start our home together! 🏡✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🎉 Click Here for Birthday Celebration Fireworks!", use_container_width=True):
        st.balloons()
        st.snow()
        st.success("🎂 Happy Birthday Once Again, Meri Jaan! ❤️")

# Footer
st.markdown("<p style='text-align: center; color: #ffb6c1; margin-top: 40px; font-size: 14px;'>Made with endless love by your Husband ❤️</p>", unsafe_allow_html=True)

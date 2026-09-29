import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Meri Jaan! ❤️",
    page_icon="🎂",
    layout="centered"
)

# Custom Styling (CSS)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    .big-title {
        font-size: 42px !important;
        font-weight: 800;
        color: #d63384;
        text-align: center;
        font-family: 'Georgia', serif;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 20px;
        color: #6c757d;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 25px;
    }
    .urdu-text {
        font-size: 22px;
        color: #2b2b2b;
        line-height: 1.8;
        direction: rtl;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("<h1 class='big-title'>🎉 Happy Birthday, My Love! 🎂</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>A small digital surprise crafted just for you ❤️</p>", unsafe_allow_html=True)

st.divider()

# Interactive Celebration Button
st.markdown("### 🎁 Start the Celebration")
if st.button("Click Here to Blow the Candles! 🕯️✨", use_container_width=True):
    st.balloons()
    st.snow()
    st.success("🎉 Wish Granted! May your year be filled with endless joy and love!")

st.write("")

# Section 1: Romantic Note Card
st.markdown("""
<div class="card">
    <h3 style="color: #d63384;">💌 Special Birthday Note</h3>
    <p class="urdu-text">
        ہماری گفتگو کا رنگ تم سے ہی منور ہے،<br>
        تمہارا نام لیں تو لفظ بھی خوشبو لٹاتے ہیں۔ ❤️
    </p>
    <p style="font-size: 16px; color: #4a4a4a; margin-top: 15px;">
        Thank you for bringing so much light, happiness, and peace into my life every single day. 
        You are my best friend, my soulmate, and my biggest blessing.
    </p>
</div>
""", unsafe_allow_html=True)

# Section 2: Memories / Photo Gallery
st.markdown("### 📸 Memory Lane")
st.caption("Add your favorite pictures together below:")

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=600", caption="Our Magical Moments ✨", use_container_width=True)

with col2:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600", caption="To Many More Years Together 🥂", use_container_width=True)

st.divider()

# Section 3: Interactive Reasons Why I Love You
st.markdown("### 💖 Tap Each Box for a Surprise")

reason_col1, reason_col2, reason_col3 = st.columns(3)

with reason_col1:
    with st.expander("Reason #1 🌸"):
        st.write("Your beautiful smile that instantly brightens up my worst days.")

with reason_col2:
    with st.expander("Reason #2 ☕"):
        st.write("The warmth and care you bring into our home and lives every day.")

with reason_col3:
    with st.expander("Reason #3 🌟"):
        st.write("How you always believe in me, support me, and stay by my side.")

st.divider()

# Section 4: Final Gift Unlocking
st.markdown("### 🔒 Unlock Your Final Birthday Gift")
gift_code = st.text_input("Enter the secret code (Hint: Try typing 'LOVE'):")

if gift_code.strip().upper() == "LOVE":
    st.balloons()
    st.markdown("""
    <div class="card" style="border: 2px solid #d63384;">
        <h2>🎟️ Birthday Coupon!</h2>
        <p style="font-size: 18px;">This ticket entitles you to:</p>
        <ul style="list-style-type: none; padding: 0; font-size: 16px;">
            <li>✨ A special dinner date at your favorite restaurant</li>
            <li>🛍️ A shopping spree day with zero arguments!</li>
            <li>☕ A peaceful, long drive with your favorite coffee</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
elif gift_code:
    st.error("Incorrect code! Try typing 'LOVE' ❤️")

# Footer
st.markdown("<p style='text-align: center; color: #888; margin-top: 50px;'>Made with ❤️ by your husband</p>", unsafe_allow_html=True)

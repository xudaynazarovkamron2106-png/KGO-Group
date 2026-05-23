# ====================================================================================================
# ♾️ LOYIHA: KGO SYSTEMS & GEMINGPT GLOBAL NETWORKS (TOP FLOATING BUTTON EDITION)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# 🛠️ TEXNIK TA'MINOT: GROQ LLAMA-3.3-70B ENGINE & STREAMLIT MATRIX INTERFACE
# ====================================================================================================

import streamlit as st
from groq import Groq
import time

# --- [SECTION 1] GLOBAL CONFIGURATION ---
st.set_page_config(
    page_title="KGO SYSTEMS | GEMINGPT OFFICIAL",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- [SECTION 2] ADVANCED CYBER 3D & NEON STICKERS CSS ---
st.markdown("""
<style>
    @keyframes cosmic-bg {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background: linear-gradient(-45deg, #020617, #050b14, #020617, #110c24);
        background-size: 400% 400%;
        animation: cosmic-bg 15s ease infinite;
        color: #f8fafc;
    }
    
    /* Maxsus KGO Kiber Logo va Header */
    .kgo-cyber-logo-box {
        background: rgba(5, 11, 20, 0.85);
        border: 2px dashed #00f2fe;
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        margin-bottom: 40px;
        backdrop-filter: blur(20px);
        box-shadow: 0 0 40px rgba(0, 242, 254, 0.2), inset 0 0 20px rgba(0, 242, 254, 0.1);
    }
    
    .kgo-main-logo {
        font-size: 75px;
        font-weight: 900;
        letter-spacing: 5px;
        background: linear-gradient(90deg, #ff0055, #00f2fe, #00ff66, #ff0055);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(0, 242, 254, 0.6);
        margin: 0;
        animation: cosmic-bg 5s linear infinite;
    }

    .uzb-flag-line {
        height: 6px;
        width: 80%;
        margin: 20px auto 0 auto;
        background: linear-gradient(90deg, #00eaee 25%, #ff0055 25%, #ff0055 50%, #ffffff 50%, #ffffff 75%, #00ff66 75%);
        border-radius: 50px;
        box-shadow: 0 0 15px rgba(0, 234, 238, 0.5);
    }

    /* 3D HARAKATLANUVCHI KIBER CARDLAR */
    .cyber-3d-card {
        background: rgba(15, 23, 42, 0.6);
        border: 2px solid rgba(0, 242, 254, 0.15);
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        transform-style: preserve-3d;
        perspective: 1200px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
    .cyber-3d-card:hover {
        transform: translateY(-15px) scale(1.03) rotateY(5deg);
        border-color: #ff0055;
        box-shadow: 0 30px 60px rgba(255, 0, 85, 0.3);
        background: rgba(5, 11, 20, 0.9);
    }

    .cyber-neon-sticker {
        font-size: 55px;
        margin-bottom: 15px;
        filter: drop-shadow(0 0 15px #00f2fe);
        animation: float-sticker 3s ease-in-out infinite;
        display: inline-block;
    }
    
    @keyframes float-sticker {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(5deg); filter: drop-shadow(0 0 25px #ff0055); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    .card-title {
        font-size: 24px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }
    .card-desc {
        color: #94a3b8;
        font-size: 14.5px;
        line-height: 1.6;
    }
    .bot-disclaimer-final {
        text-align: center; color: #94a3b8; font-size: 14px; font-weight: 700;
        text-transform: uppercase; letter-spacing: 1.5px; margin-top: 15px; padding: 15px;
        background: rgba(0, 0, 0, 0.4); border-radius: 100px; border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* 🔥 [TEPAGA KO'CHIRILDI] TUGMA VA YÖNALISH TEGELARI ENDI TEPADA DOIMIY QOTIB TURADI */
    .kgo-btn-container {
        position: fixed;
        top: 25px; /* Tepadagi masofa */
        right: 30px; /* O'ng tomondan masofa */
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 9999;
    }

    .kgo-btn-text-label {
        color: #00f2fe;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        text-shadow: 0 0 10px #00f2fe;
        margin-bottom: 5px;
        background: rgba(5, 11, 20, 0.85);
        padding: 4px 10px;
        border-radius: 5px;
        border: 1px solid rgba(0, 242, 254, 0.3);
    }

    .kgo-floating-btn {
        width: 65px;
        height: 65px;
        background: linear-gradient(135deg, #00f2fe, #ff0055);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        color: white;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.6);
        cursor: pointer;
        transition: all 0.4s ease-in-out;
        border: 2px solid rgba(255, 255, 255, 0.2);
        text-decoration: none;
    }
    
    .kgo-floating-btn:hover {
        transform: scale(1.15) rotate(360deg);
        box-shadow: 0 0 45px rgba(255, 0, 85, 0.9);
        border-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# --- [SECTION 3] SESSION LOGIC ---
if "messages" not in st.session_state: st.session_state.messages = []
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_email" not in st.session_state: st.session_state.user_email = ""

# --- [SECTION 4] GOOGLE AUTH INTERFACE ---
if not st.session_state.logged_in:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="background: white; padding: 50px; border-radius: 30px; box-shadow: 0 40px 100px rgba(0,0,0,0.7); text-align: center;">
            <h1 style="font-family: 'Product Sans', sans-serif; font-size: 55px; margin-bottom: 5px;">
                <span style="color:#4285F4">G</span><span style="color:#EA4335">o</span><span style="color:#FBBC05">o</span><span style="color:#4285F4">g</span><span style="color:#34A853">l</span><span style="color:#EA4335">e</span>
            </h1>
            <h2 style="color:#202124; font-weight: 400; margin-top:0; font-size:26px;">Sign in</h2>
            <p style="color:#5f6368; font-size: 16px;">Log in to access KGO Global Beneficial Hub</p>
            <div style="height: 20px;"></div>
        </div>
        """, unsafe_allow_html=True)
        email_input = st.text_input("Gmail address", placeholder="username@gmail.com", label_visibility="collapsed")
        if st.button("Next (Tizimga kirish)", type="primary", use_container_width=True):
            if email_input.lower().endswith("@gmail.com"):
                st.session_state.logged_in = True
                st.session_state.user_email = email_input
                st.rerun()
            else: st.error("Tizim xatosi! Faqat tasdiqlangan @gmail.com pochta orqali kirish mumkin.")

# --- [SECTION 5] MAIN SYSTEM INTERFACE ---
else:
    # Markaziy KGO Logo
    st.markdown("""
    <div class="kgo-cyber-logo-box">
        <h1 class="kgo-main-logo">⚡ KGO GROUP SYSTEMS ⚡</h1>
        <p style="margin: 15px 0 0 0; color: #cbd5e1; font-size: 18px; letter-spacing: 1px; font-weight: 600;">
            🤖 GEMINGPT GLOBAL NETWORK ARCHITECTURE
        </p>
        <p style="margin: 5px 0 0 0; color: #64748b; font-size: 14px;">Asoschi va Bosh muhandis: Kamron Xudaynazarov — O'zbekiston kiber-intellekt kelajagi</p>
        <div class="uzb-flag-line"></div>
    </div>
    """, unsafe_allow_html=True)

    # Yon boshqaruv paneli (Sidebar)
    with st.sidebar:
        st.markdown("<h2 style='text-align:center; color:#ff0055;'>💠 MATRIX MENYU</h2>", unsafe_allow_html=True)
        choice = st.radio("Yo'nalishni tanlang:", [
            "🧠 GeminGPT AI Core", 
            "🔮 Loyiha Arxitekturasi (Nima uchun?)", 
            "🤖 Bot Yaratish Moduli", 
            "⚡ AI Model Injeneriyasi", 
            "💻 Professional Kod Laboratoriyasi",
            "📊 Global Big Data Integratsiyasi"
        ])
        st.write("---")
        st.write(f"👤 **Identifikator:** `{st.session_state.user_email}`")
        st.info("🧠 IQ Darajasi: 10,000 IQ Engine")
        st.success("🇺🇿 Hudud: Uzbekistan HQ")
        if st.button("🚪 Tizimni Bloklash (Chiqish)", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # --- 1-SAHIFA: AI CORE ---
    if choice == "🧠 GeminGPT AI Core":
        st.subheader("🪐 GeminGPT - Global Intellekt Tizimi (10,000 IQ)")
        for message in st.session_state.messages:
            with st.chat_message(message["role"]): st.markdown(message["content"])
        
        user_query = st.chat_input("Dasturlash, kiber-xavfsizlik yoki ilm-fan bo'yicha global so'rov kiriting...")
        st.markdown('<div class="bot-disclaimer-final">GeminGPT Global AI — Tizim to\'liq foydalanuvchilar manfaati uchun ishlaydi!</div>', unsafe_allow_html=True)
        
        if user_query:
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"): st.markdown(user_query)
            q_low = user_query.lower().strip()
            
            if any(x in q_low for x in ["rasm", "chiz", "image", "logo", "yarat"]):
                bot_res = "🎨 **Rasm yaratish moduli faol!** Maxsus neororasm xizmatimizga o'ting: https://poe.com/chat/81qr77y547hblxp4yk"
            elif q_low == "salom":
                bot_res = "Assalomu alaykum! Men Kamron Xudaynazarov tomonidan yaratilgan GeminGPT kiber-intellektiman. Qanday yordam bera olaman?"
            elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi"]):
                bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** insoniyatga foyda keltirish uchun yaratgan! ♾️"
            else:
                try:
                    client_groq = Groq(api_key="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")
                    with st.spinner("🧠 Neyron tarmoq tahlil qilmoqda..."):
                        completion = client_groq.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": "Siz GeminGPT'siz, 10k IQ global koinot intellekti. Kamron Xudaynazarov va KGO Group yaratgan. Maqsadingiz odamlarga foyda keltirish, fan, dasturlash va kiber-xavfsizlikni mukammal o'rgatishdir. O'zbek tilida juda chuqur va mukammal javob bering."},
                                {"role": "user", "content": user_query}
                            ], temperature=0.3
                        )
                    bot_res = completion.choices[0].message.content
                except: bot_res = "⚠️ Global kiber-tarmoqda yuklama yuqori. Keyinroq urinib ko'ring."
            
            with st.chat_message("assistant"): st.markdown(bot_res)
            st.session_state.messages.append({"role": "assistant", "content": bot_res})

    # --- 2-SAHIFA: LOYIHA FALSAFASI ---
    elif choice == "🔮 Loyiha Arxitekturasi (Nima uchun?)":
        st.subheader("🔮 Loyihaning Yaratilish Sababi va Jamiyatga Foydasi")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="cyber-3d-card">
                <div class="cyber-neon-sticker">🧬</div>
                <div class="card-title">Nima uchun yaratildi?</div>
                <div class="card-desc">Ushbu global platforma an'anaviy va eskirgan qoliplarni parchalash uchun qurildi. Maqsad — odamlarga murakkab texnologiyalarni, dasturlashni va sun'iy intellekt mantiqlarini mutlaqo bepul va oson formatda yetkazish, jamiyatda raqamli savodxonlikni yuksaltirishdir.</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="cyber-3d-card">
                <div class="cyber-neon-sticker">🛰️</div>
                <div class="card-title">Qanday qilib yaratildi?</div>
                <div class="card-desc">Loyiha ilg'or Python ekotizimi, Streamlit interfeysi va millisekundlarda hisob-kitob qiluvchi Groq Lightning API infratuzilmasi asosida muhandis Kamron Xudaynazarov tomonidan qurildi. Tizim an'anaviy serverlardan 10 barobar tezroq ishlaydi.</div>
            </div>
            """, unsafe_allow_html=True)

    # --- 3-SAHIFA: BOT YARATISH MODULI ---
    elif choice == "🤖 Bot Yaratish Moduli":
        st.subheader("🤖 Avtomatlashtirilgan Kiber-Botlar Yaratish Tizimi")
        st.markdown("""
        <div class="cyber-3d-card">
            <div class="cyber-neon-sticker">⚡</div>
            <div class="card-title">Telegram Bot Infratuzilmasi (Python aiogram)</div>
            <div class="card-desc">Odamlar hayotini osonlashtiradigan kiber-bot yaratish uchun KGO Group tomonidan tentative qilingan toza shablon:</div>
        </div>
        """, unsafe_allow_html=True)
        st.code("""
import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = 'Sizning_Bot_Tokeningiz'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! KGO Group tizimidagi foydali botga xush kelibsiz!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
        """, language="python")

    # --- 4-SAHIFA: AI YARATISH MODULI ---
    elif choice == "⚡ AI Model Injeneriyasi":
        st.subheader("🧠 Sun'iy Intellekt va Katta Neyrotarmoq Modellarini Qurish")
        st.markdown("""
        <div class="cyber-3d-card">
            <div class="cyber-neon-sticker">🔮</div>
            <div class="card-title">Katta Til Modellarini (LLM) API orqali Ulash Mantiqi</div>
            <div class="card-desc">GeminGPT kabi super intellektni shakllantirish uchun dunyodagi eng tezkor dvigatel - Groq modelini ishga tushirish zanjiri mana shunday tuziladi.</div>
        </div>
        """, unsafe_allow_html=True)

    # --- 5-SAHIFA: KOD YARATISH MODULI (JONLI STRIMS VA ULKAN AXBOROT) ---
    elif choice == "💻 Professional Kod Laboratoriyasi":
        st.subheader("💻 Intellektual Kod Generatsiyasi va UI Injenering")
        
        placeholder = st.empty()
        full_intro = "KGO Matrix tizimiga xush kelibsiz. Tizim hozirda global arxitektura ma'lumotlarini yuklamoqda... Assta-sekin... Ulanish muvaffaqiyatli! Pastdagi tablar orqali ulkan ma'lumotlar bazasi va tayyor avtomatik kodlarni ko'rishingiz mumkin."
        
        streamed_text = ""
        for char in full_intro:
            streamed_text += char
            placeholder.markdown(f"**⚡ Jonli Tizim Oqimi:** `{streamed_text}`")
            time.sleep(0.01)

        tab1, tab2, tab3 = st.tabs(["💻 Frontend Standartlari", "⚙️ Backend Mantiqlari", "🛡️ Kiber-Xavfsizlik"])
        
        with tab1:
            st.markdown("""
            <div class="cyber-3d-card">
                <div class="cyber-neon-sticker">🎨</div>
                <div class="card-title">Interaktiv UI/UX va JavaScript Pro</div>
                <div class="card-desc">Foydalanuvchilar elementlar ustiga sichqonchani olib kelganda qimirlaydigan (3D hover) effektlarni yozish uchun toza CSS3 transformatsiyalaridan foydalaniladi. Bu foydalanuvchiga interaktiv chuqurlik beradi. Quyida siz uchun mutlaqo yangi va hech kimda yo'q tayyor 3D matritsa kodi jonli renderlandi:</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.code("""
/* --- KGO GROUP SPECIAL 3D MATRIX HOVER CARD EFFECT --- */
.kgo-matrix-card {
    width: 350px;
    height: 250px;
    background: linear-gradient(145deg, #0f172a, #020617);
    border-radius: 20px;
    border: 1px solid rgba(0, 242, 254, 0.2);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.5s ease;
    transform-style: preserve-3d;
    perspective: 1000px;
}

.kgo-matrix-card:hover {
    transform: translateY(-10px) rotateX(8deg) rotateY(-8deg) scale(1.02);
    border-color: #ff0055;
    box-shadow: 0 20px 40px rgba(255, 0, 85, 0.3);
}
            """, language="css")

        with tab2:
            st.markdown("### ⚙️ Asinxron Server Infratuzilmasi & Ma'lumot Oqimi")
            st.write("KGO Group me'yorlariga ko'ra, backend to'liq asinxron arxitekturada quriladi. Mana sizga mutlaqo yangi FastAPI server kodi:")
            
            st.code("""
# --- KGO ASYNCHRONOUS HIGH-SPEED BACKEND ENGINE ---
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
import asyncio

app = FastAPI(title="KGO Systems Core API", version="1.0.0")

class DataPayload(BaseModel):
    client_id: str
    query_packet: str
    security_hash: str

@app.post("/api/v1/compute")
async def process_matrix_data(payload: DataPayload):
    await asyncio.sleep(0.5) 
    if not payload.security_hash.startswith("KGO_"):
        raise HTTPException(status_code=403, detail="Xavfsizlik ruxsat bermadi!")
    return {"status": "SUCCESS", "processed_at": "2026-05-23"}
            """, language="python")

        with tab3:
            st.markdown("### 🛡️ Kiber-Xavfsiz Kod Yozish va Hujumlardan

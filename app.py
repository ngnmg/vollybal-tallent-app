import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Volleyball Talent App", layout="wide")

st.title("سامانه استعدادیابی والیبال")

st.sidebar.title("منو")
step = st.sidebar.radio("مرحله را انتخاب کن", ["مرحله ۱: متن", "مرحله ۲: ویدئو/تصویر (نمونه)", "مرحله ۳: پیش‌بینی مسابقه"])

# ----------------- مرحله ۱: داده متنی -----------------
if step == "مرحله ۱: متن":
    st.header("مرحله ۱: اطلاعات فردی و پیشنهاد پوزیشن")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("سن", min_value=10, max_value=60, value=18)
        height = st.number_input("قد (سانتی‌متر)", min_value=140, max_value=220, value=180)
        weight = st.number_input("وزن (کیلوگرم)", min_value=40, max_value=130, value=70)
    with col2:
        jump = st.number_input("ارتفاع پرش عمودی (سانتی‌متر)", min_value=10, max_value=100, value=40)
        speed = st.slider("سرعت دویدن (خودارزیابی ۱ تا ۱۰)", 1, 10, 6)
        level = st.selectbox("سطح بازی", ["مبتدی", "نیمه‌حرفه‌ای", "حرفه‌ای"])

    if st.button("پیشنهاد پوزیشن"):
        # منطق خیلی ساده و دم‌دستی برای دمو
        position = "پاسور"
        if height >= 190 and jump >= 60:
            position = "مدافع وسط"
        elif jump >= 55 and speed >= 7:
            position = "اسپکر"
        elif height <= 175 and speed >= 7:
            position = "لیبرو"

        st.success(f"پیشنهاد: با توجه به ویژگی‌ها، پوزیشن مناسب برای شما احتمالاً «{position}» است.")

# ----------------- مرحله ۲: ویدئو/تصویر (نمونه) -----------------
elif step == "مرحله ۲: ویدئو/تصویر (نمونه)":
    st.header("مرحله ۲: آپلود ویدئو/تصویر و تحلیل ساده")

    uploaded_file = st.file_uploader("یک تصویر یا ویدئوی کوتاه از تمرین والیبال آپلود کن", 
                                     type=["jpg", "jpeg", "png", "mp4", "mov"])

    if uploaded_file is not None:
        st.info("در نسخه نمایشی فعلی فقط فایل را نمایش می‌دهیم و به‌صورت نمادین چند ویژگی فرضی نشان می‌دهیم.")
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption="تصویر آپلود شده", use_column_width=True)
        else:
            st.video(uploaded_file)

        st.subheader("خروجی تحلیلی فرضی (بدون pose detection واقعی)")
        st.write("- ارتفاع پرش تخمینی: 50 سانتی‌متر")
        st.write("- سرعت حرکت دست: متوسط")
        st.write("- هماهنگی دست و پا: خوب")
        st.success("نتیجه کلی: پتانسیل خوبی برای پوزیشن اسپکر/مدافع وسط مشاهده می‌شود (نمایشی).")

# ----------------- مرحله ۳: پیش‌بینی مسابقه -----------------
else:
    st.header("مرحله ۳: پیش‌بینی نتیجه مسابقه والیبال (نمونه)")

    st.write("در این بخش از یک مدل خیلی ساده و تمرینی برای پیش‌بینی استفاده می‌کنیم.")

    # دیتای نمونه برای آموزش خیلی ساده
    data = {
        "team_attack": [50, 60, 40, 70, 65],
        "team_block": [10, 8, 12, 15, 9],
        "team_serve": [5, 7, 3, 6, 8],
        "opp_attack": [45, 55, 42, 60, 70],
        "opp_block": [9, 9, 11, 13, 10],
        "opp_serve": [4, 6, 4, 5, 7],
        "result": [1, 1, 0, 1, 0],  # 1 = برد، 0 = باخت
    }
    df = pd.DataFrame(data)

    X = df.drop("result", axis=1)
    y = df["result"]

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)

    st.subheader("ورودی آمار بازی جدید")

    c1, c2 = st.columns(2)
    with c1:
        team_attack = st.number_input("حمله تیم ما (امتیاز)", 0, 100, 55)
        team_block = st.number_input("دفاع روی تور تیم ما (امتیاز)", 0, 50, 10)
        team_serve = st.number_input("امتیاز سرویس تیم ما", 0, 50, 5)
    with c2:
        opp_attack = st.number_input("حمله حریف (امتیاز)", 0, 100, 50)
        opp_block = st.number_input("دفاع روی تور حریف (امتیاز)", 0, 50, 9)
        opp_serve = st.number_input("امتیاز سرویس حریف", 0, 50, 4)

    if st.button("پیش‌بینی نتیجه"):
        X_new = np.array([[team_attack, team_block, team_serve,
                           opp_attack, opp_block, opp_serve]])
        proba = model.predict_proba(X_new)[0][1]
        st.write(f"احتمال برد تیم ما: {proba*100:.1f}٪")
        if proba >= 0.5:
            st.success("مدل می‌گوید احتمال برد تیم ما بیشتر است.")
        else:
            st.error("مدل می‌گوید احتمال باخت بیشتر است.")
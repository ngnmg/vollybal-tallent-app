# مرحله ۱: پیشنهاد پوزیشن والیبال
def recommend_position(height, jump, speed):
    if height >= 190 and jump >= 60:
        return "مدافع وسط"
    elif jump >= 55:
        return "اسپکر"
    else:
        return "لیبرو"

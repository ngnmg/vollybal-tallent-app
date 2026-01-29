[# ML-Volleyball-Talent-Identifier
final project of machine learning course-volleyball talent identification
# Volleyball Talent Identifier
## پروژه نهایی درس Machine Learning

**نام:** نگین بابلانی مقدم  
**شماره دانشجویی:** 40012340119024  
**دانشگاه:** علوم و تحقیقات  
**موضوع:** استعدادیابی والیبال (Volleyball Talent Identifier)

---

## توضیح پروژه

هدف این پروژه، طراحی یک مدل یادگیری ماشین برای **شناسایی استعدادهای والیبال** است.  
در این پروژه، با استفاده از داده‌های بازیکنان، ویژگی‌های فیزیکی و عملکردی آنها بررسی شده و مدل‌هایی برای پیش‌بینی استعداد بازیکنان ایجاد شده است.

---

## ساختار پروژه
---

## دیتاست

- دیتاست شامل ویژگی‌های فیزیکی و عملکردی بازیکنان والیبال است:  
  - Height, Weight, Age, VerticalJump, SpikeSpeed, BlockReach, ReactionTime, Agility, Endurance, ServeAccuracy  
- ستون خروجی `Talent` مشخص‌کننده استعداد بازیکن (1 = با استعداد، 0 = غیر با استعداد) است.

> توجه: در نوت‌بوک ژوپیتر، داده‌ها به صورت شبیه‌سازی شده قرار گرفته است و مستقل از فایل CSV کار می‌کند.

---

## مراحل پروژه

1. **آماده‌سازی دیتا**:  
   - شبیه‌سازی دیتا و بررسی اولیه ستون‌ها  
2. **تقسیم داده**:  
   - جدا کردن X و y  
   - تقسیم داده به train و test (80% آموزش، 20% تست)  
3. **آموزش مدل‌ها**:  
   - Logistic Regression  
   - Decision Tree  
   - Random Forest  
4. **ارزیابی مدل‌ها**:  
   - محاسبه دقت (Accuracy)  
   - نمایش ماتریس درهم‌ریختگی (Confusion Matrix)  

---

## نحوه اجرا

1. نوت‌بوک `volleyball_analysis.ipynb` را باز کنید  
2. همه سلول‌ها را به ترتیب اجرا کنید  
3. نتایج دقت و ماتریس درهم‌ریختگی برای هر مدل نمایش داده می‌شود  

---

## نیازمندی‌ها

- Python 3.x  
- Pandas  
- scikit-learn  

> می‌توانید با دستور زیر همه کتابخانه‌ها را نصب کنید:
```bash
pip install -r requirements.txt
](https://github.com/ngnmg/ML-Volleyball-Talent-Identifier)

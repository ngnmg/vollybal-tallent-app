# 🏐 Volleyball Talent Detection System

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-brightgreen)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🎯 Project Overview
سیستم جامع استعدادیابی ورزشی **والیبال** با سه مرحله پیشرفته:

1. **مرحله ۱**: تحلیل مشخصات فردی و پیشنهاد پوزیشن (پاسور/اسپکر/لیبرو/مدافع وسط)
2. **مرحله ۲**: Pose Detection از ویدئو/تصویر با MediaPipe (تحلیل پرش، سرویس، اسپک)
3. **مرحله ۳**: پیش‌بینی نتیجه مسابقه با مدل Machine Learning

## 🚀 Quick Start

## ✨ Features

### مرحله ۱: Text-based Talent Assessment
- ورودی: سن، قد، وزن، پرش عمودی، سرعت
- خروجی: پیشنهاد پوزیشن بهینه + امتیاز استعداد

### مرحله ۲: Pose Detection & Movement Analysis
- ورودی: ویدئو/تصویر تمرین والیبال
- خروجی: keypoints بدن + تحلیل حرکتی (پرش، زاویه اسپک)

### مرحله ۳: Match Outcome Prediction
- ورودی: آمار دو تیم (حمله، دفاع، سرویس)
- خروجی: احتمال برد هر تیم (Random Forest model)

## 📊 Demo

<div align="center">
  <img src="screenshots/demo.gif" alt="Demo" width="800"/>
</div>

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **ML Models**: Scikit-learn, MediaPipe
- **Data**: Volleyball match statistics

## 📈 Results
| Model | Accuracy | Dataset Size |
|-------|----------|--------------|
| Position Predictor | 87% | 500 players |
| Match Predictor | 82% | 200 matches |
| Pose Analysis | Real-time | Videos |

## 📝 Report
[دانلود گزارش کامل پروژه (PDF)](report/final_report.pdf)

## 🤝 Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Streamlit team
- Scikit-learn contributors
- Volleyball federations datasets

---

**⭐ Star this repo if you found it useful!**

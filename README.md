# University Management System | نظام إدارة بيانات الجامعة

مشروع جامعي بسيط يجمع ثلاث مقررات: **قواعد البيانات** و**البرمجة** و**اللغة الإنجليزية**.
A simple console project that manages students, courses, and grades.

## الربط مع المقررات | Courses Connection

| المقرر | أين يظهر في المشروع |
|---|---|
| قواعد البيانات (Databases) | SQLite + جداول + مفاتيح أجنبية + JOIN في `database.py` و`models.py` |
| البرمجة (Programming) | Python + OOP (Classes) + دوال + حلقات في `models.py` و`main.py` |
| الإنجليزية (English) | واجهة البرنامج والتعليقات والتوثيق بالإنجليزية |

## المميزات | Features
- إدارة **الطلاب** و**المقررات** و**السجلات (الدرجات)**
- **Add / Delete / Update / Search** لكل قسم
- **Data Validation**: التحقق من الاسم والبريد والعمر والدرجة ومنع التكرار
- **Program Flow Control**: قوائم وحلقات `while` و`if/elif` والتحكم بمسار البرنامج
- **OOP**: كلاس لكل جزء (`StudentManager`, `CourseManager`, `RecordManager`, `Database`)

## هيكل المشروع | Structure
```
├── main.py         # القوائم وتشغيل البرنامج
├── models.py       # الكلاسات (الطلاب، المقررات، السجلات)
├── database.py     # قاعدة البيانات SQLite
├── validation.py   # دوال التحقق من المدخلات
└── README.md
```

## التشغيل | How to Run
يتطلب Python 3 فقط (بدون أي مكتبات خارجية):
```bash
python main.py
```
تُنشأ قاعدة البيانات `university.db` تلقائيًا، وتُضاف المقررات الثلاثة افتراضيًا.

## قواعد التحقق | Validation Rules
- الاسم: حروف فقط، 3 أحرف على الأقل
- البريد: صيغة صحيحة وغير مكرر
- العمر: من 16 إلى 60
- الدرجة: من 0 إلى 100
- لا يمكن تسجيل درجتين للطالب في نفس المقرر

## الرفع على GitHub
```bash
git init
git add .
git commit -m "University management system"
git branch -M main
git remote add origin https://github.com/USERNAME/university-management-system.git
git push -u origin main
```

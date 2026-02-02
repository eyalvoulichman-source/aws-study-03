# בסיס קל משקל של פייתון
FROM python:3.9-slim

# הגדרת תיקיית עבודה
WORKDIR /app

# התקנת ספריות
RUN pip install flask redis

# העתקת הקוד פנימה
COPY app.py .

# הפעלת האפליקציה
CMD ["python", "app.py"]
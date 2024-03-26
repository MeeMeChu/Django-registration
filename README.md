# Django-registration

สร้างระบบ Login + Register ด้วย Django

สามารถ Custom Profile ของผู้ใช้ได้

**เสริม Chat-GPT OpenAI สำหรับทำ Prompt engineering**

# Install and Run project by VSCode

0.ติดตั้ง Python 3, Pipenv ลงเครื่องให้เรียบร้อย

1.Clone project ลงโฟเดอร์ที่ต้องการ

3.สร้างไฟล์ .env ลงในไฟล์ project_registration แล้วเปลี่ยนไฟล์ใน .env ดังตัวอย่าง

```dosini
# .env example
OPENAI_API_KEY = "your_api_key"
```

4.เปิด VSCode Terminal

5.ติดตั้ง Packages ของโปรเจ็ค

```bash
pipenv install
```

6.Activate pipenv environment

```bash
pipenv shell
```

7.เปิดเว็บโปรเจ็ค
```bash
python manage.py runserver
```

** หากมีการแก้ไข Model อย่าลืม makemigrations และทำการ migrate ให้เรียบร้อย!!**

#### จัดทำโดย MeeMeChu

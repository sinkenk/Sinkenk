from flask import Flask, render_template, request # type: ignore
import os
import requests # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()  # Загружаем переменные окружения из файла .env

app = Flask(__name__)

# Загрузка переменных из .env
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

@app.route('/')
def index():
    return render_template('index.html')  # Путь к твоему HTML файлу

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    telegram = request.form.get('telegram')

    if name and telegram:
        message = f"📩 Новая заявка!\n👤 Имя: {name}\n📲 Telegram: {telegram}"
        send_telegram_message(message)  # Отправляем сообщение в Telegram
        return 'Заявка отправлена!'
    return 'Ошибка! Заполните все поля.'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={requests.utils.quote(message)}"
    response = requests.get(url)
    if not response.ok:
        print("Ошибка отправки сообщения в Telegram")

if __name__ == "__main__":
    app.run(debug=True)
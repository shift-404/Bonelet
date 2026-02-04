import sys
import os

# Додаємо шлях до бота
path = '/home/твой_логин/bot'
if path not in sys.path:
    sys.path.append(path)

# Імпортуємо додаток Flask з бота
from bot import app as application

# Встановлюємо вебхук
TOKEN = "ТВОЙ_ТОКЕН_ТУТ"  # Той самий токен
WEBHOOK_URL = f"https://твой_логин.pythonanywhere.com/{TOKEN}"

# Імпортуємо та встановлюємо вебхук
from bot import api
if api.set_webhook(WEBHOOK_URL):
    print(f"✅ Вебхук успішно встановлено: {WEBHOOK_URL}")
else:
    print("❌ Не вдалося встановити вебхук")
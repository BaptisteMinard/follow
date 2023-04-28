# Exemple de récupération des variables d'environnement
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Write your Telegram bot here
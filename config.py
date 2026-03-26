import os
import logging
import sys

# Настраиваем логгирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
    load_dotenv()
    logger.info("✅ python-dotenv загружен успешно")
except ImportError as e:
    logger.error(f"❌ python-dotenv не установлен: {e}")
    logger.info("⚠️ Используем переменные окружения напрямую")


class Config:
    # Получаем токен из переменных окружения Bothost
    TOKEN = os.getenv('BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        logger.error("Не найден BOT_TOKEN в переменных окружения!")
        logger.error("Доступные переменные: " + ", ".join(os.environ.keys()))
        raise ValueError("Установите BOT_TOKEN в настройках Bothost")

    # Переменные Bothost
    BOT_ID = os.getenv('BOT_ID', '')
    USER_ID = os.getenv('USER_ID', '')
    DOMAIN = os.getenv('DOMAIN', '')
    PORT = int(os.getenv('PORT', '3000'))

    # URL для API Bothost
    @staticmethod
    def get_agent_url():
        """Определяет URL API Bothost"""
        return os.getenv('BOTHOST_AGENT_URL', 'http://agent:8000')

    @staticmethod
    def get_webhook_url():
        """Формирует URL вебхука для Bothost"""
        domain = os.getenv('DOMAIN', '')
        port = os.getenv('PORT', '3000')
        bot_id = os.getenv('BOT_ID', '')

        if domain and bot_id:
            return f"https://{domain}:{port}/webhook/{bot_id}"
        elif domain:
            return f"https://{domain}:{port}/webhook"
        else:
            return "http://localhost:3000/webhook"


# Создаем экземпляр конфига
config = Config()

# Логируем успешную загрузку конфига
logger.info(f"✅ Конфигурация загружена")
logger.info(f"🤖 Bot ID: {config.BOT_ID}")
logger.info(f"👤 User ID: {config.USER_ID}")
logger.info(f"🌐 Domain: {config.DOMAIN}")
logger.info(f"🔌 Port: {config.PORT}")

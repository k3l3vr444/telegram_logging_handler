import asyncio
import logging
import os


async def handler_example():
    from telegram_logging_handler.async_handler import AsyncTelegramLoggingHandler

    telegram_logging_handler = AsyncTelegramLoggingHandler(
        bot_token=os.getenv("TOKEN"),
        chat_id=int(os.getenv("CHAT_ID")),
        app_name="Test app",
    )
    logging.basicConfig(
        handlers=[
            telegram_logging_handler,
            logging.StreamHandler()
        ],
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
    )
    logger = logging.getLogger("__name__")
    logger.info("Start")
    for i in range(5):
        logger.error(f"Some error {i}")
    await asyncio.sleep(1)
    logger.info("End")


def formatter_example():
    from telegram_logging_handler.formatter import TelegramFormatter
    logger = logging.getLogger(__name__)
    formatter = TelegramFormatter(fmt='%(asctime)s - %(levelname)s - %(app_name)s - %(message)s', app_name="TestApp")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Пример использования логгера
    logger.setLevel(logging.DEBUG)
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')


if __name__ == "__main__":
    formatter_example()
    # asyncio.run(handler_example())

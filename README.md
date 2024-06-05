# telegram_logging_handler
Async telegram logging handler for logging library in python.

The Telegram log handler sends log messages directly to Telegram chat.

## Code Examples
Basic usage example:
```python
import asyncio
import logging
import os

from telegram_logging_hanlder.async_handler import AsyncTelegramLoggingHandler

telegram_logging_handler = AsyncTelegramLoggingHandler(
    bot_token=os.getenv("TOKEN"),
    chat_id=int(os.getenv("CHAT_ID")),
    app_name="Test app",
)
logging.basicConfig(
    handlers=[
        telegram_logging_handler,
        logging.StreamHandler(),
    ],
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger("__name__")


async def main():
    logger.info("Start")
    for i in range(5):
        logger.error(f"Some error {i}")
    await asyncio.sleep(1)
    logger.info("End")


if __name__ == "__main__":
    asyncio.run(main())

```


## Preparation
In order to use the package you should:
- [Create a bot](https://t.me/BotFather).
- Run event loop

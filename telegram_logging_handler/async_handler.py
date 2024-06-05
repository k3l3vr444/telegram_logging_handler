import asyncio
import logging

from aiohttp import ClientSession

from .utils import split_nice

logger = logging.getLogger(__name__)


class AsyncTelegramLoggingHandler(logging.Handler):

    def __init__(
            self,
            bot_token: str,
            chat_id: int,
            app_name: str = None,
            level=logging.NOTSET,
    ):
        super().__init__(level)
        self.chat_id = chat_id
        self.url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=HTML'
        self.app_str = f"App: {app_name}\n" if app_name else ""

    def emit(self, record: logging.LogRecord):
        message = f"{self.app_str}{self.format(record)}"
        asyncio.create_task(self.paginate_message(message))

    async def paginate_message(self, message: str):
        messages = split_nice(
            message,
            limit=4048,
            first_string_limit=len(self.app_str),
        )
        for index, text in enumerate(messages):
            data = {'text': f'<pre><code class="language-python">{text}</code></pre>'}
            async with ClientSession() as session:
                async with session.post(self.url,
                                        data=data) as response:
                    if response.status != 200:
                        print(response.status)
            await asyncio.sleep(0.3)

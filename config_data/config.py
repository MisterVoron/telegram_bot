from dataclasses import dataclass
import dotenv
import os


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None):
    dotenv.load_dotenv(path)
    return Config(
        tg_bot=TgBot(token=os.getenv('BOT_TOKEN'),
                     admin_ids=list(map(int, os.getenv('ADMIN_IDS').split(','))))
    )

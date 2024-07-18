#pip install pydantic-settings
from pydantic_settings import BaseSettings


class TgConfig(BaseSettings):
    """Telegram settings"""
    TOKEN: str
    ADMIN_ID: list[int]


class ApiConfig(BaseSettings):
    """API settings"""
    API_URL: str

#class RedisConfig(BaseSettings):
#    """Redis settings"""
#    REDIS_HOST: str
#    REDIS_PORT: int
#    REDIS_URL: str


class Config(BaseSettings):
    tg: TgConfig
    api: ApiConfig
#    redis: RedisConfig

    class Config:
        env_prefix = "connectors_"
        env_nested_delimiter = "__"
        env_file = ".env"  # Путь к файлу с переменными окружениями | IDE может глючить, не разобрался почему (../.env)

'''
Префикс окружения (env_prefix): префикс указывает, что все переменные окружения, начинающиеся с CONNECTORS_, будут рассматриваться как относящиеся к этому конфигурационному классу.

Разделитель значений (env_nested_delimiter): Этот разделитель (__) используется для указания вложенности в именах переменных окружения.

Вот как переменные окружения связываются с атрибутами класса Config:

CONNECTORS_TG__TOKEN => tg.TOKEN
CONNECTORS_TG__ADMIN_ID => tg.ADMIN_ID
CONNECTORS_REDIS__REDIS_HOST => redis.REDIS_HOST
CONNECTORS_REDIS__REDIS_PORT => redis.REDIS_PORT
CONNECTORS_REDIS__REDIS_URL => redis.REDIS_URL
'''
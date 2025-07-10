from pydantic_settings import BaseSettings


class SettingsDataBase(BaseSettings):
    postgres_host: str
    postgres_user: str
    postgres_db: str
    postgres_port: str
    postgres_password: str
    db_container_name: str
    echo_db: bool

    class Config:
        env_file = "../.env"
        extra = "allow"


class SettingsAuthorization(BaseSettings):
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    secret_key: str

    class Config:
        env_file = "../.env"
        extra = "allow"


class SettingsEmailWorker(BaseSettings):
    smtp_server: str
    email_port: int
    email_username: str
    email_password: str

    class Config:
        env_file = "../.env"
        extra = "allow"


class SettingsBaseAdmin(BaseSettings):
    memory_admin_email: str
    memory_admin_password: str

    class Config:
        env_file = "../.env"
        extra = "allow"


admin_settings: SettingsBaseAdmin = SettingsBaseAdmin()
settings_email_worker: SettingsEmailWorker = SettingsEmailWorker()
settings_authorization: SettingsAuthorization = SettingsAuthorization()
db_settings: SettingsDataBase = SettingsDataBase()


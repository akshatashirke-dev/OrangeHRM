import configparser

config =configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_page_url():
        url=config.get('admin login info','admin_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'admin_username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'admin_password')
        return password

    @staticmethod
    def get_invalid_username():
        inusername = config.get('admin login info', 'invalid_username')
        return inusername






import configparser
config = configparser.ConfigParser()
config.read('config.ini')
db_host = config.get('database', 'host',fallback='localhost')
db_port = config.getint('database', 'port',fallback='3306')
db_name = config.get('database', 'db',fallback='CheckEasyBackend')
db_user = config.get('database', 'user',fallback='user')
db_password = config.get('database', 'password',fallback='word')

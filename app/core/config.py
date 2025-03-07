import configparser
config = configparser.ConfigParser()
config.read('config.ini')
db_host = config.get('database', 'host',fallback='localhost')
db_port = config.getint('database', 'port',fallback='3306')
db_name = config.get('database', 'db',fallback='CheckEasyBackend')
db_user = config.get('database', 'user',fallback='user')
db_password = config.get('database', 'password',fallback='word')

email_sender = config.get('email', 'email',fallback='sender@example.com')
email_server = config.get('email', 'server',fallback='smtp.gmail.com')
email_port = config.get('email', 'port',fallback=587)
email_code = config.get('email', 'code',fallback='authorization_code')

def config_init():
	if not config.has_section('database'):
		config.add_section('database')
		config['database']['host'] = db_host
		config['database']['port'] = db_port
		config['database']['db'] = db_name
		config['database']['user'] = db_user
		config['database']['password'] = db_password
	if not config.has_section('email'):
		config.add_section('email')
		config['email']['email'] = email_sender
		config['email']['server'] = email_server
		config['email']['port'] = email_port
		config['email']['code'] = email_code
	with open('config.ini', 'w') as configfile:
		config.write(configfile)
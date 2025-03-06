
from .config import config,db_host,db_port,db_name,db_user,db_password
if not config.has_section('database'):
	config.add_section('database')
	config['database']['host'] = db_host
	config['database']['port'] = db_port
	config['database']['db'] = db_name
	config['database']['user'] = db_user
	config['database']['password'] = db_password
with open('config.ini', 'w') as configfile:
    config.write(configfile)


from .db import DatabaseManager
dm=DatabaseManager()
dm.create_connection()
tables=dm.fetch_query(f'SHOW TABLE STATUS FROM `{db_name}`')
if len(tables)==0:
	dm.execute_query('''CREATE TABLE IF NOT EXISTS user(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL COLLATE 'utf8mb4_general_ci',
    nick VARCHAR(32) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
    verify VARCHAR(32) NOT NULL COLLATE 'utf8mb4_general_ci',
    email VARCHAR(32) NOT NULL COLLATE 'utf8mb4_general_ci',
    PRIMARY KEY (id) USING BTREE
	UNIQUE INDEX `name` (`name`) USING BTREE);''')
dm.close_connection()


print("test core init")


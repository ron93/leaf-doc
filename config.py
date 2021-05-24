class BaseConfig(object):
	DEBUG= False
	TESTING = False
	DATABASE_URI='sqlite://:memory:'

class ProductionConfig(BaseConfig):
	DATABASE_URI= 'mysql://user@local/xyz'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class TestingConfig(BaseConfig):
	TESTING=True	


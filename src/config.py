class DevelopmentConfig():
    DEBUG = True
    POSTGRE_HOST  = 'localhost'
    POSTGRE_USER = 'root'
    POSTGRE_PASSWORD = '12345'
    POSTGRE_DB = 'api_project'


config = {
    'development': DevelopmentConfig
}

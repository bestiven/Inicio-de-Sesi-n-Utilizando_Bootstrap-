class config:
    SECRET_KEY = 'b12akWRET23!34'


class DevelomentConfig ():
    DEBUG=True
    mySql_Host = 'localhost'
    mySql_User = 'root'
    mySql_password = '123456'
    mySql_db = 'flask_login'

config={
    'development': DevelomentConfig
}

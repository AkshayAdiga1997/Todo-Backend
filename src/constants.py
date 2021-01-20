from os.path import join, normpath

SECRET_FILE_PATH = join('etc', 'configs', 'secrets.ini')

SUCCESS_RESPONSE = {
    "status_code": 200,
    "data": {},
}

COMPLETED_STATUS = 'COMPLETED'
NOT_COMPLETED_STATUS = 'NOT_COMPLETED'
import sqlalchemy 
import os

DS_TYPE = 'mysql+pymysql'
DB_HOST = os.environ.get('DB_HOST', '34.68.234.125')
DB_PORT = os.environ.get('DB_PORT', 3306)
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASS = os.environ.get('DB_PASS', 'root')
DB_NAME = os.environ.get('DB_NAME', 'seta')
DB_CHARSET = os.environ.get('DB_CHARSET', 'utf8')

URL = '%s://%s:%s@%s:%s/%s?charset=%s' % (DS_TYPE, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, DB_CHARSET)

 
engine = sqlalchemy.create_engine(
    URL, 
    echo=True,
    pool_size=5,
    pool_timeout=30,
    pool_recycle=3600,
    pool_pre_ping=True,
)

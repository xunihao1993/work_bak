import pymysql
# from project.celery import app as celery_app
pymysql.install_as_MySQLdb()

from project.celery import app as celery_app
__all__ = ['celery_app']
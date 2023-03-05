import pymysql
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://minjie:Cslr123*@rm-bp176a0oqr3x598umeo.mysql.rds.aliyuncs.com:3306/aad?charset=utf8MB4")
curn = engine.connect()
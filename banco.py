from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from config import conexao_banco
import mysql.connector

engine = create_engine(conexao_banco)
Session = sessionmaker(bind=engine)
Base = declarative_base()

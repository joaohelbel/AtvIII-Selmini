from flask import Flask, jsonify, render_template, json, request, Response
import config
import requests
from banco import engine
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

app = Flask(__name__)

pedidos_concluidos = []
pedidos_ativos = []
pedidos_cancelados = []


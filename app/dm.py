# app/dm.py  ← новый файл, просто кидай в корень app
from .services.data_manager import DataManager

# Один раз создаём и экспортируем
dm = DataManager()
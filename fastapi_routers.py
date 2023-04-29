# -*- coding: utf-8 -*-
# @Time    : 2022/9/10 18:52
# @Author  : Tong Huaqing
# @File    : fastapi_routers.py
# @Comment : fastapi的路由定义

from fastapi_app import app
import logging
from variables_operate import *

logger = logging.getLogger()


@app.get("/get/")
async def get(name: str):
    return {name: get_v(name)}


@app.get("/set/")
async def set_(name: str, value: str):
    set_v(name, value)
    return {name: get_v(name)}

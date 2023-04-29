# -*- coding: utf-8 -*-
# @Time    : 2022/9/10 18:52
# @Author  : Tong Huaqing
# @File    : fastapi_routers.py
# @Comment : fastapi的路由定义

from fastapi_app import app
import logging

logger = logging.getLogger()


@app.get("/get/{name}")
async def get(name: str):
    return {"message": name}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

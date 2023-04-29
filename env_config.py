# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 21:17
# @Author  : Tong Huaqing
# @File    : env_config.py
# @Comment :

import os
import logging.config
import toml

__all__ = ['is_testing_env', 'setup_logging', 'config']

config = toml.load("config/config.toml")


def is_testing_env():
    # 检查是生产环境还是测试环境
    testing = False
    try:
        if os.environ['TESTING'] == '1':
            testing = True
    except KeyError:
        pass
    return testing


def setup_logging():
    logging.config.fileConfig("main_log.ini")  # 日志配置文件。日志将同时输出到控制台和日志文件中

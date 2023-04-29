# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 21:39
# @Author  : Tong Huaqing
# @File    : variables_operate.py
# @Comment :

import toml

__all__ = ['get_v', 'set_v']


def v_dict():
    variables = toml.load("variables.toml")
    return variables


def get_v(name):
    variables = v_dict()
    return variables.get(name, None)


def set_v(name, value):
    variables = v_dict()
    variables[name] = value
    with open("variables.toml", "w") as f:
        toml.dump(variables, f)

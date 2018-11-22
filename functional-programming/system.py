#!/usr/bin/env python
# -*- coding: utf-8 -*-

# exception io socket
try:
    # 主代码 执行
    raise Exception('')
except Exception as e:
    # 捕获异常时 执行
    print e
else:
    # 主代码 执行完 无异常 才执行
    pass
finally:
    # 不论异常与否 都执行
    pass
# -*- coding: UTF-8 -*-
import logging  # 引入logging模块
import time
import traceback
import asyncio

import requests

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# log_path = os.path.dirname(os.getcwd()) + '/logs/'
log_path = "/home/jake/workspace/python-learning/crontab/logs/"
log_name = log_path + 'open-api-test.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)


# 日志
def call_api():
    try:
        url = "https://logger.nexusguard.app/logger_api/data/get_site_list?token=30f6c652f2635d38d986e1f1284d8fab&size=1"
        response = requests.get(url)
        logger.info(response.content)
    except Exception as e:
        e_msg = traceback.format_exc()
        logger.error(e_msg)



for i in range(5):
    loop.run_until_complete(call_api())

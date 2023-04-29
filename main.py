import asyncio
import logging.config
import os
import traceback

import uvicorn

from env_config import *


async def run_fastapi(host, port):
    uvconfig = uvicorn.Config(
        app='fastapi_routers:app',
        host=host,
        port=port,
        reload=False,
        loop='asyncio',
        log_config="fastapi_log.ini"
    )
    uvserver = uvicorn.Server(uvconfig)
    await uvserver.serve()


async def main():
    setup_logging()
    logger = logging.getLogger()

    try:
        pid = os.getpid()
        logger.info(f"主进程启动, pid = {pid}")

        if testing := is_testing_env():
            logger.info("当前环境: 测试环境")
        else:
            logger.info("当前环境: 生产环境")

        host = "0.0.0.0"
        if testing:
            port = config["test_port"]
        else:
            port = config['port']

        logger.info("启动Fastapi")
        logger.info(f"首页地址: http://{host}:{port}")

        task_fastapi_server = asyncio.create_task(run_fastapi(host, port))
        # task_check_latency = asyncio.create_task(check_latency())

        await task_fastapi_server
        # await task_check_latency

        logger.info("全部任务结束")

    except SystemExit:
        logger.info("开始退出主进程")
    except KeyboardInterrupt:
        logger.info("^C中断进程")
    except Exception:
        logger.error(traceback.format_exc())
    finally:
        logger.info(f"主进程结束")


if __name__ == "__main__":
    asyncio.run(main())

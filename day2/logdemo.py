import logging 

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    filemode='w',
    format="python-app: %(process)d %(name)s-%(levelname)s-%(message)s-%(asctime)s"
)

logging.debug("Debug error occurred in code")
logging.info("Info: Admin logged in")
logging.warning("Warning: Less hard disk space")
logging.error("Error: Apps stopped")
logging.critical("Critical: App crashed")

username = "somesh"
logging.info(f"{username} has logged in")  # Fixed log message wording

try:
    a = 10
    b = 0
    c = a / b
except Exception as ex:
    logging.error("Exception occurred", exc_info=True)  # Fixed `exec_info=true` to `exc_info=True`
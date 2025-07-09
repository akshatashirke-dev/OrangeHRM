import logging

class log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename='.\\logs\\OrangeHRM_logs', format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',force=True)
        logger= logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
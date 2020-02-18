import logging

def setup_custom_logger(name, profile_id):
    
    formatstr = '%(asctime)s | %(message)s'
    fh = logging.FileHandler("/tmp/face-recognition/%s.log" % profile_id, mode='w', encoding=None, delay=False)
    formatter = logging.Formatter(formatstr)
    fh.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(fh)

    return logger
    
    
    
    
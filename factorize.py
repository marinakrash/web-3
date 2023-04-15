from multiprocessing import Pool, current_process
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def factorize(*number):
    results=[]
    for i in number:
        logger.debug(f"pid={current_process().pid}, i={i}")
        result = []
        for n in list(range(1, i+1)):
            num=i % n
            if num == 0:
                result.append(n)
        results.append(result)
    return (results)

if __name__ == '__main__':
    number = (128, 255, 99999, 10651060)
    with Pool(processes=2) as pool:
        logger.debug(pool.map(factorize, number))

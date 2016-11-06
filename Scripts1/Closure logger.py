from functools import wraps


def logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info('Running "{}" with the arguments {}, {}'.format(orig_func.__name__,args, kwargs) )
        print('logger executed')
        return(orig_func(*args, **kwargs))
    return wrapper

def timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig_func(*args,**kwargs)
        t2 = time.time() - t1
        print('Time taken for function {} to execute is {} '.format(orig_func.__name__, t2))
        print('timer executed')
        return result
    return wrapper


import time

@timer
@logger
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name,age))


display_info('Rakesh', 31)
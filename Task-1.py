import time


def time_check(function,call_count= 3,start_sleep_time= 1,factor= 2,border_cleep_time=60):
    call_count = call_count
    call_count_break = 0
    start_sleep_time = start_sleep_time
    factor = factor
    border_sleep_time = border_cleep_time
    t = start_sleep_time
    def sleep_time(*args,**kwargs):
        nonlocal start_sleep_time
        nonlocal call_count
        nonlocal t
        nonlocal factor
        nonlocal border_sleep_time
        nonlocal call_count_break
        result = function(*args, **kwargs)
        if t < border_sleep_time:
            t *= factor
            timer = time.sleep(t)
        if t >= border_sleep_time:
            t = border_sleep_time
            timer = time.sleep(border_sleep_time)
        call_count_break += 1
        print(f"Кол-во запусков = {call_count_break}\nНачало работы\nЗапуск номер {call_count_break}. Ожидание: {t} секунд. Результат декорируемой функций = {result}")
        while call_count_break != call_count:
            sleep_time(function.__call__(*args))
    return sleep_time

@time_check
def list_append(args: int):
    return args**2

print(list_append(5))

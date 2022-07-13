import time


def time_check(function,call_count= 0,start_sleep_time= 1,factor= 2,border_cleep_time=60):
    call_count = call_count
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
        result = function(*args, **kwargs)
        if function:
            call_count += 1
            if t < border_sleep_time:
                t = start_sleep_time*factor**t
                timer = time.sleep(t)
            if t >= border_sleep_time:
                t = border_sleep_time
                timer = time.sleep(border_sleep_time)
        return f"Кол-во запусков = {call_count}\nНачало работы\nЗапуск номер {call_count}. Ожидание: {t} секунд. Результат декорируемой функций = {result}"
    return sleep_time


@time_check
def list_append(args: int):
    return args**2


print(list_append(22))
print(list_append(8))
print(list_append(7))

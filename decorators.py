def decorator(func):
    def decorated(w,h):
        if w >= 0 and h >= 0:
            return func(w,h)
        else:
            raise ValueError('정수 내놔 임마!')


    return decorated
@decorator
def spah(w,h):
    return w * h


def User(func):
    # is_authenticated 0은 거짓 1은 참
    is_authenticated = 1
    def decorated(w,h):
        if is_authenticated == 1:
            return print(func(w,h))
        else:
            raise ValueError ('인증 필요')
    return decorated

@User
def nemo(w,h):
    return w*h

nemo(5,5)
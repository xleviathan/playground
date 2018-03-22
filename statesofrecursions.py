import time
print(time.time())
def when():
    minutes = time.time()//60
    hours  = minutes // 60
    days = hours // 24
    print('it took about ',days,'days',hours%24,'hours',minutes%60,'minutes  and ',minutes%60,'seconds')
when()
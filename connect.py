import redis

r: redis.Redis
log_number = 0


def init_connection(host, port):
    global r, log_number
    r = redis.Redis(host=host, port=port)
    try:
        last_key = max(map(lambda x: int(x.decode('UTF-8')[3:]), r.keys("log*")))
        log_number = last_key + 1
        print(f"Last key: {last_key}")
    except:
        print("There are no logs in database")


def add_log(time, url, ip):
    global log_number
    r.hset(name=f"log{log_number}", key="time", value=time)
    r.hset(name=f"log{log_number}", key="url", value=url)
    r.hset(name=f"log{log_number}", key="ip", value=ip)

    log_number += 1


def get_logs():
    log_keys = map(lambda key: key.decode('UTF-8'), r.keys('log*'))
    logs = list()
    for key in log_keys:
        row = r.hgetall(key)
        log_utf = {
            "log_key": key,
            "time": row[b'time'].decode('UTF-8'),
            "url": row[b'url'].decode('UTF-8'),
            "ip": row[b'ip'].decode('UTF-8')
        }
        logs.append(log_utf)
        logs.sort(key=lambda x: int(x['log_key'][3:]))
    return logs


def clear_base():
    keys = r.keys("log*")
    for key in keys:
        r.delete(key)

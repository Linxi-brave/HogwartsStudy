import datetime

def timeN(n):
    time = datetime.datetime.now() + datetime.timedelta(days=int(n))
    timeN = time.strftime("%Y-%m-%d %H:%M:%S")
    return timeN


def timenow():

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return str(time)

def timeday():

    time = datetime.datetime.now().strftime("%Y-%m-%d")

    return str(time)



import time
import datetime
class mytime(object):
    #返回一个比当前时间➕6天的时间戳
    def time(self):

        second = int(time.time())

        second = second + 6 * 86400

        return second

    #返回一个yy--mm--dd 格式的时间RR
    def datetime(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        return date


    def timeN(n):
        time = datetime.datetime.now() + datetime.timedelta(days=int(n))
        timeN = time.strftime("%Y-%m-%d %H:%M:%S")
        return timeN
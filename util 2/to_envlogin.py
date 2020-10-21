from util.get_tklogintoken import Teamkitlogintoken
from util.get_logincode import qrcode
from log.user_log import UserLog
class envlogin(object):
    def __init__(self,driver):
        log = UserLog()
        logger = log.get_log()
        self.driver = driver
        Teamkitlogin = Teamkitlogintoken()
        Teamkitlogin.url = "https://dnapp.bitkinetic.com/api/v5/login/mplogin"
        Teamkitlogin.body = {
            "zoneNum": "86",
            "phone": "15088132074",
            "password": "123456"
        }
        self.tks = Teamkitlogin.getMerloginHeader()
        logger.info("11111111111")
        logger.info(self.tks)
        print(self.tks)


    def tologin(self):
        header = self.tks[1]
        qrcodelogin = qrcode(self.driver)
        qrcodeloginurl = "https://dnapp.bitkinetic.com/api/v5/user/qrcodelogin"
        qrcodelogin.toqrcodelogin(qrcodeloginurl,header)
        print("22222")


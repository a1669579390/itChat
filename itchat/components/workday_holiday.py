import datetime

# 判断 2018年4月30号 是不是节假日
from chinese_calendar import is_workday, is_holiday
# 或者在判断的同时，获取节日名
import chinese_calendar as calendar  # 也可以这样 import
# 还能判断法定节假日是不是调休
import chinese_calendar


class Date():
    def is_workday(self,date):
        #当前日期是否为工作日
        self.assertFalse(is_workday(april_last))

    def is_holiday(self,date):
        #当前日期是否为周六日
        self.assertTrue(is_holiday(april_last))

    def is_in_lieu(self,date):
        #当前日期是否为调休
        self.assertFalse(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 1)))

    def is_remind(self,date):
        # 当前日期是否发送提醒消息

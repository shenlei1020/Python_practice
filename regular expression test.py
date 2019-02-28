# coding=utf-8
import re

line = "XXX出生于2001年6月1日"
line = "XXX出生于2001-6-1"
line = "XXX出生于2001_6_1"
line = "XXX出生于2001_06_01"
line = "XXX出生于2001-06-01"
# line = "XXX出生于2001/6/1"
# line = "XXX出生于2001/06/01"
# line = "XXX出生于2001年6月"

regex_str = ".*生于?(\d{4}[-_年/]\d{1,2}[-_月/]($|\d{1,2}$|\d{1}日$))"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group)
    print(match_obj.group(0))
    print(match_obj.group(1))

else:
    print('wrong!')
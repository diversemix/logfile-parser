"""
8;"2014-11-10 16:21:08.405125+00";"2014-11-10 16:21:23.23541+00";"Yes|I love it!";FALSE;0;4
9;"2014-11-10 16:21:30.683417+00";"2014-11-10 16:21:44.561077+00";"No|It's horrible!";FALSE;1;4

"""
import os
import sys
from datetime import datetime

DT = '2014-11-10 '

def dt(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

START = dt("2014-11-10 16:21:08")
END = dt("2014-11-10 16:21:44")

if __name__ == '__main__':
    
    log_list = os.listdir(os.getcwd())

    for log in log_list:
        if '.log' not in log:
            continue
        log_name = os.path.join(os.getcwd(), log)
        with open(log_name) as log_file:
            lines = log_file.readlines()
            for line in lines[1:]:
                bits = line.split(' ')
                if len(bits) > 4 and bits[0] == 'Nov' and bits[1] == '10': 

                    value = bits[2]
                    time_entry = datetime.strptime(DT + value, "%Y-%m-%d %H:%M:%S")
                    if time_entry >= START and time_entry <= END:
                        print line


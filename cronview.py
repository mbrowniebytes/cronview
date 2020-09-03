#!/usr/bin/env python
# -*- coding: utf-8 -*-
import croniter
import datetime
import sys

DATEFORMAT = "%d.%m.%Y %H:%M" # See http://strftime.org

def main(args):
    now = datetime.datetime.now()
    cronlist = []
    try:
        for line in sys.stdin:
            li=line.strip()
            if li == '':
                continue
            if li.startswith('SHELL') or li.startswith('PATH') or li.startswith('MAILTO'):    
                continue
            if li.startswith("#"):
                continue
            mycron = line.rstrip()
            mycronlist = mycron.split()
            mycrondate = ' '.join(mycronlist[0:5])
            cron = croniter.croniter(mycrondate, now)
            for i in range(0,int(sys.argv[1])): # get each cronjob n times, not optimal
                x = cron.get_next(datetime.datetime).strftime(DATEFORMAT)
                y = str(' '.join(mycronlist[5::]))
                cronlist.append((x, y)) # list of tuples

        cronlist_sorted = sorted(cronlist, key=lambda x: datetime.datetime.strptime(x[0], DATEFORMAT))
        for i in cronlist_sorted[:int(sys.argv[1])]:
            print(i[0] + ' - ' + i[1])
    except IndexError:
        print("You need to specify how many occurrences, ie. crontab -l | python view.py 4")


if __name__ == '__main__':
    sys.exit(main(sys.argv))

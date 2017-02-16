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
            if not li.startswith("#"):
                mycron = line.rstrip()
                mycronlist = mycron.split()
                mycrondate = ' '.join(mycronlist[0:5])
                cron = croniter.croniter(mycrondate, now)
                for i in range(0,int(sys.argv[1])):
                    t = cron.get_next(datetime.datetime).strftime(DATEFORMAT)
                    cronlist.append(str(t) + ' - ' +  str(' '.join(mycronlist[5::])))

        cronsorted = sorted(cronlist)
        for i in cronsorted[:int(sys.argv[1])]:
            print i
    except IndexError:
        print("You need to specify how many occurences, ie. crontab -l | python view.py 4")


if __name__ == '__main__':
    sys.exit(main(sys.argv))

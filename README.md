# cronview
Reading crontab -l can be cumbersome and I needed a nicer formatted view of the next cron jobs. cronview takes the output from crontab -l and prints a list of desired length.  

![](cronview.png "cronview")

## Requirements

the script uses `croniter`, which you can install with pip

```bash
pip install croniter
```

## Usage
In linux, crontab -l prints the cron jobs for your user. Simply pipe the content from crontab -l into the script and specify how many occurences, ie.

```bash
crontab -l | python view.py 4
```
means four jobs.
You can also show the cron agenda for a different user like this:

```bash
crontab -u username -l | python view.py 3
```

onlog.py: log when a computer is on
===================================

This is a Python script to log when a computer is on.

Execute it, and it produces a sqlite database with two tables, "up" and "down".
One records times at which the computer came up, the other times at which it
went down.

This script is intended to be invoked on system startup.

Details
-------

Ideally one could simply record all "on" and "off" events at the time they
occurred, including boot, reboot, suspend, hibernate, etc. However, this is
very system-dependent and always non-exhaustive (for example, sudden loss of
power is never recorded).

The simpler solution employed here is to log at intervals the fact that the
computer is up. To avoid growing the log at every interval, this script always
replaces the last recorded "up" time with a new one, if the last one was
recent enough to assume that no intermittent downtime occurred.

If these updates were done through simple file I/O, a sudden power off during
an update could cause the loss of uptime information for the last up period.
For this reason, logging is done transactionally with sqlite.

Consequently, this will cause periodic disk I/O.


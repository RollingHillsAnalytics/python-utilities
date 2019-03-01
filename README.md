# python-utilities
Set of various Python utilities to be used in other scripts and projects.


displayduration

This module can be used to display a nicely formatted message showing the elapsed time between two events.
A common use is to display the execution time of a program or process.

For example:
'''
from timeit import default_timer as timer
from displayduration import DisplayDuration

starttime = timer()
...
<some processing>
...
endtime = timer()

DisplayDuration(starttime, endtime)
'''



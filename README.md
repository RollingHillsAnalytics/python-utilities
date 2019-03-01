# python_utilities
Set of various Python utilities to be used in scripts and projects.


## DisplayDuration

This module can be used to display a nicely formatted message showing the elapsed time between two events.
A common use is to display the execution time of a program or process.

For example:
```python
from timeit import default_timer as Timer
from python_utilities import DisplayDuration as Duration

starttime = Timer()
...
<some processing>
...
endtime = Timer()

Duration(starttime, endtime)
```



import sys
sys.path.append("controllers")

"""
To allow our website to see our different controllers, we must import them using
this views.py file. The syntax is as follows:

from A import B

where A is a Python file in the /controllers folder (without the .py!) and B is
the name of the function that runs that particular route.

"""

from index import index
from question import question
from answer import answer
from confirm import confirm

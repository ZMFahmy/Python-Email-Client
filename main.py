import sys
from frontend.gui import GUI

arguments = sys.argv[1:]
email = arguments[0]
password = arguments[1] + ' ' + arguments[2] + ' ' + arguments[3] + ' ' + arguments[4]
gui = GUI(email, password)

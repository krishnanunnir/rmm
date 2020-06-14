from properties import *
import subprocess

logging_location = log_location + log_name
subprocess.call(['mkdir','-p',log_location])
subprocess.call(['mkdir','-p',screenshot_location])
subprocess.call(['touch',logging_location])
subprocess.call(['pip','install','-r','../requirements.txt'])
import argparse

parser = argparse.ArgumentParser(description="Start and control water monitor system")

parser.add_argument('-d', '--debug', type=int, choices=[0,1,2],
 help="0 - no debug (default), 1 - print activity, 2 - print sensor events and activity",
 default=0)

args = parser.parse_args()

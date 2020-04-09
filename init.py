"""App initialization"""
import argparse
import sys
from core import main

def _define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', help='The job to run (default: 1, 2)')
    return parser

def _get_job(parser):
    args = parser.parse_args()
    print(args.job)
    if not args.job:
        return 1
    elif args.job in ["1", "2"]:
        return int(args.job)
    else:
        print("fuck")
        sys.exit(-1)

PARSER = _define_args()
JOB = _get_job(PARSER)

main.Main(JOB)

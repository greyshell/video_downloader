#!/usr/bin/env python3

# author: greyshell

import sys
from lib.parse_args import get_args
from lib.talk_python import TalkPython
from lib.packtpub import PacktPub

if __name__ == '__main__':
    args = get_args()
    course = None

    if len(sys.argv) == 1:
        args.print_help(sys.stderr)
        sys.exit(1)

    if args.cmd == 'talk_python':
        course = TalkPython(args.download_location, args.module_name)

    elif args.cmd == 'packtpub':
        pass  # TODO: implement that class

    else:
        args.print_help(sys.stderr)
        sys.exit(1)

    course.process()


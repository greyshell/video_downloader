# !/usr/bin/env python3

# author: greyshell

import argparse


def get_args():
    # create the top-level parser
    parser = argparse.ArgumentParser(
        description='download videos'
    )

    parser.add_argument(
        '-d',
        '--download_location',
        help='provide the download location',
        required=True,
    )

    subparsers = parser.add_subparsers(
        title='courses',
        help='see [course] --help for more details',
    )

    # create a course
    course_name = 'talk_python'
    course = subparsers.add_parser(f'{course_name}')
    # add arguments
    course.add_argument(
        '-m',
        '--module_name',
        help='provide the module name',
        required=True,
    )

    course.set_defaults(
        cmd=f'{course_name}',
    )

    # create an another course with different required arguments
    # TODO: packtpub

    return parser.parse_args()

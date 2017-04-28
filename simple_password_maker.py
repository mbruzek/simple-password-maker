#!/usr/bin/env python3

"""
simple-password-maker the command line wrapper for the SimplePasswordMaker lib.

Copyright 2016 Matthew Bruzek

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import argparse
import sys
import traceback

from lib.SimplePasswordMaker import SimplePasswordMaker


HASH = 'Hash algorithm md5/sha1/sha224/sha256/sha384/sha512'
MASTER_PASS = 'Master password'
URL = 'URL'
USERNAME = 'Username'
MODIFIER = 'Modifier'
LENGTH = 'Password length'
CHARSET = 'Characters to use'
DEFAULT_CHARSET = SimplePasswordMaker.CHARSET


def command_line():
    """The function to parse the arguments from the command line."""
    description = "Make passwords based on user input."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-a', '--algorithm',
                        help='{0} [{1}]'.format(HASH, 'sha256'))
    parser.add_argument('-m', '--master', default='',
                        help='{0} [{1}]'.format(MASTER_PASS, None))
    parser.add_argument('-r', '--url', default='',
                        help='{0} [{1}]'.format(URL, None))
    parser.add_argument('-u', '--user', default='',
                        help='{0} [{1}]'.format(USERNAME, None))
    parser.add_argument('-d', '--modifier', default='',
                        help='{0} [{1}]'.format(MODIFIER, None))
    parser.add_argument('-g', '--length', default='16',
                        help='{0} [{1}]'.format(LENGTH, '16'))
    printable_charset = DEFAULT_CHARSET.replace('%', '%%')
    parser.add_argument('-c', '--charset', default=DEFAULT_CHARSET,
                        help='{0} [{1}]'.format(CHARSET, printable_charset))
    arguments = parser.parse_args()



    try:
        maker = SimplePasswordMaker()
        print(maker.generate_password(
                arguments.algorithm,
                arguments.master,
                arguments.url + arguments.user + arguments.modifier,
                arguments.length,
                arguments.charset))

    except:
        traceback.print_exc()
        exit(1)


def interactive():
    """The function to interactivly prompt the user the possible values."""
    options = {}
    try:
        options['algorithm'] = prompt(HASH, 'sha256')
        options['master'] = prompt(MASTER_PASS)
        options['url'] = prompt(URL)
        options['username'] = prompt(USERNAME)
        options['modifier'] = prompt(MODIFIER)
        options['length'] = prompt(LENGTH, '16')
        options['charset'] = prompt(CHARSET, DEFAULT_CHARSET)

        maker = SimplePasswordMaker()
        print(maker.generate_password(
                options['algorithm'],
                options['master'],
                options['url'] + options['username'] + options['modifier'],
                options['length'],
                options['charset']))
    except (KeyboardInterrupt, SystemExit):
        print("\n\nUser has quit, exiting the program.")
        exit(2)
    except:
        traceback.print_exc()
        exit(1)


def prompt(message, default=None):
    """A method to prompt the user for a value, with an optional default."""
    if default:
        return input('{0} [{1}]: '.format(message, default)) or default
    else:
        return input('{0}: '.format(message))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        command_line()
    else:
        interactive()

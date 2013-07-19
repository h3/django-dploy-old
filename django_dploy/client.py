#!/usr/bin/env python

import imp
import logging
import os
import os.path
import sys

from optparse import OptionParser

from django_dploy import VERSION
from django_dploy.core import Dploy

#from django_dploy.commands import send_command, get_command_options

"""
Example usage:

$ dploy on prod
$ dploy rollback on prod 5ed9fc756a67462c8e537894208caf5
$ dploy django:syncdb on beta,prod
$ dploy restart-web-server on prod
$ dploy django:"collectstatic -lqy" on beta,prod
"""

def main():
    parser = OptionParser(version="%%prog %s" % VERSION)
    cmd  = sys.argv[1]

   #for opts in get_command_options(cmd):
   #    if isinstance(opts[1], dict): # ex: -h
   #       parser.add_option(opts[0], **opts[1])
   #    else: # ex: -h, --help
   #       parser.add_option(opts[0], opts[1], **opts[2])

    (options, args) = parser.parse_args()

    return Dploy(options).run()
#   command_list = (
#       'init',
#       'help',
#   )


#   if len(sys.argv) < 2\
#       or sys.argv[1] not in command_list\
#       or sys.argv[1] == 'help':
#       print "usage: dploy [command] [options]\n"
#       print "Available subcommands:"
#       for cmd in command_list:
#           print " ", cmd
#       if len(sys.argv) >= 2 and sys.argv[1] == 'help':
#           print ""
#       else:
#           sys.exit(1)





#   if getattr(options, 'debug', False):
#       django_settings.DEBUG = True

#   send_command(cmd, *args[1:], **options.__dict__)

    sys.exit(0)

if __name__ == '__main__': # pragma: no cover
    main()

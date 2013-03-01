import os, sys

from django_dploy.commands import BaseCommand
from django_dploy.utils import color as c


class HelpCommand(BaseCommand):
    """
    Show duke help.
    """

    options = []

    def call(self, *args, **options):
        self.base_path = 'base_path' in options and options['base_path'] or os.getcwd()

       #print "[%s]" % c("Available environment shortcuts", "bold_green")
       #shortcuts = ['buildout', 'dbshell', 'dev', 'dumpdata', 'loaddata',\
       #             'python', 'runserver', 'shell', 'syncdb']
       #print "".join(['  %s\n' % x for x in shortcuts])

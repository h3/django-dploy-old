import os, sys

from django_dploy.commands import BaseCommand
from django_dploy.utils import color as c


class InitCommand(BaseCommand):
    """
    Init dploy
    """

    options = []

    def call(self, *args, **options):
        self.base_path = 'base_path' in options and options['base_path'] or os.getcwd()
        self.dploy_path = os.path.join(self.base_path, 'dploy')
        self.dploy_conf = os.path.join(self.dploy_path, 'conf.yml')

        if os.path.exists(self.dploy_conf):
            print "Error: dploy already initialized for this project"
        else:
            print "mkdir -p dploy"
            print "touch dploy/conf.yml"

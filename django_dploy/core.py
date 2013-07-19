import os
import sys
import yaml
import subprocess
import IPython


class Dploy(object):

    def __init__(self, options):
        self.options = options
        self.argv = sys.argv
        self.cwd = os.getcwd()
        self.dploy_path = os.path.join(self.cwd, '.dploy')
        self.load_specs()
        self.parse_arguments()

        for stage in self.stages:
            self.call(self.command, stage)

    def parse_arguments(self):
        print "argv: %s" % ', '.join(['%s:%s' % (k,a) for k,a in enumerate(self.argv)])

        if len(self.argv) < 2:
            print "Error: not enough arguments"
            # TODO: print help
            sys.exit(1)

        self.command = self.argv[1]

        # Determine the command to execute
        if self.argv[1] == 'on':
            self.stages = self.argv[2].split(',')
            self.command = 'deploy'
        elif 'on' not in self.argv:
            self.stages = ['dev']
        elif self.argv[2] == 'on':
            self.stages = self.argv[3].split(',')

    def load_specs(self):
        """
        Populates self.config, self.events, self.commands
                  self.config_path, self.events_path, self.commands_path
        """
        for spec in ['config', 'events', 'commands']:
            p = os.path.join(self.dploy_path, '%s.yml' % spec)
            setattr(self, '%s_path' % spec, p)
            stream = file(p, 'r')
            setattr(self, spec, yaml.load(stream))

    def call(self, command, stage):
        print 'Executing task: %s on stage "%s"' % (command, stage)
        if not self.commands.get(stage):
            print "Error: stage not found"
            sys.exit(1)
        else:
            commands = self.commands.get(stage)
            if commands.get(command):
                for cmd in commands.get(command):
                    if stage == 'dev':
                        rc = subprocess.call(cmd, shell=True)
                    else:
                        # TODO: Fabric
                        rc = 1
            else:
                print "Error: unknown command"

    def run(self):
        sys.exit(0)

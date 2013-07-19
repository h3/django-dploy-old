import os
import sys
import yaml


class Dploy(object):

    def __init__(self, options):
        self.options = options
        self.argv = sys.argv
        self.cwd = os.getcwd()
        self.dploy_path = os.path.join(self.cwd, '.dploy')

        self.load_specs()

       #if len(self.argv) in [3, 4]:
            # dploy on <stage>
        print self.argv

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

    def run(self):
        # TODO: exec command...
        sys.exit(0)

import argparse
import dotmap
import logging
import yaml

from . import colour as c
from . import exceptions
from . import logger
from . import configuration

log = logger.setupLog('root')


"""
    Simple Console Application with Logging, YAML Configuration and Argparse
"""
class Scalyca():
    app_name = 'Scalyca'

    def __init__(self, *, description=''):
        self.description = description
        self.ok = True

    def initialize(self):
        self.create_argparser()
        self.args = self.argparser.parse_args()
        self.ok = False
        log.info(f"{c.script(self.app_name)} initializing...")

        try:
            self.load_config()
            self.override_config()
            configuration.make_static(self.config)
            self.debug_config()

        except exceptions.FatalError:
            log.critical(f"{c.script(self.app_name)} aborting during configuration")
            sys.exit(-1)

    def create_argparser(self, *, description=None):
        self.argparser = argparse.ArgumentParser(description)
        self.argparser.add_argument('config', type=argparse.FileType('r'), help="Main configuration file")
        self.argparser.add_argument('-l', '--logfile', type=argparse.FileType('w'), help="Write log to file")
        self.argparser.add_argument('-d', '--debug', action='store_true', help="Turn on verbose logging")

    def load_config(self):
        self.config = configuration.load_YAML(self.args.config)

    def override_config(self):
        log.setLevel(logging.DEBUG if self.args.debug else logging.INFO)

        if self.args.debug:
            log.warning(f"Debug output is {c.over('active')}")

        if self.args.logfile:
            log.addHandler(logging.FileHandler(self.args.logfile.name))
            log.warning(f"Added log output {c.over(self.args.logfile.name)}")

    def debug_config(self):
        log.debug("Full config is")
        if self.args.debug:
            self.config.pprint()

    def main(self):
        pass

    def run(self):
        try:
            self.initialize()
            self.main()
            self.finalize()
        except exceptions.PrerequisiteError as e:
            log.error(f"Terminating due to missing prerequisites")
        except exceptions.ConfigurationError as e:
            log.error(f"Terminating due to a configuration error: {e}")
        finally:
            if self.ok:
                log.info(f"{c.script(self.app_name)} finished successfully")
            else:
                log.critical(f"{c.script(self.app_name)} aborted during runtime")

    def override_warning(self, parameter, old, new):
        log.warning(f"Overriding {c.param(parameter)} ({c.over(old)} -> {c.over(new)})")

    def finalize(self):
        self.ok = True

    def load_configuration(self):
        self.raw_config = dotmap.DotMap(yaml.safe_load(self.args.config), _dynamic=True)

    def override_configuration(self):
        log.setLevel(logging.DEBUG if self.args.debug else logging.INFO)

        if self.args.debug:
            log.warning(f"Debug output is {c.over('active')}")

    def configure(self):
        pass

    def override_warning(self, parameter, old, new):
        log.warning(f"Overriding {c.param(parameter)} ({c.over(old)} -> {c.over(new)})")


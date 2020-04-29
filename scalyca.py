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
    Scala: Simple Console Application with Logging and Argparse
"""
class Scala():
    app_name = 'Scala'
    description = "Simple Configurable Application with Logging and Argparse"

    def __init__(self):
        self.ok = True

    def initialize(self):
        self.create_argparser()
        self.add_default_arguments()
        self.add_arguments()

        self.args = self.argparser.parse_args()
        self.ok = False

    def create_argparser(self):
        self.argparser = argparse.ArgumentParser(self.description)

    def add_default_arguments(self):
        self.argparser.add_argument('-l', '--logfile', type=argparse.FileType('w'), help="Write log to file")
        self.argparser.add_argument('-d', '--debug', action='store_true', help="Turn on verbose logging")

    def add_arguments(self):
        pass

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
            if not self.ok:
                log.critical(f"{c.script(self.app_name)} aborted during runtime")

    def override_warning(self, parameter, old, new):
        log.warning(f"Overriding {c.param(parameter)} ({c.over(old)} -> {c.over(new)})")

    def finalize(self):
        self.ok = True

    def override_configuration(self):
        log.setLevel(logging.DEBUG if self.args.debug else logging.INFO)

        if self.args.debug:
            log.warning(f"Debug output is {c.over('active')}")

    def override_warning(self, parameter, old, new):
        log.warning(f"Overriding {c.param(parameter)} ({c.over(old)} -> {c.over(new)})")


"""
    Simple Console Application with Logging, YAML Configuration and Argparse
"""
class Scalyca(Scala):
    app_name = 'Scalyca'
    description = "Simple Configurable Application with Logging, YAML Configuration and Argparse"

    def add_default_arguments(self):
        self.argparser.add_argument('config', type=argparse.FileType('r'), help="main configuration file")
        super().add_default_arguments()

    def initialize(self):
        super().initialize()
        try:
            self.load_config()
            self.override_config()
            self.lock_config()
            self.debug_config()

        except exceptions.FatalError:
            log.critical(f"{c.script(self.app_name)} aborting during configuration")
            sys.exit(-1)

    def load_config(self):
        raw = configuration.load_YAML(self.args.config)
        self.config = dotmap.DotMap(raw, _dynamic=True)

    def override_config(self):
        log.setLevel(logging.DEBUG if self.args.debug else logging.INFO)

        if self.args.debug:
            log.warning(f"Debug output is {c.over('active')}")

        if self.args.logfile:
            log.addHandler(logging.FileHandler(self.args.logfile.name))
            log.warning(f"Added log output {c.over(self.args.logfile.name)}")

    def lock_config(self):
        configuration.make_static(self.config)

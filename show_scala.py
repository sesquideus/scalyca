#!/usr/bin/env python

import argparse
import logging
from scalyca import Scala
from scalyca import colour as c


log = logging.getLogger("root")


class ScalaShowcase(Scala):
    _app_name = "SCALA showcase"
    _description = "A very simple SCALA showcase"
    _success_message = "Cat management finished successfully"

    def add_arguments(self):
        self.add_argument('string', type=str, choices=['foo', 'bar', 'baz'])
        self.add_argument('number', type=int)
        self.add_argument('file', type=argparse.FileType('r'))
        self.add_argument('--hungry', action='store_true')

    def main(self):
        log.info(f"{c.script(self._app_name)} running: cat '{c.param(self.args.string)}' has {c.param(self.args.number)} kittens "
                 f"and is {'' if self.args.hungry else 'not '}hungry")
        self.purr(self.args.number)

    def purr(self, number):
        """ This emulates something that the actual program would be doing... """
        for i in range(0, number):
            print("Purr...", end=" " if i < number - 1 else "\n")

        if self.args.hungry:
            log.warning("The cat is hungry")


ScalaShowcase(success_message=f"Cat management complete. {c.act('Yay')}!").run()

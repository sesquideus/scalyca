#!/usr/bin/env python

import logging
from scalyca import Scala
from scalyca import colour as c


log = logging.getLogger("root")


class ScalaShowcase(Scala):
    app_name = "SCALA showcase"
    description = "SCALA showcase"

    def add_arguments(self):
        self.argparser.add_argument('string', type=str, choices=['foo', 'bar', 'baz'])
        self.argparser.add_argument('number', type=int)
        self.argparser.add_argument('--hungry', action='store_true')

    def main(self):
        log.info(f"SCALA showcase running: cat '{c.param(self.args.string)}' has {c.param(self.args.number)} kittens "
              f"and is {'' if self.args.hungry else 'not '}hungry")


ScalaShowcase().run()

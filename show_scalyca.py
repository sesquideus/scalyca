#!/usr/bin/env python

import time
import logging

from schema import Schema, Or

from scalyca import Scalyca
from scalyca import colour as c

log = logging.getLogger("root")


class ScalycaShowcase(Scalyca):
    _description = "A very simple SCALYCA showcase"
    _prog = "Scalyca showcase"
    _version = "1.0"
    _schema = Schema({
        'name': Or('foo', 'bar', 'baz', 'qux'),
        'kittens': int,
        'hungry': bool,
    })

    def add_arguments(self):
        self.add_argument('name', type=str, choices=['foo', 'bar', 'baz'])
        self.add_argument('kittens', type=int)
        self.add_argument('--hungry', action='store_true')

    def override_configuration(self):
        self.config.name = self.args.name
        self.config.kittens = self.args.kittens
        self.config.hungry = self.args.hungry

    def main(self):
        log.info(f"{self._prog} running: cat '{c.param(self.config.name)}' has {c.param(self.config.kittens)} kittens "
                 f"and is {'' if self.config.hungry else 'not '}hungry")
        self.purr(self.args.kittens)

    def purr(self, number):
        for i in range(0, number):
            print("Purr...", end=" " if i < number - 1 else "\n", flush=True)
            time.sleep(0.5)

        if self.args.hungry:
            log.warning("The cat is hungry")

        log.info("Cat management complete")


ScalycaShowcase().run()

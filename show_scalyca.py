#!/usr/bin/env python

import logging

from schema import Schema, Or

from scalyca import Scalyca
from scalyca import colour as c

log = logging.getLogger("root")


class ScalycaShowcase(Scalyca):
    _app_name = "Scalyca showcase"
    _description = "A very simple SCALYCA showcase"
    _prog = "Scalyca showcase"
    schema = Schema({
        'name': Or('foo', 'bar', 'baz', 'qux'),
        'kittens': int,
        'hungry': bool,
    })

    def add_arguments(self):
        self.add_argument('name', type=str, choices=['foo', 'bar', 'baz'])
        self.add_argument('kittens', type=int)
        self.add_argument('--hungry', action='store_true')

    def override_configuration(self):
        self.override_with_warning(self.config.name, self.args.name, 'name')
        self.override_with_warning(self.config.kittens, self.args.kittens, 'kittens')
        self.override_with_warning(self.config.hungry, self.args.hungry, 'hungry')

    def main(self):
        log.info(f"SCALYCA showcase running: cat '{c.param(self.config.name)}' has {c.param(self.config.kittens)} kittens "
                 f"and is {'' if self.config.hungry else 'not '}hungry")
        self.purr(self.args.kittens)

    def purr(self, number):
        for i in range(0, number):
            print("Purr... ", end="")
        print()

        if self.args.hungry:
            log.warning("The cat is hungry")

        log.info("Cat management complete")


ScalycaShowcase().run()

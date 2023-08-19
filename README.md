# SCALA
Simple Console Application with Logging and Argparse

This project is my attempt to provide a very simple common framework for console jobs. It provides

- logging, primarily for `stdout` during operation. This is implemented with the standard `logging` module.
- parsing command line arguments, which should somehow affect the initial state and configuration of the application.
  The tool for the job is `argparse`.

# SCALYCA
Simple Console Application with Logging, YAML Configuration and Argparse

This subclass of `SCALA` adds persistent configuration from a `YAML` file, using `yaml` and `dotmap`.

It is supposed to be very lightweight and easily integrable.

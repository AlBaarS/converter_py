#!/bin/python3
from src.orchestrator import Orchestrator

import sys

if __name__ == "__main__":
    input_args: str = " ".join(sys.argv[1:])
    return Orchestrator.convert(input_args)

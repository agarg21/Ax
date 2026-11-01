# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os

# pytest-xdist's controller imports a warning's module when it receives a
# warning from a worker, from one receiver thread per worker. Importing ax here,
# once, before the workers start keeps those threads from importing it
# concurrently (seen as an importlib _DeadlockError on Python 3.14).
import ax  # noqa: F401


def pytest_configure(config) -> None:
    # Under pytest-xdist each worker would otherwise start one torch thread per
    # CPU, so N workers run N*N threads and some tests hit TestCase's 120 s limit.
    if os.environ.get("PYTEST_XDIST_WORKER"):
        import torch

        torch.set_num_threads(1)

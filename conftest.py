# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pytest-xdist's controller imports a warning's module when it receives a
# warning from a worker, from one receiver thread per worker. Importing ax here,
# once, before the workers start keeps those threads from importing it
# concurrently (seen as an importlib _DeadlockError on Python 3.14).
import ax  # noqa: F401

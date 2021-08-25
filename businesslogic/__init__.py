from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import uuid


def generate_uuid(length: int = 10):
    uid: str = uuid.uuid4().hex
    return uid[0:length] if length is not None and isinstance(length, int) and (0 < length < 40) else uid

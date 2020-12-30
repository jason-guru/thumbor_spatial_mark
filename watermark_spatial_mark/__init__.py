#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.1.0'

try:
    from watermark_spatial_mark.spatial_mark import Filter  # NOQA
except ImportError:
    logging.exception('Could not import spatial_mark. Probably due to setup.py installing it.')
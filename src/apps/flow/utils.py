# -*- coding: utf-8 -*-

import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
transition_filename = os.path.join(current_directory, 'transitions.json')

with open(transition_filename) as f:
    TRANSITIONS = json.loads(f.read())

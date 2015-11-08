#!/usr/bin/env python
# -*- coding: utf-8 -*-

crontable = []
outputs = []


def process_message(data):
    if data['channel'] == 'C0CMFHF7Z' \
            and "text" in data \
            and data['text'].startswith("Warchief"):

        action = data['text'].replace("Warchief, ", "")
        reply = "Roger that! Orcs, let's %s!" % action

        outputs.append([data['channel'], reply])

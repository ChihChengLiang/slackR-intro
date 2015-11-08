#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
crontable = []
outputs = []


def process_message(data):
    print(sys.version)
    print(data)
    if data['channel'] == 'C0CMFHF7Z' and "text" in data:
        if data['text'].startswith("Warchief"):
            reply = "Roger that! Orcs, let's {}!".format(
                data['text'].replace("Warchief, ", ""))
            print(reply)
            outputs.append([data['channel'], reply])

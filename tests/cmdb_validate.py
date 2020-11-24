# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
import jsonschema
import json

schema = {
          "type": "array",
          "title": "Host list",
          "format": "tabs",
          "items": {
              "$ref": "file:docs/host_ping.json",
          }
}

cmdb = open('docs/cmdb.json', 'r')
jsoncmdb = json.load(cmdb)

jsonschema.validate(jsoncmdb, schema)

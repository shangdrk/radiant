from django.contrib.auth.models import User
from django.core import serializers

from random import random
import json


def populate(username, user_value=5):
    result = {"nodes": [], "links": []}
    first_friends = []
    first_node = {"username": username, "value": user_value}

    return


def get_user_node(username, user_value):
    user_friends = [User.objects.get(username=username).personal.friends]
    user_node = {"username": username, "value": user_value}
    return


def feed():
    raw_data = {"nodes": [{
        "username": "Frank",
        "value": 2,
        "friends": ["b", "c"],
        "size": 15
    }, {
        "username": "Derek",
        "value": 5,
        "friends": ["a"],
        "size": 8
    }, {
        "username": "Yuhao",
        "value": 2,
        "friends": ["a", "d"],
        "size": 10
    }, {
        "username": "Zora",
        "value": 4,
        "friends": ["c", "e", "f", "g"],
        "size": 4
    },{ "username": "Jialun",
        "value": 3,
        "friends": ["c"],
        "size": 9
        }, { "username": "A",
             "value": 1,
             "friends": ["c"],
             "size": 12
             }, { "username": "B",
                  "value": 5,
                  "friends": ["D"],
                  "size": 4
                  }, { "username": "C",
                       "value": 5,
                       "friends": ["E"],
                       "size": 2
                       }, { "username": "D",
                            "value": 3,
                            "friends": ["D"],
                            "size": 10
                            },{ "username": "E",
                                "value": 4,
                                "friends": ["D"],
                                "size": 5
                                },{ "username": "F",
                                    "value": 2,
                                    "friends": ["D"],
                                    "size": 6
                                    },{ "username": "F",
                                        "value": 7,
                                        "friends": ["D"],
                                        "size": 7
                                        } ], "links": [{
        "source": 0,
        "target": 1
    }, {
        "source": 0,
        "target": 2
    }, {
        "source": 2,
        "target": 3
    }, {
        "source": 4,
        "target": 3
    },{
        "source": 5,
        "target": 0
    },{
        "source": 0,
        "target": 6
    },{
        "source": 7,
        "target": 8
    }]}
    json_data = json.dumps(raw_data)

    return json_data
import requests


class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    def send(self, uid, name, verbose=False):
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en",
            "connection": "keep-alive",
            "dnt": "1",
            "host": "iterborea-supsi.ch",
            "origin": self.base_url,
            "referer": f"{self.base_url}/iter/iterborea/{uid}",
            "sec-ch-ua": "'Google Chrome';v='111', 'Not(A:Brand';v='8', 'Chromium';v='111'",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
        }

        if verbose:
            print("Headers", headers)

        # Create session
        s = requests.Session()

        # Request 1 - Get session cookie
        response = s.get(
            f"{self.base_url}/iter/iterborea/{uid}", headers=headers)

        if verbose:
            print(response.status_code)
            print("Cookies", s.cookies)

        # Request 2 - Get csrf token
        response = s.get(
            f"{self.base_url}/iter/?v-r=init&location=iterborea%2F{uid}", headers=headers)

        if verbose:
            print(response.status_code)
            print(response.text)

        csrfToken = response.json()["appConfig"]["uidl"]["Vaadin-Security-Key"]

        if verbose:
            print("CSRF Token", csrfToken)

        # Request 3
        body = {
            "csrfToken": csrfToken,
            "rpc": [
                {
                    "type": "publishedEventHandler",
                    "node": 1,
                    "templateEventMethodName": "connectClient",
                    "templateEventMethodArgs": [
                            "flow-container-root-2521314",
                            "ROOT-2521314",
                            f"iterborea/{uid}",
                            "",
                            None
                    ],
                    "promise": 0
                }
            ],
            "syncId": 0,
            "clientId": 0
        }
        response = s.post(
            f"{self.base_url}/iter/?v-r=uidl&v-uiId=0", headers=headers, json=body)
        if verbose:
            print(response.status_code)
            print(response.text)

        # Request 4
        response = s.get(f"{self.base_url}/iter/", headers=headers)
        if verbose:
            print(response.status_code)
            print(response.text)

        # Requests 5-13
        steps = [
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "event",
                        "node": 48,
                        "event": "opened-changed",
                        "data": {}
                    }
                ],
                "syncId": 1,
                "clientId": 1
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "channel",
                        "node": 1,
                        "channel": 0,
                        "args": [
                            None
                        ]
                    },
                    {
                        "type": "channel",
                        "node": 1,
                        "channel": 2,
                        "args": [
                            None
                        ]
                    },
                    {
                        "type": "channel",
                        "node": 1,
                        "channel": 4,
                        "args": [
                            None
                        ]
                    }
                ],
                "syncId": 2,
                "clientId": 2
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "event",
                        "node": 48,
                        "event": "opened-changed",
                        "data": {}
                    }
                ],
                "syncId": 3,
                "clientId": 3
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "mSync",
                        "node": 38,
                        "feature": 1,
                        "property": "value",
                        "value": name
                    },
                    {
                        "type": "event",
                        "node": 38,
                        "event": "change",
                        "data": {}
                    },
                    {
                        "type": "event",
                        "node": 42,
                        "event": "click",
                        "data": {
                            "event.shiftKey": False,
                            "event.metaKey": False,
                            "event.detail": 1,
                            "event.ctrlKey": False,
                            "event.clientX": 305,
                            "event.clientY": 461,
                            "event.altKey": False,
                            "event.button": 0,
                            "event.screenY": 363,
                            "event.screenX": 305
                        }
                    }
                ],
                "syncId": 4,
                "clientId": 4
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "event",
                        "node": 48,
                        "event": "opened-changed",
                        "data": {}
                    }
                ],
                "syncId": 5,
                "clientId": 5
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "event",
                        "node": 15,
                        "event": "click",
                        "data": {
                            "event.shiftKey": False,
                            "event.metaKey": False,
                            "event.detail": 1,
                            "event.ctrlKey": False,
                            "event.clientX": 88,
                            "event.clientY": 576,
                            "event.altKey": False,
                            "event.button": 0,
                            "event.screenY": 663,
                            "event.screenX": 88
                        }
                    }
                ],
                "syncId": 6,
                "clientId": 6
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "event",
                        "node": 53,
                        "event": "opened-changed",
                        "data": {}
                    }
                ],
                "syncId": 7,
                "clientId": 7
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "channel",
                        "node": 1,
                        "channel": 6,
                        "args": [
                            "19445"
                        ]
                    },
                    {
                        "type": "channel",
                        "node": 1,
                        "channel": 8,
                        "args": [
                            "20"
                        ]
                    },
                    {
                        "type": "channel",
                        "node": 1,
                        "channel": 10,
                        "args": [
                            name
                        ]
                    }
                ],
                "syncId": 8,
                "clientId": 8
            },
            {
                "csrfToken": csrfToken,
                "rpc": [
                    {
                        "type": "mSync",
                        "node": 53,
                        "feature": 1,
                        "property": "opened",
                        "value": False
                    },
                    {
                        "type": "event",
                        "node": 53,
                        "event": "opened-changed",
                        "data": {}
                    }
                ],
                "syncId": 9,
                "clientId": 9
            },
        ]

        for step in steps:
            response = s.post(
                f"{self.base_url}/iter/?v-r=uidl&v-uiId=0", headers=headers, json=step)
            if verbose:
                print(response.status_code)
                print(response.text)

            if '"sessionExpired":true' in response.text:
                return False

        return True

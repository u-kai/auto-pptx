import unittest
import requests
import json
import subprocess
import os
import time


class TestServerTest(unittest.TestCase):
    def test_pptxを作成するリクエストを受け取ってpptxを作成できる(self):
        subprocess.Popen(["python", "app.py", "5000"])
        time.sleep(1)

        req = {
            "filename": "test.pptx",
            "slides": [
                {
                    "type": "title_only",
                    "title": "This is Slide 1",
                },
                {
                    "type": "title_and_content",
                    "title": "This is Slide 2",
                    "contents": [
                        {
                            "text": "Hello World",
                        },
                        {
                            "text": "Good Bye",
                            "children": [
                                {
                                    "text": "ChildRen",
                                },
                            ],
                        },
                    ],
                },
            ],
        }
        request = requests.post(
            # For some reason, I can't connect to localhost:5000
            # so, I use 127.0.0.1:5000 instead
            "http://127.0.0.1:5000/create_pptx",
            data=json.dumps(req),
            headers={"Content-Type": "application/json"},
        )

        self.assertEqual(request.status_code, 200)

        try:
            with open("test.pptx", "rb") as f:
                print("Success to create pptx to server test")
                os.remove("test.pptx")
        except:
            print("Failed to create pptx to server test")
            raise Exception("Failed to create pptx to server test")

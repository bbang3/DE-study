# import requests
import json
import os
import urllib

import requests
from dotenv import load_dotenv

load_dotenv()


def lambda_handler(event, context):
    print(f"Event: {event}")
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
    msg = _format_message(event)
    encoded = json.dumps(msg).encode("utf-8")

    response = requests.post(
        SLACK_WEBHOOK_URL,
        data=encoded,
        headers={"Content-Type": "application/json"},
    )

    return {
        "statusCode": response.status_code,
        "body": json.dumps(f"Slack message sent: {msg}"),
    }


def _format_message(event) -> dict:
    record = event["Records"][0]
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "text": "두근두근💓 파일이 S3에 업로드되었어요! 무슨 파일일까요?",
                    "type": "mrkdwn",
                },
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Object key*\n{urllib.parse.unquote(record['s3']['object']['key'])}",
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Object size*\n{record['s3']['object']['size']}",
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Event*\n{record['eventName']}",
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Bucket*\n{record['s3']['bucket']['name']}",
                    },
                    {"type": "mrkdwn", "text": f"*Time*\n{record['eventTime']}"},
                    {
                        "type": "mrkdwn",
                        "text": f"*Uploader*\n{record['userIdentity']['principalId']}",
                    },
                ],
            }
        ]
    }

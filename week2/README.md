# Week 2
- Slack notification when S3 Upload

## How to run
1. Create virtual environment and install dependencies
    ```bash
    python -m virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Set environment variables in `.env`
    ```python
    SLACK_WEBHOOK_URL="<YOUR_WEBHOOK_URL>"
    ```
3. Compress labmda function and installed packages into one file.
    ```bash
    cd venv/lib/python3.11/site-packages/
    zip -r lambda.zip venv/lib/python3.11/site-packages/
    zip -g lambda.zip slack_alert.py .env
    ```

4. Upload the zip file to your AWS Lambda
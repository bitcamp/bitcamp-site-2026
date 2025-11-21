from bitbot import receive
import json

def lambda_handler(event, context):
    """
    Expected POST body: { "message": "hello" }
    """
    try:
        body = json.loads(event.get("body", "{}"))
        user_message = body.get("message", "")

        if not user_message:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No message provided"})
            }

        # Use the standalone receive() function
        bot_reply = receive(user_message)

        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps({ "reply": bot_reply })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

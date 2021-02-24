import base64
base64_message = 'UjBWTVRFQkZibU55ZVhCMExuSmxkbVZ5YzJVdWMzQnNhU2dwS0dWNFpXTW9ZbUZXWTJ4UmQyTkZjMnhJTm1oaFVHVklkdz09'
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)

import json

# file = 'files/messages/inbox/MartynaLipinska_-dkdE-MIeg/message_1.json'
file = 'files/messages/inbox/mateusznycz_0xu-u6ou3q/message_1.json'


def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
            .decode('unicode-escape')
            .encode('latin1')
            .decode(encoding))


# TODO: make messages a Message instance
class Conversation:
    def __init__(self, data):
        self.participants = data['participants']
        self.messages = data['messages']


# TODO: Smarter way of doing this? Not by data. Other methods like __repr__
class Message:
    def __init__(self, data):
        self.sender = data['sender_name']
        self.timestamp = data['timestamp_ms']
        self.content = data['content']


if __name__ == '__main__':
    with open(file) as f:
        data = json.load(f)

    nycz_conv = Conversation(data)
    for msg in nycz_conv.messages:
        msg = Message(msg)
        print(string_escape(f'[{msg.timestamp}] {msg.sender}: {msg.content}'))

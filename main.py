import json
from datetime import datetime

# file = 'files/messages/inbox/MartynaLipinska_-dkdE-MIeg/message_1.json'
file = 'files/messages/inbox/mateusznycz_0xu-u6ou3q/message_1.json'


def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
            .decode('unicode-escape')
            .encode('latin1')
            .decode(encoding))


class Conversation:
    __slots__ = ['participants', 'messages', 'title', 'is_still_participant', 'thread_type', 'thread_path']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.messages = [Message(**message) for message in self.messages]

    def __len__(self):
        return len(self.messages)

    def __str__(self):
        return f'Conversation: {self.title}'


class Message:
    __slots__ = ['sender_name', 'timestamp_ms', 'content', 'type']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return f'[{self.timestamp_ms}] {self.sender_name}: {self.content}'


if __name__ == '__main__':
    with open(file) as f:
        data = json.load(f)

    nycz_conv = Conversation(**data)
    print(nycz_conv)

    for ms in nycz_conv.messages:
        print(ms)

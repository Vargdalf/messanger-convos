import json

# file = 'files/messages/inbox/mateusznycz_0xu-u6ou3q/message_1.json'
file = 'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_1.json'
file_second = 'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_2.json'


def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
            .decode('unicode-escape')
            .encode('latin1')
            .decode(encoding))


# TODO: update() function
class Conversation:

    def __init__(self, *conversations):
        self.participants: list = list()
        self.messages: list = list()
        for file in conversations:
            with open(file) as f:
                conversation = json.load(f)
            print('hello')
            self.participants += sorted(conversation['participants'], key=lambda x: x['name'])
            self.messages += [Message(message) for message in conversation['messages']]
            self.title: str = conversation['title']
            self.is_still_participant: bool = conversation['is_still_participant']
            self.thread_type: str = conversation['thread_type']
            self.thread_path: str = conversation['thread_path']

    def __len__(self):
        return len(self.messages)

    def __str__(self):
        return f'Conversation: {self.title}'


class Message:

    def __init__(self, message):
        self.author: str = message['sender_name']
        self.timestamp: int = message['timestamp_ms']
        self.type: str = message['type']

        # Content:
        self.content = self.share = None

        if 'content' in message:
            self.content: str = message['content']
        if 'share' in message:
            self.share: dict = message['share']

        # Instead of content
        self.audio_files = self.videos = self.gifs = self.photos = self.sticker = None

        if 'audio_files' in message:
            self.audio_files: list = message['audio_files']
        if 'videos' in message:
            self.videos: list = message['videos']
        if 'gifs' in message:
            self.gifs: list = message['gifs']
        if 'photos' in message:
            self.photos: list = message['photos']
        if 'sticker' in message:
            self.sticker: dict = message['sticker']

        # Can be on any message
        self.reactions = None
        if 'reactions' in message:
            self.reactions: list = message['reactions']

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return f'[{self.timestamp}] {self.author}: {self.content}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # with open(file) as f:
    #     data = json.load(f)

    conv = Conversation(file, file_second)
    print(len(conv.messages))
    # a = [1, 2, 3]
    # b = [2, 3, 4]
    # c = [x for x in b if x not in a] <--- TODO: SOMETHING LIKE THIS TO AVOID DUPS IN PARTICIPANTS OR SOMETHING
    #
    # a = conv.messages.copy()
    # b = conv.messages.copy()
    # import random
    #
    # random.shuffle(b)
    # print(a == b)
    # b.sort(key=lambda x: x.timestamp, reverse=True)
    # print(a == b)
    print(conv.participants)

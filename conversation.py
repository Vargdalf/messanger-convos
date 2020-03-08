import json
import itertools


# TODO: Check for \ at the end of string. Will be in the form of '\\"'
# Can actually be any number of backslashes ://
def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
            .decode('unicode-escape')
            .encode('latin1')
            .decode(encoding))


class Conversation:

    def __init__(self, *conversations):
        self.participants: list = list()
        self.messages: list = list()
        self.title: str = str()
        self.thread_type: str = str()
        self.thread_path: str = str()

        self.update(*conversations)

    def __len__(self):
        return len(self.messages)

    def __str__(self):
        return f'Conversation: {self.title}'

    def __repr__(self):
        return self.__str__()

    def update(self, *conversations):
        for file in conversations:
            with open(file) as f:
                conversation = json.load(f)

            self.participants += [participant for participant in conversation['participants'] if
                                  participant not in self.participants]
            self.messages += [Message(message) for message in conversation['messages']]
            self.title: str = conversation['title']
            self.thread_type: str = conversation['thread_type']
            self.thread_path: str = conversation['thread_path']

        self.participants.sort(key=lambda x: x['name'])
        self.messages.sort(key=lambda x: x.timestamp, reverse=True)

    def escape(self, encoding='utf-8'):
        self.title = string_escape(self.title, encoding)
        self.participants = [{'name': string_escape(participant['name'], encoding)} for participant in
                             self.participants]
        [message.escape(encoding=encoding) for message in self.messages]

    def words(self):
        words = [message.words() for message in self.messages if message.words() is not None]
        return list(itertools.chain(*words))

    def reactions(self):
        reactions = [message.reactions for message in self.messages if message.reactions is not None]
        return list(itertools.chain(*reactions))


class Message:

    def __init__(self, message):
        self.author: str = message['sender_name']
        self.timestamp: int = message['timestamp_ms']
        self.type: str = message['type']
        self.type_of_message: str = 'Deleted'

        # Content:
        self.content = self.current_content = self.share = None

        if 'content' in message:
            self.content: str = message['content']
            self.current_content = self.content
            self.type_of_message: str = 'Text'
        if 'share' in message:
            self.share: dict = message['share']
            self.type_of_message: str = 'Share'

        # Instead of content
        self.audio_files = self.videos = self.gifs = self.photos = self.sticker = None

        if 'audio_files' in message:
            self.audio_files: list = message['audio_files']
            self.current_content = self.audio_files
            self.type_of_message: str = 'Audio'
        if 'videos' in message:
            self.videos: list = message['videos']
            self.current_content = self.videos
            self.type_of_message: str = 'Video'
        if 'gifs' in message:
            self.gifs: list = message['gifs']
            self.current_content = self.gifs
            self.type_of_message: str = 'Gif'
        if 'photos' in message:
            self.photos: list = message['photos']
            self.current_content = self.photos
            self.type_of_message: str = 'Photo'
        if 'sticker' in message:
            self.sticker: dict = message['sticker']
            self.current_content = self.sticker
            self.type_of_message: str = 'Sticker'

        # Can be on any message
        self.reactions = None
        if 'reactions' in message:
            self.reactions: list = message['reactions']

    def __len__(self):
        return len(self.current_content)

    def __str__(self):
        return f'[{self.timestamp}] {self.author}: "{self.current_content}"'

    def __repr__(self):
        return self.__str__()

    def words(self):
        return self.content.split() if self.content is not None else None

    def escape(self, encoding='utf-8'):
        self.author = string_escape(self.author, encoding=encoding)
        if self.content:
            self.content = string_escape(self.content, encoding=encoding)
            self.current_content = string_escape(self.current_content, encoding=encoding)

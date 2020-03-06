import json


# TODO: add string_escape() method to escape participants, messages, title (later)
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


class Message:

    def __init__(self, message):
        self.author: str = message['sender_name']
        self.timestamp: int = message['timestamp_ms']
        self.type: str = message['type']

        # Content:
        self.content = self.current_content = self.share = None

        if 'content' in message:
            self.content: str = message['content']
            self.current_content = self.content
        if 'share' in message:
            self.share: dict = message['share']

        # Instead of content
        self.audio_files = self.videos = self.gifs = self.photos = self.sticker = None

        if 'audio_files' in message:
            self.audio_files: list = message['audio_files']
            self.current_content = self.audio_files
        if 'videos' in message:
            self.videos: list = message['videos']
            self.current_content = self.videos
        if 'gifs' in message:
            self.gifs: list = message['gifs']
            self.current_content = self.gifs
        if 'photos' in message:
            self.photos: list = message['photos']
            self.current_content = self.photos
        if 'sticker' in message:
            self.sticker: dict = message['sticker']
            self.current_content = self.sticker

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

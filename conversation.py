import json
import itertools


# TODO: Check for \ at the end of string. Will be in the form of '\\"'
# Can actually be any number of backslashes ://
def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
            .decode('unicode-escape')
            .encode('latin1')
            .decode(encoding))


def avg_length(messages):
    txt_msgs = [x for x in messages if x.content is not None]
    lengths = [len(x) for x in txt_msgs]
    return round(sum(lengths) / len(lengths))


def avg_words(messages):
    lengths = [len(x.words()) for x in messages if x.words() is not None]
    return round(sum(lengths) / len(lengths))


def stats(conversation):
    # How many messages?
    print(f'Total number of messages: {len(conversation)}')
    # How many words?
    print(f'Total number of words: {len(conversation.words())}')

    # Messages by Ola :3
    messages_by_ola = [x for x in conversation.messages if x.author == 'Aleksandra Kogut']
    print(f'Messages by Ola: {len(messages_by_ola)}')

    # Messages by Kacper
    messages_by_kacper = [x for x in conversation.messages if x.author == 'Kacper Mieszała']
    print(f'Messages by Kacper: {len(messages_by_kacper)}')

    # Words by Ola :3
    ola_words = [x.words() for x in messages_by_ola if x.words() is not None]
    words_by_ola = len(list(itertools.chain(*ola_words)))
    print(f'Words by Ola: {words_by_ola}')

    # Words by Kacper
    my_words = [x.words() for x in messages_by_kacper if x.words() is not None]
    words_by_kacper = len(list(itertools.chain(*my_words)))
    print(f'Words by Kacper: {words_by_kacper}')

    # Average length of message
    # By Ola :3
    print(f'Average length of message by Ola: {avg_length(messages_by_ola)}')

    # By Kacper
    print(f'Average length of message by Kacper: {avg_length(messages_by_kacper)}')

    # Average words per message
    # By Ola :3
    print(f'Average number of words per message by Ola: {avg_words(messages_by_ola)}')

    # By Kacper
    print(f'Average number of words per message by Kacper: {avg_words(messages_by_kacper)}')

    # Number of reactions
    # By Ola :3
    ola_reactions = [x for x in conversation.reactions() if 'Kogut' in x['actor']]
    print(f'Number of reactions by Ola: {len(ola_reactions)}')

    # By Kacper
    kacper_reactions = [x for x in conversation.reactions() if 'Kacper' in x['actor']]
    print(f'Numver of reactions by Kacper: {len(kacper_reactions)}')


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

    def words(self):
        return self.content.split() if self.content is not None else None

    def escape(self, encoding='utf-8'):
        self.author = string_escape(self.author, encoding=encoding)
        if self.content:
            self.content = string_escape(self.content, encoding=encoding)
            self.current_content = string_escape(self.current_content, encoding=encoding)

import itertools

from conversation import Conversation

files = [
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_1.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_2.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_3.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_4.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_5.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_6.json',
]
files_2 = [
    'files/messages/inbox/KamilMusial_bABm7_mZxQ/message_1.json',
    'files/messages/inbox/KamilMusial_bABm7_mZxQ/message_2.json',
    'files/messages/inbox/KamilMusial_bABm7_mZxQ/message_3.json',
    'files/messages/inbox/KamilMusial_bABm7_mZxQ/message_4.json',
    'files/messages/inbox/KamilMusial_bABm7_mZxQ/message_5.json',
    'files/messages/inbox/KamilMusial_bABm7_mZxQ/message_6.json',
]


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


if __name__ == '__main__':
    conv = Conversation(*files)
    conv.escape()
    stats(conv)

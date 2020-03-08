import itertools


def avg_length(messages):
    txt_msgs = [x for x in messages if x.content is not None]
    lengths = [len(x) for x in txt_msgs]
    return round(sum(lengths) / len(lengths))


def avg_words(messages):
    lengths = [len(x.words()) for x in messages if x.words() is not None]
    return round(sum(lengths) / len(lengths))


def divided_messages(messages):
    counts = {}
    for message in messages:
        if message.type_of_message in counts:
            counts[message.type_of_message] += 1
        else:
            counts[message.type_of_message] = 1
    print(
        f'Which consists of: '
        f'Text: {counts["Text"]}, '
        f'Photo: {counts["Photo"]}, '
        f'Video: {counts["Video"]}, '
        f'Sticker: {counts["Sticker"]}, '
        f'Gif: {counts["Gif"]}, '
        f'Audio: {counts["Audio"]}, '
        f'Share: {counts["Share"]}, '
        f'Deleted: {counts["Deleted"]}')


def top_x_most_used_words(messages, x=10):
    words = [message.words() for message in messages if message.words() is not None]
    words = list(itertools.chain(*words))
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    result = {}
    for i in range(x):
        result.update({max(word_count, key=lambda key: word_count[key]): max(word_count.values())})
        word_count.pop(max(word_count, key=lambda key: word_count[key]))
    return result


def stats(conversation):
    # How many messages?
    print(f'Total number of messages: {len(conversation)}')
    # How many words?
    print(f'Total number of words: {len(conversation.words())}')
    print(f'10 top used words overall: {top_x_most_used_words(conversation.messages)}')

    # Messages by Ola :3
    messages_by_ola = [x for x in conversation.messages if x.author == 'Aleksandra Kogut']
    print(f'Messages by Ola: {len(messages_by_ola)}')

    # Messages by Kacper
    messages_by_kacper = [x for x in conversation.messages if x.author == 'Kacper Mieszała']
    print(f'Messages by Kacper: {len(messages_by_kacper)}')

    divided_messages(messages_by_ola)
    divided_messages(messages_by_kacper)

    # Words by Ola :3
    ola_words = [x.words() for x in messages_by_ola if x.words() is not None]
    words_by_ola = len(list(itertools.chain(*ola_words)))
    print(f'Words by Ola: {words_by_ola}')

    # Words by Kacper
    kacper_words = [x.words() for x in messages_by_kacper if x.words() is not None]
    words_by_kacper = len(list(itertools.chain(*kacper_words)))
    print(f'Words by Kacper: {words_by_kacper}')

    print(f'10 most used words by Ola: {top_x_most_used_words(messages_by_ola)}')
    print(f'10 most used words by Kacper: {top_x_most_used_words(messages_by_kacper)}')

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

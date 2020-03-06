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


def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
            .decode('unicode-escape')
            .encode('latin1')
            .decode(encoding))


if __name__ == '__main__':
    conv = Conversation(*files)
    print(len(conv.messages))

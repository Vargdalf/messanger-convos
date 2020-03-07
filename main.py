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

if __name__ == '__main__':
    conv = Conversation(*files)
    conv.escape()
    print(len(conv.messages))
    print(conv.participants)
    print(conv.messages[100:120])

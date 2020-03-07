from wordcloud import WordCloud
import matplotlib.pyplot as plt

from conversation import Conversation

files = [
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_1.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_2.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_3.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_4.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_5.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_6.json',
]


def word_map_all(conversation):
    words = ' '.join(conversation.words())
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(words)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.show()


if __name__ == '__main__':
    conv = Conversation(*files)
    conv.escape()
    word_map_all(conv)

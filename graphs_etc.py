import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

from conversation import Conversation

files = [
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_1.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_2.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_3.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_4.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_5.json',
    'files/messages/inbox/AleksandraKogut_6TQX1Y0GGw/message_6.json',
]


def word_map_all(conversation, width=480, height=480):
    words = ' '.join(conversation.words())
    wordcloud = WordCloud(width=width, height=height, margin=0).generate(words)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.show()


def words_map_mask(conversation, mask):
    words = ' '.join(conversation.words())
    wordcloud = WordCloud(mask=mask).generate(words)

    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.show()


if __name__ == '__main__':
    conv = Conversation(*files)
    conv.escape()

    # Normal Word Map
    # word_map_all(conv)

    frog_mask = np.array(Image.open('files/images/frog.jpg'))
    heart_mask = np.array(Image.open('files/images/heart.jpg'))

    # Word map with mask
    # words_map_mask(conv, heart_mask)

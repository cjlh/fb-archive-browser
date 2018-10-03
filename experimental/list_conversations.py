import os
import json


class Conversation(object):
    def __init__(self, name, dirname):
        self.name = name
        self.dirname = dirname


def get_fb_dir():
    data_dir = "../data"
    fb_dir = None
    for dirname in next(os.walk(data_dir))[1]:
        if (dirname[0:9] == "facebook-"):
            fb_dir = data_dir + "/" + dirname
    return fb_dir


def get_conversations_list(fb_dir):
    messages_dir = fb_dir + "/messages"
    special_dirs = ["stickers_used"]
    conversations = []
    for dirname in next(os.walk(messages_dir))[1]:
        # For each conversation, there is an all-lowercase directory containing
        # the messages.json file. When a conversation contains media there is
        # a separate directory with the same name, except that the person's
        # name has PascalCase. So we check that the current directory is
        # all-lowercase.
        if (dirname.lower() != dirname or dirname in special_dirs):
            continue
        full_dirname = messages_dir + "/" + dirname
        with open(full_dirname + "/message.json") as f:
            messages_data = json.load(f)
        name = messages_data["participants"][0]["name"]
        conversations.append(Conversation(name, full_dirname))
    return conversations


if (__name__ == "__main__"):
    fb_dir = get_fb_dir()
    if (fb_dir is None):
        print("Facebook archive directory not found.")

    print("Facebook directory:", fb_dir)

    print("Conversations:")
    conversations = get_conversations_list(fb_dir)
    for conversation in conversations:
        print("-", conversation.name)

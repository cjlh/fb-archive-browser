import os
import json


class Conversation(object):
    def __init__(self, participants, path, media_path, title,
                 is_still_participant, thread_type):
        self.participants = participants
        self.path = path
        self.media_path = media_path
        self.title = title
        self.is_still_participant = is_still_participant
        self.thread_type = thread_type


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

        path = messages_dir + "/" + dirname
        with open(path + "/message.json") as f:
            messages_data = json.load(f)

        participants = []
        for participant in messages_data["participants"]:
            participants.append(participant["name"])

        media_path = messages_dir + "/" + messages_data["thread_path"]

        title = messages_data.get("title", "Facebook User")

        conversations.append(
            Conversation(participants, path, media_path, title,
                         messages_data["is_still_participant"],
                         messages_data["thread_type"]))
    return conversations


if (__name__ == "__main__"):
    fb_dir = get_fb_dir()
    if (fb_dir is None):
        print("Facebook archive directory not found.")
        exit()

    print("Facebook directory:", fb_dir)

    print("Conversations:")
    conversations = get_conversations_list(fb_dir)
    for conversation in conversations:
        print("-", conversation.title)

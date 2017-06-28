# Name:
# Date

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup


# -----------------------------------------------------------------------
#
# proj08: RSS Feed Filter

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret


# ======================
# Part 1
# Data structure design
# ======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link


# TODO: NewsStory

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):

        # return True
        # return False
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    # Body refers to the text in the news story
    def is_word_in(self, body):
        triggerword = self.word.lower()
        body = body.lower()
    # For loop added to check each character (including punctuation in the body content of the news story)
        for characters in string.punctuation:
            if characters in string.punctuation:
                body = body.replace(characters, ' ')
                #body = body.replace(characters, '')
    # Split the body back up
        body = body.split()

        if triggerword in body:
            return True
        else:
            return False

# TODO: TitleTrigger

class TitleTrigger(WordTrigger):
    def evaluate(self, story):

        title = story.get_title()

        notification = self.is_word_in(title)

        return notification
# 
# 
# 
# TODO: SubjectTrigger

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        subject = story.get_subject()
        notification = self.is_word_in(subject)
        return notification


# TODO: SummaryTrigger

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        summary = story.get_summary()
        notification = self.is_word_in(summary)
        return notification

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, work):
        self.work = work
    def evaluate(self, work2):
        if self.work.evaluate(work2) is not True:
            return True
        else:
            return False
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, work, work3):
        self.work = work
        self.work3 = work3
    def evaluate(self, work2):
        if self.work.evaluate(work2) and self.work3.evaluate(work2) == True:
            return True
        else:
            return False

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, work, work3):
        self.work = work
        self.work3 = work3
    def evaluate(self, work2):
        if self.work.evaluate(work2) or self.work3.evaluate(work2) == True:
            return True
        else:
            return False

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        summary = story.get_summary()
        title = story.get_title()
        subject = story.get_subject()
        return self.phrase in subject or self.phrase in title or self.phrase in summary
#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):

    final_pulled_list = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                final_pulled_list.append(story)
    return final_pulled_list
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    return stories

#======================
# Extensions: Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    x = raw_input("Pick a subject with correct grammer: ")
    t1 = SubjectTrigger(x)
    t2 = SummaryTrigger(x)
    t3 = PhraseTrigger(x)
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()


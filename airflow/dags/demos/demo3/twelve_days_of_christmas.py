import argparse

parser = argparse.ArgumentParser(description='Return n verses of "12 Days of Christmas".')
parser.add_argument('--verses', type=int, default=1,help='an integer for the number of verses to return')
args = parser.parse_args()

num_verses = args.verses

lyrics = [
    'A partridge in a pear tree',
    'Two turtledoves',
    'Three French hens',
    'Four calling birds',
    'Five golden rings',
    'Six geese a-laying',
    'Seven swans a-swimming',
    'Eight maids a-milking',
    'Nine ladies dancing',
    'Ten lords a-leaping',
    'Eleven pipers piping',
    'Twelve drummers drumming',
]

verse_num = 1
while verse_num <= num_verses:
    verses = lyrics[0:verse_num]
    verses.reverse()
    print(f"On the {verse_num} day of Christmas, my true love gave to me:")
    for verse in verses:
        print(verse)
    print("")
    verse_num +=1

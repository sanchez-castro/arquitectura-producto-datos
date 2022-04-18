"""Script for returning n verses of 'Twelve Days of Christmas'"""

import argparse
# Parser takes 1 Argument: --verses
parser = argparse.ArgumentParser(description='Return n verses of "12 Days of Christmas".')
parser.add_argument('--verses', type=int, default=1,help='an integer for the number of verses to return')
args = parser.parse_args()

# Extract Verses Arg
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

# Start with first verse
verse_num = 1
# While nth verse is less than or equal to the number of verses to return
while verse_num <= num_verses:
    # Grab first N verses
    verses = lyrics[0:verse_num]
    # Flip the order of verses
    verses.reverse()
    print(f"On the {verse_num} day of Christmas, my true love gave to me:")
    # Print each verse to return
    for verse in verses:
        print(verse)
    #Print a new line for formatting
    print("")
    # Move on to the next verse
    verse_num +=1

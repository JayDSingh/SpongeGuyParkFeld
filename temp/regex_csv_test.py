import csv
import re

test_str = """JERRY: You know, why we're here? [he means: here in the "Comedy
              club"] To be out, this is out...and out is one of the single
              most enjoyable experiences of life. People...did you ever hear people
              talking about "We should go out"? This is what they're
              talking about...this whole thing, we're all out now, no one is home.
              Not one person here is home, we're all out! There are people tryin'
              to find us, they don't know where we are. [imitates one of these
              people "tryin' to find us"; pretends his hand is a phone]
              "Did you ring?, I can't find him." [imitates other person
              on phone] "Where did he go?"  """

print(test_str)

new_str = re.sub(r'[\(\[].*?[\)\]]', "", test_str, flags = re.S)

new_str2 = new_str.split(':')

print(new_str2)

with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(new_str2)

# Summary of Files

### clean_seinfeld.py
Outdated file used to organize messy seinfeld transcript.

### regex_csv_test.py
Tester file which takes the first line in seinfeld and (1) removes brackets then (2) separates it between speaker and line. Used to help create main/scrape_seinfeld.py

### text_gen.py
Text generator using LTSM (Long Time Short Memory) Neural Network. Code adapted from https://github.com/spiglerg/RNN_Text_Generation_Tensorflow.
Run with `python3 text_gen.py --input_file=\path_to_transcript --ckpt_file="saved/model.ckpt" --mode=train`
`--input_file` defaults to "southpark_transcript.csv" in temp.
This code can be ran from anywhere within SpongeGuyParkFeld on your machine.
Training it takes days...

### PandaNB.py
basis for show classification using the Pandas library
currently predicting with MultinomialNB

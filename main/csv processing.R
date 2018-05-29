# finding the six most frequent speakers and their lines from each csv
# hard-coded and messy, function could be better for this purpose... 

# spongebob and south park and seinfeld

# read in data for each
sponge = data.frame(read.csv("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/temp/spongebob_transcript.csv"))
south = data.frame(read.csv("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/temp/southpark_transcript.csv"))
seinfeld = data.frame(read.csv("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/main/seinfeld_transcript.csv"))

# find column names for each, figure out which contains speaker name
colnames(sponge)
colnames(south)
colnames(seinfeld)

# use speaker name to find the 6 most frequent speakers
freqsponge = names(tail(sort(table(sponge["X"])), 6))
freqsouth = names(tail(sort(table(south["Character"])), 6))
freqseinfeld = names(tail(sort(table(seinfeld["Character"])), 6))

# load dplyr for filtering by speakers
library(dplyr)

# finding entries in the spongebob (and others) data that are by the top 6 speakers of spongebob
spongest = dplyr::filter(sponge, X %in% freqsponge)
southest = dplyr::filter(south, Character %in% freqsouth)
seinfeldest = dplyr::filter(seinfeld, Character %in% freqseinfeld)

# writes to csv, change names and variables for each
write.csv(seinfeldest, "six_freq_seinfeld.csv", row.names = FALSE)

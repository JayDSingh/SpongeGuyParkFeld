

# finding the six most frequent speakers and their lines from each csv

# spongebob and south park and seinfeld

setwd("C:/Users/Lauren Shin/Desktop")

sponge = data.frame(read.csv("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/temp/spongebob_transcript.csv"))
south = data.frame(read.csv("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/temp/southpark_transcript.csv"))
seinfeld = data.frame(read.csv("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/main/seinfeld_transcript.csv"))

attach(sponge)
attach(south)
attach(seinfeld)

colnames(sponge)
colnames(south)
colnames(seinfeld)
freqsponge = names(tail(sort(table(sponge["X"])), 6))
freqsouth = names(tail(sort(table(south["Character"])), 6))
freqseinfeld = names(tail(sort(table(seinfeld["Character"])), 6))

library(dplyr)

spongest = dplyr::filter(sponge, X == freqsponge)

southest = dplyr::filter(south, Character == freqsouth)

seinfeldest = dplyr::filter(seinfeld, Character == freqseinfeld)

write.csv(seinfeldest, "six_freq_seinfeld.csv", row.names = FALSE)

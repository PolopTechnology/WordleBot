# WordleBot
Bot that plays Wordle! It isn't technically machine learning, but it does use automation algorithms.

## How it works 
It goes through every word in a five-letter dataset and goes through every possibility and determines
a "value" (based on the number of words left. Scenarios with high values mean there is a low amount
of choices and a low value means a lot of words it could be). It takes the average and that becomes
the "total value" of a word. It then is also compared to how common the word is. The result being;
The highest ranking word is a combination of the word that leaves very little choices on average
and a very common word. This word becomes the starter word.

Once you enter the recommended word into Wordle, you are asked to input to the program the results.
it should be written like this; 1 0 0 1 1. (0 equals gray, 1 equals yellow, 2 equals green). It
will use this data to shorten the dataset and then repeat the above process to take the highest
ranking word. The process is completed until it reaches six tries, or it reaches all 2's (all
greens, therefore the correct word).

### Wordle
https://www.nytimes.com/games/wordle/index.html

Update:  The starter word will always be 'zowie' so instead of waiting 8 minutes for the bot
to calculate it, it has been hard coded in.

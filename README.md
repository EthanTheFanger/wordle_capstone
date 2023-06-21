# wordle_capstone

In my capstone project, I attempted to build something to solve wordle prolems for me. 
I had mainly two ways of solving a wordle, the first one directly finding the wordle answer from the wordle website, the second way was me coming up an algorithm to solve the wordle. 

## The first plan

The first plan worked and I found a link to the answer on the wordle website: https://www.nytimes.com/svc/wordle/v2/2023-[date].json
You can view each day's answer by changing the [date] for example, if you wanted the wordle answer on June 11, you would just type in https://www.nytimes.com/svc/wordle/v2/2023-6-11.json

Then I was able to figure out how to interact with the wordle API from this reddit post here: https://www.reddit.com/r/diyelectronics/comments/wp3tb0/anyone_managed_to_get_into_the_new_nyt_wordle_api/

The code to send commands to the API is included in the title.zip file, and I would run it using bash on a Macbook. 
It is not finished however, the last thing to do is to scrape the answer off of the answer website and then code up a program that would change the information that would be sent to the wordle API

## The second plan
This one went a bit less smoothly
I built a wordle clone first, but I was unable to come up with an algorithm,
I ended up following a guide on the internet: https://betterprogramming.pub/building-a-wordle-bot-in-under-100-lines-of-python-9b980539defb

However, the program is still slow and has an O(N^3) time complexity

Despite that, I learned how to turn a file into a list for the first time.

The code is unfinished 

import praw
import random
import datetime
import time
from textblob import TextBlob

# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "Biden has been doing a [terrible] job!! It is so [infuriating] to see what he is doing to this once [amazing] country. In my opinion, [Trump] was a much [better] president. ",
    "What has happened to our [country]?! I just went to McDonald’s and saw that the price for a [quarter pounder] is now [$4.99]!!! This is [outrageous] and it is all [Sleepy] Joe’s fault. ",
    "Have you guys paid attention to those [outrageous] gas prices?! Never in my [50] years in [Murica] have I ever seen gas so [goshdarn] expensive!!! Me and my [buddies] are going to stock up on gas right now. I’m storing my gas in [plastic bags]. THANKS SLEEPY JOE. ",
    "The kids these days are just so [lazy]! Back in my day, we would be out of the house by age [18]! I was working full time at [a pizza shop] for [$6] an hour and saved up for my first [car]. This is what happens when you put those libtards in charge. ",
    "I say SCREW JOE BIDEN! Let’s all [storm] the [capital] next [Wednesday]! I know we’re all sick and tired of this [PLANdemic] and all the lies Fauci and the Biden administration is feeding to [the public] >:( ",
    "I can’t believe some [people] still think Biden won the election. It was so obviously [rigged] when those poll workers ILLEGALLY [brought] in [a million] fake ballots. TRUMP [2021]!!!! "
    ]

replacements = {
    'terrible': ['terrible', 'wonderful', 'amazing', 'horrible', 'dreadul'],
    'infuriating': ['infuriating', 'frustrating','fascinating', 'inspiring'],
    'amazing': ['amazing', 'perfect', 'flawed', 'inspiring'],
    'Trump': ['Trump', 'Obama', 'Bush', 'Clinton'],
    'better': ['better', 'worse', 'more skilled'],
    'country': ['country', 'state', 'county','town'],
    'quarter pounder': ['quarter pounder', 'cheeseburger', 'hotdog'],
    '$4.99': ['$4.99', '$10.57', '$6.99', '$12.37'],
    'outrageous': ['outrageous', 'unacceptable', 'terrible'],
    'Sleepy': ['sleepy', 'stinky', 'ugly', 'old'],
    '50': ['50', '38', '80', '45'],
    'Murica': ['Murica', 'the Land of the Free', 'the US of A', 'the U.S.A.'],
    'goshdarn': ['gosh darn', 'freaking','bloody'],
    'buddies': ['buddies', 'friends', 'bros', 'family', 'cousins'],
    'plastic bags': ['plastic bags', 'five-gallon jugs', 'my trunk', 'my bunker'],
    'lazy': ['lazy', 'stubborn', 'distracted'],
    '18': ['18', '12', '16', '10'],
    'a pizza shop': ['a pizza shop', 'a grocery store', 'a toothpaste factory', 'a steel factory'],
    '$6': ['$6', '$4.50', '50 cents', '75 cents'],
    'car': ['car', 'apartment', 'house', 'airplane', 'boat'],
    'storm': ['storm', 'raid', 'attack', 'charge'],
    'capital': ['capital', 'White House', 'courthouse'],
    'Wednesday': ['Sunday', 'Monday', 'Wednesday', 'Friday'],
    'PLANdemic': ['PLANdemic', 'pandemic HOAX','covid bullcrap'],
    'the public': ['the public', 'the sheep', 'the snowflakes'],
    'people': ['people', 'sheep','libtards', 'snowflakes'],
    'rigged': ['rigged', 'manipulated', 'forged', 'fake'],
    'brought': ['brought', 'snuck in', 'counted'],
    'a million': ['a million', 'hundreds', 'a bajillion', 'thousands'],
    '2021': ['2020', '2021', '2022', '2024']
    }

def generate_comment():
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('[' + k + ']', random.choice(replacements[k]))
    return s

# select a "home" submission in the /r/BotTown subreddit to post to and put the url below
reddit = praw.Reddit('BottyMcThotty')
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

'''
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
'''

if True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)


    #TASK 0: get a list of all of the comments in the submission 
    # HINT: this requires using the .list() and the .replace_more() functions

    submission.comments.replace_more(limit=None)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))


    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments: 
        if str(comment.author) != 'anotha_bot' :
            not_my_comments.append(comment)

    print('len(not_my_comments)=',len(not_my_comments))

    
    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    #task 2
    if has_not_commented:
        text = generate_comment()
        submission.reply(text)

    
    else:
        #(task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        comments_without_replies = []

        for comment in not_my_comments:
            if comment.author != 'duckduckbotcs40':
                response = False
                for reply in comment.replies:
                    if str(reply.author) == 'duckduckbotcs40':
                        response = True
                if response is False:
                    comments_without_replies.append(comment)
        print('len(comments_without_replies)=',len(comments_without_replies))


        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        

        for comments in comments_without_replies:
            selection = random.choice(comments_without_replies)
            generated_reply = generate_comment()
            try:
                selection.reply(generated_reply)
            except praw.exceptions.RedditAPIException as error:
                if "DELETED_COMMENT" in str(error):
                    print("Comment " + comment.id + " was deleted")
                else:
                    print('Error Found: ', error)


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions

    randomnumber = random.random()
    allsubmissions = []
    if randomnumber >= 0.5:
        print('Original Sub')
        submission = reddit.submission(url='https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/')
        submission.reply(generate_comment())
    if randomnumber < 0.5:
        print('Top Subreddit Sub')
        for submission in reddit.subreddit('BotTown').hot(filter= 5):
            allsubmissions.append(submission)
        newsubmission = random.choice(allsubmissions)
        submission = reddit.submission(id=newsubmission)
        print('Submission ID: ', newsubmission)
        print(newsubmission.title)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)
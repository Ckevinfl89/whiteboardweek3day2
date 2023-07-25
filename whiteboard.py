# Given a word w 
# and some text t, find whether w is in t. 
# For example: 
# w="nest", t="I built a nest and tested it."
# output: "here"
# example 2:
# w="runs", t="The dog"
# output: "not here"
# Example 3: 
# w="April", t="april showers bring may flowers"
# output: "not here"


# eval the word (w) and see if its in text (t)

#case sensitive
# step 1 look at the word
# step 2 read the sentence out loud
# step 3 is the word in the sentence or not 
# step 4 answer is = "is here" or "not here"

w = 'nest'
t = 'I built a nest and tested it'
def solution(w,t):
    if w in t:
        return "here"
    else: return "not here"
        
solution(w,t)

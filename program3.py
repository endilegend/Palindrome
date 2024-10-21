######################################
# Endi Troqe
# 10-21-2024
######################################
import deque

#recursive function that goes over the phrases and checks if it is a plaindrome 
def palindrome(d):
    #base case (if the size is 1 then it must be a plaindrome and return the palindrome)
    if d.size() == 1:
        return (f"{text}\n")

    #removes the first and last letters and if they arent the same then it is not a plaindrome
    elif d.remove_front() != d.remove_rear():
        return (f"Phrase is not a palindrome\n")
    
    #if the size of the deque is 0 then it must be palindrome
    elif d.size() == 0:
        return (f"{text}\n")
    #if none of the conditions have been met repeat the recursive function
    else:
        return palindrome(d)


#file
file = "phrases.txt"

#opens file with the phrases and also opens a output file
with open(file, "r") as f, open("output3.txt", 'a') as o:
    #goes over every line in the phrases file
    for line in f:
        d = Deque()
        #gets rid of the new line and also makes the text lower case
        text = line.replace("\n","")
        text = text.lower()
        #adds every alphabetical character to the back of the deque
        for i in text:
            if i.isalpha():
                d.add_rear(i)
        #calls the function
        o.write(palindrome(d))


    
                
                
            



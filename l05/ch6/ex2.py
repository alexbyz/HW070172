#ex2
#the ants go marching
#now Idea how this song actually goes...

#The ants go marching one by one.
#Hoorah! Hoorah!
#The ants go marching one by one.
#Hoorah! Hoorah!
#The ants go marching one by one;
#The little one stops to suck his thumb,
#And they all go marching down to the ground
#To get out of the rain.
#Boom, boom, boom, boom!
# from : https://supersimple.com/song/ants-go-marching/

def hura():
    return "hurrah! hurrah!"

def marching(text):
    return "The ants go marching " + text + " by " + text + " "

def boom():
    return "\nAnd they all go marching down to the ground\nTo get out of the rain\nBoom, boom, boom, boom!\n\n"

def little(activity):
    return "\nThe little one stops to "+activity

def verse(number, activity):
    return (marching(number) + hura() +"\n")*2 + marching(number) + little(activity) + boom()

def main():

    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    activities = ["suck his thumb", "tie his shoe", "climb a tree", "shut the door", "take a dive", "pick up sticks", "pray to heaven", "rollerskate", "check the time", "shout"]
    
    for i in range(len(numbers)):
        print(verse( numbers[i], (activities[i])))
main()
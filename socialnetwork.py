## Jaslyn Palomino
## My Social Network

    ## Adding a friend with only using a username
    
class User:

    def createID(self, num):
        self.userID = num
    
    def __init__(self, username):
            self.username = username
            self.firstName = ""
            self.lastName = ""
            self.bio = ""
            self.friendslist = []
            self.posts = []
            friendsList = []
            posts = []

    def createPost(self, Content):
        mypost = post(content)
        self.post.append(mypost)
        myPost.createPostID(len(post))
        self.userID = ""

    def createUserID(self, num):
        self.userID = num
    
    def addfirstName(self, firstName):
        self.firstName = firstName

    def addlastName (self, lastName):
          self.lastName = lastName

    def addbio(self, bio):
        self.bio = bio

    def addFriend(self, obj):
       self.friendslist.append(obj)

    def viewFeed(self):
        for friend in self.friendslist:
            print(friend.username)
            print(friend.posts)
                                                                                                    ##kms
    
    def unFriend(self, obj):
        for friend in self.friendslist:
            if friend.username == obj.username:
                self.friendslist.remove(obj)
                
    def addposts (self, post):
        self.posts.append(post)
                  
    def showUsername (self):
        for friend in self.friendslist:
            print (friend.username)

class Post:
    def __init__(self, content):
        self.content = content
        self.postID = len
        self.commments = []
 
    def createPostID(self, num):
        self.postID = num

##    def addComment(self, comment):
##        self.comment.append.(comment)

class Network:
    def __init__ (self):
        self.users = []
        print ("User Created")

    def createUser(self, username):
##        for user in self.users:
##            if (user.username == username):
##                print ("Username Taken")
        myUser = User(username, mySize)
        self.users.append(myUser)
        mySize = int(len(self.users))+1
##        myUser.createUserID(mySize)
        print(len(self.users))

    def addConnection(self, user1, user2):
        user1OBJ = self.getOBJ(user1)
        user2OBJ = self.getOBJ(user2)

        user1OBJ.addfriends(user2OBJ)
        user2OBJ.addfriends(user1OBJ)

    def getOBJ(self, username):
        userID = self.getUserID(username)
        userOBJ = self.user [userID-1]
        print(userOBJ.username)
        return userOBJ

    def getsUserID(self, username):
        for i in self.users:
            if i.username == username:
                return i.userID
        
        
if __name__ == "__main__":
    network = Network ()
    network.createUser("jaslynpolynomial")
                  
##    username = "jaslynpolynomial"
##                  
##    jaslyn = User("jaslynpolynomial") 
##    em = User("em")
##    maxuel = User ("maxuel")
##
##                                    ##jaslyn.addpost("hi")
##                                    ##jaslyn.unfriend("maxuel")
####My Account
##    firstName = "Jaslyn"
##    lastName = "Palomino"
##    username = "jaslynpolynomial"
##    bio = "Hi, my name last name is actually Palomino"
##    userID = "0000"
##
####User
##    jaslyn = User("jaslynpolynomial")  
##    maxx = User("maxuel")
##    emily = User("em")
##    
####Posts
##    emily.addposts("Hello world")
##    maxx.addposts("This is a new post by Maxx")
##    
##    jaslyn.addFriend(maxx)
##    jaslyn.addFriend(emily)
##
##    jaslyn.viewFeed()
##
##    jaslyn.showUsername()
##
##    jaslyn.unFriend(maxx)
##
##    jaslyn.showUsername()
 

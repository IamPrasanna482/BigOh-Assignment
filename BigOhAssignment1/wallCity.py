
# Class User that stores username, email, password, prof
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.profile = {}

# Class Admin 
class Admin(User):
    def __init__(self,name,password):
        self.name = name
        self.password = password

# UserManagement class that stores different methods
class UserManager:
    def __init__(self):
        self.users = []

    # method to register users
    def register_user(self, username, email, password):
        newUser = User(username, email, password)
        self.users.append(newUser)
        print(f"{username} is successfully registered !")

    # method to login user
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("User is logged in !")
        return None

    # method to logout user
    def logout(self, userObj):
        print(f"User {userObj.username} logged out.")

    # method to find the hottest user
    def find_hottest_user(self, brickManageObj):
        userBricks = {user: 0 for user in self.users}
        for brick in brickManageObj.bricks:
            userBricks[brick.owner] += 1
        hottestGuy = max(userBricks, key=userBricks.get)
        print(f"The hottest guy is {hottestGuy}")

    # method to print the users
    def printUsers(self):
        li = self.users
        for i in li:
            print(i)

# Class Citywall
class CityWall:
    def __init__(self):
        self.walls = []
        self.totalWalls = 0

    # method to create a method
    def add_wall(self, wall):
        self.walls.append(wall)
        self.totalWalls += 1


# class Brick
class Brick:
    def __init__(self, owner, caption, message, dedication):
        self.owner = owner
        self.caption = caption
        self.message = message
        self.dedication = dedication
        self.flagCount = 0
        self.visible = True

# Class brickmanager that stores different methods
class BrickManager:
    def __init__(self):
        self.bricks = []
        self.totalBricks = 0
    
    # method to create a brick
    def createBrick(self, owner, caption, message, dedication):
        new_brick = Brick(owner, caption, message, dedication)
        self.bricks.append(new_brick)
        self.total_bricks += 1
        self.brickAssociated[owner] = new_brick
        print(f"New brick is created flr the user {owner}")


    # method to edit brick
    def edit_brick(self, user, brickObj, newCaption, newMessage, newDedication):
        if user == brickObj.owner:
            brickObj.caption = newCaption
            brickObj.message = newMessage
            brickObj.dedication = newDedication
    
    # method to edit admin
    def editAdmin(self,userObj, brickObj, newCaption, newMessage):
        brickObj.caption = newCaption
        brickObj.message = newMessage

    # method to flag a brick
    def flag_brick(self, brickObj):
        brickObj.flagCount += 1
        if brickObj.flagCount > 10:
            brickObj.visible = False

    # method to animate a brick
    def animate_brick(self, brickObj):
        print(f"{brickObj.owner}'s brick is being animated !")
        

# create a UUID for adminto restrict access
adminUUID = 1234

def main():
    umg = UserManager()
    bmg = BrickManager()
    adm = Admin('prasanna',password=1234)


    while True:
        print("Welcome to WallCity Program !")
        print("Welcome to Bank")
        print("1. Admin")  
        print("2. User")  
        print("3. Exit") 

        ch = int(input("Enter your choice"))

        if ch == 1:
            print("Welcome Admin")
            adminID = int(input("Enter the admin password "))
            print(adminID)
            print(adminUUID)
            if adminID != adminUUID:
                print("Authentication failed")
            else:
                # methods for the admin
                while True:
                    print("1. Edit Brick")
                    print("2. Add users")
                    print("3. Print Users")
                    print("4. Exit")

                    ch1 = int(input("Enter your choice"))

                    if ch1==1:
                        name = input("Enter whose brick to be edited")
                        caption = input("Enter new caption")
                        message = input("Enter new message")
                        bmg.editAdmin(name,caption,message)
                    
                    elif ch1 == 2:

                        umg.printUsers()

                    elif ch1 == 3:
                        n = int(input("Enter the amount of users to be added"))
                        for i in range(n):
                            username = input(f"Enter username for user {i+1}: ")
                            email = input("Enter email: ")
                            password = input("Enter password: ")
                            umg.register_user(username, email, password)
                    elif ch1 == 3:
                        break

        elif ch == 2:
            print("Welcome User")
            while True:
                print("1. Login")
                print("2. Create Brick")
                print("3. Edit Brick")
                print("4. Flag brick")
                print("5. Find Hottest Guy or Girl")
                print("6. Find users without dedications")
                print("7. Login")
                print("8. Exit")


                ch1 = int(input("Enter the choice : "))

                if ch1 == 1:
                    username = input("Enter the username : ")
                    password = input("Enter the password : ")
                    umg.login(username,password)
                
                elif ch1 == 2:
                    owner = umg.users[0]
                    bmg.createBrick(owner, "Caption", "Message", "Dedication")

                elif ch1 == 3:
                    bmg.edit_brick(owner, "New Caption", "New Message", "New Dedication")
                    print("Brick edited successfully.")
            
                elif ch1 == 4:
                    for _ in range(11):
                        bmg.flag_brick()
                    if bmg.visible:
                        print("Brick is visible.")
                    else:
                        print("Brick is invisible.")
                
                elif ch1 == 5:
                    hottest_user = umg.find_hottest_user(bmg)
                    print(f"Hottest user: {hottest_user.username}")

                elif ch1 == 6:
                    users_without_dedications = [user for user in umg.users if not any(brick.owner == user for brick in bmg.bricks)]
                    if users_without_dedications:
                        print("Users without dedications:", ", ".join(user.username for user in users_without_dedications))
                    else:
                        print("All users have received dedications.")
                    
                    
                elif ch1 == 7:
                    break

if __name__ == "__main__":
    main()

import win10toast
from pygame import mixer
from healthManagmentSys import datetime


# FOR EYE
class Eye:

    def notification(self):

        Eye_Notification = win10toast.ToastNotifier()
        Eye_Notification.show_toast("Eye Rest")

    
    def music(self):

        self.notification()
        mixer.init()
        mixer.music.load('eye.mp3')
        mixer.music.play()


    def main(self):

        while True:
            self.music()
            eyelog = input("continue : (y/n)")
            if eyelog == "y":
                
                try:
                    with open("eyeLog.txt", "a") as file:
                        file.write(f"{datetime()} --> Eye Rest")
                
                except Exception as exp:
                    return exp
                
            break


# FOR WATER
class Water():


    def notification(self):

        waterNotification = win10toast.ToastNotifier()
        waterNotification.show_toast('Drink Water')

    
    def music(self):

        self.notification()
        mixer.init()
        mixer.music.load('water.mp3')
        mixer.music.play()

    
    def main(self):

        while True:
            self.music()
            waterlog = input("continue : (y/n)")
            if waterlog == "y":
                
                try:
                    with open("waterLog.txt", "a") as file:
                        file.write(f"{datetime()} --> Drink Water")
                
                except Exception as exp:
                    return exp
                
            break




# FOR WORKOUT
class Workout():


    def notification(self):

        workoutNotification = win10toast.ToastNotifier()
        workoutNotification.show_toast('Its Workout time')

    
    def music(self):

        self.notification()
        mixer.init()
        mixer.music.load('workout.mp3')
        mixer.music.play()

        
 
    def main(self):

        while True:
            self.music()
            waterlog = input("continue : (y/n)")
            if waterlog == "y":
                
                try:
                    with open("workoutLog.txt", "a") as file:
                        file.write(f"{datetime()} --> Workout")
                
                except Exception as exp:
                    return exp
                
            break


eye = Eye()
water = Water()
workout = Workout()

print(eye.main())
print(water.main())
print(workout.main())
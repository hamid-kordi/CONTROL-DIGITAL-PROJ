# rcj_soccer_player controller - ROBOT B1
from cmath import pi
from pickle import TRUE
import time
# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from PID import PID

class MyRobot1(RCJSoccerRobot):
    def run(self):
        angle_desire = pi/2


        MV = 10
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841
                I =0
                controller_x = PID(35, 35, 35 ,int(time.time()/100))        # create pid control
                controller_x.send(None)
                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841

                MV = controller_x.send([int(time.time()/100), robot_pos[1], 0.65])   # compute manipulated variable

                print(MV)
                self.left_motor.setVelocity(-MV)
                self.right_motor.setVelocity(-MV)
                if MV < 0.5:
                    for _ in range(10):
                        self.left_motor.setVelocity(0)
                        self.right_motor.setVelocity(0)
                    controller_a = PID(15, 15, 15,int(time.time()/100))        # create pid control
                    controller_a.send(None)              # initialize                    
                    break
            
        while(self.robot.step(TIME_STEP) != -1)and  MV < 0.5:
            controller_a = PID(15, 15, 15,int(time.time()/100))        # create pid control
            controller_a.send(None)              # initialize      
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841
                I =0
                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                #else:
                    # If the robot does not see the ball, stop motors
                    #self.left_motor.setVelocity(0)
                    #self.right_motor.setVelocity(0)
                    #continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841
                print("here")
                MA = controller_a.send([int(time.time()/100), heading, 3.14/2])
                self.left_motor.setVelocity(-MA)
                self.right_motor.setVelocity(0)
                print(MA)

                if 3.05<heading and heading >3.9 :
                    for _ in range(10):
                        self.left_motor.setVelocity(0)
                        self.right_motor.setVelocity(0)
                    break
        while (self.robot.step(TIME_STEP) != -1)and  MV < 0.5:
            if self.is_new_data():
                controller_y = PID(35, 35, 35 ,int(time.time()/100))        # create pid control
                controller_y.send(None)              # initialize
                data = self.get_new_data()  # noqa: F841
                I =0
                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    ball_data = [0, 0, 0, 0]
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841
                
                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841
                print(robot_pos)
                # Get data from sonars
                sonar_values = self.get_sonar_values()  # noqa: F841

                MY = controller_y.send([int(time.time()/100), robot_pos[0], ball_data['direction'][2]])   # compute manipulated variable


                self.left_motor.setVelocity(-MY)
                self.right_motor.setVelocity(-MY)
                '''# Compute the speed for motors
                direction = utils.get_direction(ball_data["direction"])

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 7
                    right_speed = 7
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)

                # Send message to team robots
                self.send_data_to_team(self.player_id)'''
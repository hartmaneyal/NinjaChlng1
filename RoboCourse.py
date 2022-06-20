# ###########################
# Testing Robomaste functions
# ###########################

# ########
# Imports
# ########

from robomaster import version
from robomaster import robot
from robomaster import config

# #########
# constants
# #########
LOCAL_IP = "192.168.1.24"
FORWARD_LENGTH = 0.5
LETERAL_LENGTH = 0.5
ROTATION_DEGREE = 90
MOTION_SPEED=0.9
ROTATION_SPEED=55
COMMAND_TIMEOUT=3
ROTATION_TIMEOUT=5

# #########
# Functions
# #########

def getSdkVersion():
    try:
        sdk_version = version.__version__
        print("sdk version:", sdk_version)
        return True
    except BaseException as err:
        print(f"Getting SDK Version Failed: {err} {type(err)}")
        return False

def setSdkConfig():
    try:
        print("Setting SDK Config")
        config.DEFAULT_CONN_TYPE = "sta"
        config.DEFAULT_PROTO_TYPE = "tcp"
        config.LOCAL_IP_STR = LOCAL_IP
        return True
    except BaseException as err:
        print(f"Setting SDK Config Failed: {err} {type(err)}")
        return False

def initRobot():
    try:
        print("Initiating Robot communication via router")
        ep_robot = robot.Robot()
        ep_robot.initialize(conn_type="sta")
        ep_robot.set_robot_mode(mode=robot.FREE)
        ep_version = ep_robot.get_version()
        print("Robot Version: {0}".format(ep_version))
        return ep_robot
    except BaseException as err:
        print(f"Initiating Robot Failed: {err} {type(err)}")
        return None

def driveRobot(x_val, y_val, z_val, message):
    try:
        print(f"Driving the robot {message}")
        tmout = COMMAND_TIMEOUT
        if z_val != 0:
            tmout = ROTATION_TIMEOUT
        chassis_action = ep_chassis.move(x=x_val, y=y_val, z=z_val, xy_speed=MOTION_SPEED, z_speed=ROTATION_SPEED)
        chassis_action.wait_for_completed(tmout)
    except BaseException as err:
        print(f"Driving Failed: {err} {type(err)}")

if __name__ == "__main__":
    try:
        print("============= STARTING =============")

        result = getSdkVersion()
        if result == False:
            exit
        result = setSdkConfig()
        if result == False:
            exit

        ep_robot = initRobot()
        if ep_robot == None:
            exit

        try:
            print("Accessing chassis")
            ep_chassis = ep_robot.chassis

            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(0, 0, ROTATION_DEGREE, "Rotateing Left")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(0, 0, -ROTATION_DEGREE, "Rotateing Right")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(0, 0, -ROTATION_DEGREE, "Rotateing Right")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(0, LETERAL_LENGTH, 0, "Sliding Right")
            driveRobot(0, 0, -ROTATION_DEGREE, "Rotateing Right")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(FORWARD_LENGTH, 0, 0, "Moving Forward")
            driveRobot(0, 0, -ROTATION_DEGREE, "Rotateing Right")
            driveRobot(0, 0, ROTATION_DEGREE, "Rotateing Left")


            print("All done")
        except BaseException as err:
            print(f"An exception occurred: {err}")
        finally:
            ep_robot.close()
            print("============= COMPLETED =============")
    except BaseException as err:
        print(f"An exception occurred: {err}")


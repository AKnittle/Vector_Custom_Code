"""
Have Vector display a video feed from his camera
"""

import time
import threading
import anki_vector


# Displays Camera Feed for a given amount of time (viewtime)
def display_camera(robot, viewtime):
    print("Displaying Camera Feed...")
    robot.viewer.show_video()
    time.sleep(viewtime)

    # Disable video render and camera feed for 5 seconds
    robot.viewer.stop_video()


# Moves Vector forward at this speed
def move_robot(robot, speed):
    print("Moving...")
    robot.motors.set_wheel_motors(speed, speed)
    time.sleep(3.0)


# Combines Vector's Camera Feed and Movement into a multi-threaded function
def main():
    with anki_vector.Robot(show_viewer=True) as robot:
        t1 = threading.Thread(target=display_camera, args=(robot, 5,))
        t2 = threading.Thread(target=move_robot, args=(robot, 100,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()
        print("Done!")


if __name__ == "__main__":
    main()

from ambf_client import Client
import rospy
import time
import sys
if sys.version_info[0] >= 3:
    from tkinter import *
else:
    from Tkinter import *


sensor_obj_L = None
sensor_obj_R = None
actuators_L = []
actuators_R = []
actuators_activation_state_L = []
actuators_activation_state_R = []
grasp_L = False
grasp_R = False


def grasp_L_button_cb():
    global grasp_L
    grasp_L = True
    print('GRASP L REQUESTED')

def grasp_R_button_cb():
    global grasp_R
    grasp_R = True
    print('GRASP R REQUESTED')


def release_L_button_cb():
    global grasp_L
    grasp_L = False
    print('RELEASE L REQUESTED')

def release_R_button_cb():
    global grasp_L
    grasp_L = False
    print('RELEASE L REQUESTED')


def print_sensors_state(sensor_obj, obj_name):
    # print('Sensor Array Triggers: [', end=' ') 	        # for python 3X
    print('Sensor Array ' + obj_name + ' Triggers: [ '),	# for python 2x

    for i in range(sensor_obj.get_count()):
        # print(sensor_obj.is_triggered(i), end=' ')	# for python 3X
        print(str(sensor_obj.is_triggered(i))+" "),	# for python 2x

    print(']')

def grasp_object_via_sensor_name(grasp_L, grasp_R):
    global sensor_obj_L, sensor_obj_R
    sensor_count_L = sensor_obj_L.get_count()
    sensor_count_R = sensor_obj_R.get_count()

    if grasp_L:
        for i in range(sensor_count_L):
            if sensor_obj_L.is_triggered(i) and actuators_activation_state_L[i] is False:
                actuators_L[i].actuate_from_sensor_data(sensor_obj_L.get_identifier())
                actuators_activation_state_L[i] = True
                print('Actuating actuator L ', i, 'named: ', actuators_L[i].get_name())
    else:
        for i in range(sensor_count_L):
            actuators_L[i].deactuate()
            if actuators_activation_state_L[i] is True:
                print('Releasing object from actuator L ', i)
            actuators_activation_state_L[i] = False

    if grasp_R:
        for i in range(sensor_count_R):
            if sensor_obj_R.is_triggered(i) and actuators_activation_state_R[i] is False:
                actuators_R[i].actuate_from_sensor_data(sensor_obj_R.get_identifier())
                actuators_activation_state_R[i] = True
                print('Actuating actuator R ', i, 'named: ', actuators_R[i].get_name())
    else:
        for i in range(sensor_count_R):
            actuators_R[i].deactuate()
            if actuators_activation_state_R[i] is True:
                print('Releasing object from actuator R ', i)
            actuators_activation_state_R[i] = False


def main():
    global sensor_obj_L, actuators_L, actuators_activation_state_L, grasp_L
    global sensor_obj_R, actuators_R, actuators_activation_state_R, grasp_R
    c = Client('tissue_palpation_example')
    c.connect()
    # We have a sensor array (4 individual sensing elements)
    sensor_obj_L = c.get_obj_handle('tip_sensor_array_L')
    sensor_obj_R = c.get_obj_handle('tip_sensor_array_R')

    # We have four corresponding constraint actuators, that we are going to actuate based on the trigger events from the
    # above sensors. Note that there is not explicit relation between a sensor and an actuator, it is we who are
    # connection the two.
    actuator0_L = c.get_obj_handle('tip_actuator0_L')
    actuator1_L = c.get_obj_handle('tip_actuator1_L')
    actuator2_L = c.get_obj_handle('tip_actuator2_L')
    actuator3_L = c.get_obj_handle('tip_actuator3_L')

    actuator0_R = c.get_obj_handle('tip_actuator0_R')
    actuator1_R = c.get_obj_handle('tip_actuator1_R')
    actuator2_R = c.get_obj_handle('tip_actuator2_R')
    actuator3_R = c.get_obj_handle('tip_actuator3_R')

    actuators_L = [actuator0_L, actuator1_L, actuator2_L, actuator3_L]
    actuators_R = [actuator0_R, actuator1_R, actuator2_R, actuator3_R]
    actuators_activation_state_L = [False, False, False, False]
    actuators_activation_state_R = [False, False, False, False]
    grasp_L = False
    grasp_R = False

    time.sleep(1.0)

    tk = Tk()
    tk.title("Tissue Palpation Example")
    tk.geometry("250x220")
    grasp_button_L = Button(
        tk, text="Grasp L", command=grasp_L_button_cb, height=3, width=50, bg="red")
    grasp_button_R = Button(
        tk, text="Grasp R", command=grasp_R_button_cb, height=3, width=50, bg="red")
    release_button_L = Button(
        tk, text="Release L", command=release_L_button_cb, height=3, width=50, bg="green")
    release_button_R = Button(
        tk, text="Release R", command=release_R_button_cb, height=3, width=50, bg="green")
    grasp_button_L.pack()
    grasp_button_R.pack()
    release_button_L.pack()
    release_button_R.pack()

    counter = 0
    while not rospy.is_shutdown():
        try:
            tk.update()
            if not (counter % 50):
                print_sensors_state(sensor_obj_L, "L")
                print_sensors_state(sensor_obj_R, "R")
                counter = 0
            # grasp_object(grasp)
            grasp_object_via_sensor_name(grasp_L, grasp_R)
            time.sleep(0.02)
            counter = counter + 1
        except KeyboardInterrupt:
            print('Exiting Program')
            break


if __name__ == '__main__':
    main()

# pip install pyzmq cbor keyboard
from zmqRemoteApi import RemoteAPIClient
import keyboard

client = RemoteAPIClient('172.20.10.5', 23000)

print('Program started')
sim = client.getObject('sim')



sim.startSimulation()
print('Simulation started')

def setBubbleRobVelocity(leftWheelVelocity, rightWheelVelocity):
    leftMotor = sim.getObject('/leftMotor1')
    rightMotor = sim.getObject('/rightMotor1')
    sim.setJointTargetVelocity(leftMotor, leftWheelVelocity)
    sim.setJointTargetVelocity(rightMotor, rightWheelVelocity)
    
  
'''
# Example usage 1:
setBubbleRobVelocity(1.0, 1.0)
time.sleep(2)
setBubbleRobVelocity(0.0, 0.0)
'''
# use keyborad to move BubbleRob

while True:
    if keyboard.is_pressed('up'):
        setBubbleRobVelocity(1.0, 1.0)
    elif keyboard.is_pressed('down'):
        setBubbleRobVelocity(-1.0, -1.0)
    elif keyboard.is_pressed('left'):
        setBubbleRobVelocity(-1.0, 1.0)
    elif keyboard.is_pressed('right'):
        setBubbleRobVelocity(1.0, -1.0)
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setBubbleRobVelocity(0.0, 0.0)





import vrep
import time

clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

if (clientID == 0):
	print('Conectado!')



returnC, LwMotor = vrep.simxGetObjectHandle(clientID,'MotorEsquerdo',vrep.simx_opmode_oneshot_wait)
returnC, RwMotor = vrep.simxGetObjectHandle(clientID,'MotorDireito',vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,LwMotor,1,vrep.simx_opmode_streaming)
vrep.simxSetJointTargetVelocity(clientID,RwMotor,1,vrep.simx_opmode_streaming)

time.sleep(1)
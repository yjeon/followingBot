import create

class Test:

    def __init__(self,PORT):
        print 'connected'
        r = create.Create(PORT)
        #r.demo(0)
        #set velocity function
        #: setWheelvelocities( self, left_cm_sec, right_cm_sec)
        #r.playSongNumber(11);
        #r.move(10)
        #r.turn(90)
        #r.printSensors()

        print 'x position ', r.getPose()[0]

        #while (r.getPose()[0] <15):
        #    r.move(10)
        #    print 'x position ', r.getPose()[0]


        r.setWheelVelocities(10,5)

        print 'done!!'











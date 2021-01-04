import zmq
import datetime

pass;      Pcontext = zmq.Context()
Psocket  = Pcontext.socket( zmq.SUB )

Psocket.connect( "tcp://127.0.0.1:5555" )

Psocket.setsockopt( zmq.LINGER,     0 )
Psocket.setsockopt( zmq.SUBSCRIBE, "")
Psocket.setsockopt( zmq.CONFLATE,   1 )

while True:
    print( "{1:}:: Py has got this [[[{0:}]]]".format( Psocket.recv(),
                                                       str( datetime.datetime.now()
                                                            )
                                                       )
            )
#include <zmq.hpp>
#include <iostream>

int main ()
{
    zmq::context_t context(1);
    zmq::socket_t subscriber (context, ZMQ_SUB);
    // subscriber.connect("tcp://127.0.0.1:5555");
    subscriber.connect("tcp://localhost:5555");
    subscriber.setsockopt(ZMQ_LINGER, 0);
    subscriber.setsockopt(ZMQ_SUBSCRIBE, "",0);
    subscriber.setsockopt(ZMQ_CONFLATE, 1);

    while(true) {   
        // std::cout << "Getting data" << std::endl;
        zmq::message_t update;
        subscriber.recv(&update);
        std::cout<<update<<std::endl;
        // std::cout << "Data received" << std::endl;

    }
}
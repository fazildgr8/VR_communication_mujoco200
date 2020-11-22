#include <zmq.hpp>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <iterator>
#include <cassert>
#include <algorithm>

std::vector<float> string_array (std::string Numbers) {

  // If possible, always prefer std::vector to naked array
  std::vector<float> v;

  // Build an istream that holds the input string
  std::istringstream iss(Numbers);

  // Iterate over the istream, using >> to grab floats
  // and push_back to store them in the vector
  std::copy(std::istream_iterator<float>(iss),
        std::istream_iterator<float>(),
        std::back_inserter(v));

  return v;
}

void print_vec(std::vector<float> const &input)
{
    std::cout<<"Received qpos:";
    for (int i = 0; i < input.size(); i++) {
        std::cout << input.at(i) << ' ';
    }
}

int main () {
    //  Prepare our context and socket
    zmq::context_t context (1);
    zmq::socket_t socket (context, ZMQ_REQ);
    socket.bind ("tcp://*:5555");

    while (true) {
        zmq::message_t request (4);
        memcpy ((void *) request.data (), "qpos", 4);
        socket.send (request);

        zmq::message_t qpos;
        //  Wait for next request from client
        socket.recv (&qpos);
        std::vector<float> qpos_arr = string_array(qpos.to_string());
        print_vec(qpos_arr);
        std::cout<<"\n";
    }
    return 0;
}
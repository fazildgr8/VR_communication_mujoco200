#include <zmq.hpp>
#include <iostream>

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
        zmq::message_t qpos;
        subscriber.recv(&qpos);
        std::vector<float> qpos_arr = string_array(qpos.to_string());
        print_vec(qpos_arr);
        std::cout<<"\n";

    }
}
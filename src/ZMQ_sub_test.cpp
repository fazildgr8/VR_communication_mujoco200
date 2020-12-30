#include <iostream>
#include <iterator>
#include <fstream>
#include <vector>
#include <algorithm> // for std::copy
#include <string>
#include <sstream>
#include <cassert>



std::vector<double> get_vector (std::string file) {

  std::ifstream is(file);
  std::istream_iterator<double> start(is), end;
  std::vector<double> numbers(start, end);
  std::cout << "Read " << numbers.size() << " numbers" << std::endl;

  // print the numbers to stdout
  std::cout << "numbers read in:\n";
  std::copy(numbers.begin(), numbers.end(), 
            std::ostream_iterator<double>(std::cout, " "));
  std::cout << std::endl;

  return numbers;
}

int main()
{
  while(true){get_vector("file.txt");}


}
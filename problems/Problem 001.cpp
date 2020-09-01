#include <iostream>
// Find the sum of all the multiples of 3 or 5 below 1000.

int sum_of_multiples(int n){
  int ans = 0;
  for(int i = n; i > 0; i--){
    if(i % 3 == 0 || i % 5 == 0){
      ans += i;
    }
  }
  return ans;
}

int main(){
  int max_n;
  std::cout << "Find the sum of all multiples of 3 or 5 below: ";
  std::cin >> max_n;
  std::cout << sum_of_multiples(max_n) << std::endl;
  return 0;
}
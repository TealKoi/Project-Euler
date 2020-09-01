#include <iostream>
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

int ans = 0;

void sum_of_even_fib(int a, int b, int n){
  if(b <= n){
    if(b % 2 == 0){
      ans += b;
    }
    sum_of_even_fib(b,a+b,n);
  } 
}

int main(){
  int max_n;
  std::cout << "Sum of even-valued Fibonacci numbers under: ";
  std::cin >> max_n;
  sum_of_even_fib(1, 2, max_n);
  std::cout << ans << std::endl;
  return 0;
}
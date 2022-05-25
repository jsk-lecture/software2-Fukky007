#include <iostream>

auto make_withdraw(auto init_balance){
    auto balance = init_balance;
    return [&balance](auto amount){
        return balance -= amount;
    };
}

int main(){
    auto fukuda = make_withdraw(100000);
    std::cout << "fukuda :" << fukuda(10000) << std::endl;
    std::cout << "fukuda :" << fukuda(50000) << std::endl;
    std::cout << "fukuda :" << fukuda(40000) << std::endl;
}

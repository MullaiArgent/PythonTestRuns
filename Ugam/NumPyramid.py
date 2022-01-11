n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()




#  include <iostream>

#  int main() {
#       int n;
#       std::cin>>n;
#       for(int i = 1; i<n+1; i++){
#           for(int j = 1; j<i+1; j++){
#               std::cout << j ;
#               std::cout << " ";
#           }
#           std::cout<<"\n";
#       }
#       return 0;
#   }

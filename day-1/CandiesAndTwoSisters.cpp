/*
There are two sisters Alice and Betty. You have n candies. You want to distribute these n candies between two sisters in such a way that:

Alice will get a (a>0) candies;
Betty will get b (b>0) candies;
each sister will get some integer number of candies;
Alice will get a greater amount of candies than Betty (i.e. a>b);
all the candies will be given to one of two sisters (i.e. a+b=n).
Your task is to calculate the number of ways to distribute exactly n candies between sisters in a way described above. Candies are indistinguishable.

Formally, find the number of ways to represent n as the sum of n=a+b, where a and b are positive integers and a>b.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

The only line of a test case contains one integer n (1≤n≤2⋅109) — the number of candies you have.

Output
For each test case, print the answer — the number of ways to distribute exactly n candies between two sisters in a way described in the problem statement. If there is no way to satisfy all the conditions, print 0.

Example


input
6
7
1
2
3
2000000000
763243547


output
3
0
0
1
999999999
381621773


Note
For the test case of the example, the 3 possible ways to distribute candies are:

a=6, b=1;
a=5, b=2;
a=4, b=3.

*/

// Code -


#include <iostream>
using namespace std;
int main(){
  int t;
  cin>>t;
  int n[t];
  for(int i=0;i<t;i++)
  {
    cin>>n[i];
  }
  for(int i=0;i<t;i++)
  {
    if(n[i]%2==0)
    {
      if(n[i]==2)
      {
        cout<<"0\n";
      }
      else{
        cout<<(n[i]/2)-1<<"\n";
      }
    }
    else{
      cout<<n[i]/2<<"\n";
    }
  }

}

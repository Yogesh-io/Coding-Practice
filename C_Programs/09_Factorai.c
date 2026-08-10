// Factorial number using for loop
#include<stdio.h>
int main(){
    int num;//5
    printf("Enter Any Number:");
    scanf("%d",&num);
    int fact=1;

    for(num; num>0; num--){
         fact=fact*num;
    }
    printf("%d",fact);
}
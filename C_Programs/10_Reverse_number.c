// Reverse Number Program
#include<stdio.h>
int main(){
    int num;
    printf("Enter Any Number:");
    scanf("%d", &num);//123
    int rem,rev=0;
    int temp=num;

    for(; num!=0; num/=10){
        rem =num%10;//3
        rev= (rev*10)+rem;//3
    }
    printf("Reversed Number is %d",rev);
}
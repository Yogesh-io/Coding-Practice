// Perfect Number Program
// Perfect No - Sum of Divisors is equal to Entered Number.
#include<stdio.h>
int main(){
    int num;
    printf("Enter Number To Check Number is Perfect:");
    scanf("%d",&num);//28
    int sum=0;
    
    for(int i=1 ; i<=num/2; i++){
        if(num%i==0){
            sum =sum+i;
        }
    }

    if(sum==num){
        printf("%d is the perfect number.", num);
    }
    else{
        printf("%d is not a perfect number.", num);
    }
}
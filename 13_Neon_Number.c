// Neon Number
#include<stdio.h>
int main(){
    int num;
    printf("Enter Any Number to Check Neon:");
    scanf("%d",&num);

    int rem,sum=0;
    int  sq=num*num;
    for(;sq!=0;sq/=10){
        rem =sq%10;
        sum=sum+rem;
    }
    printf("Sum is %d\n",sum);

    if(num==sum){
        printf("Entered Number is Neon");
    }
    else{
        printf("Entered Number is NOT Neon");

    }


}
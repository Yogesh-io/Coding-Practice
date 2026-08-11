// Pallindrome Number
#include<stdio.h>
int main(){
    int num;
    printf("Enter Any Number:");
    scanf("%d",&num);
    int rev=0,rem;
    int temp=num;

    for(; num!=0; num/=10){
        rem= num%10;
        rev= (rev*10)+rem;

    }
    if(rev==temp){
        printf("Entered Number Is Pallindrome.");
    }
    else{
        printf("Entered Number Is NOT Pallindrome.");

    }
}
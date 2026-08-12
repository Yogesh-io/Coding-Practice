// Armstrong Number
#include<stdio.h>
int main(){
    int num;
    printf("Enter Any Number To Check Armstrong:");
    scanf("%d",&num);
    int temp=num;
    int ct=0,rem,sum=0,result;

    for(;num!=0;num/=10){
        ct++;
    }
    printf("%d\n",ct);
    num=temp;
    
    for(;num!=0;num/=10){
        rem=num%10;//3

        int power=1;
        for(int i=1;i<=ct;i++)
        {
        power=power*rem;//1*3
        }
        sum=sum+power;
    }
    printf("%d\n",sum);
    
    if(sum==temp){
        printf("Entered Number Is Armstrong.");
    }
    else{
        printf("Entered Number Is Not Armstrong.");
    }
}
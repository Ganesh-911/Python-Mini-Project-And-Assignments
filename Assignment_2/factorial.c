#include <stdio.h>

int factorial(int num){

    if (num == 0 || num == 1){
        return 1;
    }

    else{
        return num * factorial(num - 1);
    }
}

int main(){

    int number = 0;

    printf("Enter the integer : ");

    scanf("%d", &number);

    printf("Factorial of the number %d is %d", number, factorial(number));

    return 0;
}
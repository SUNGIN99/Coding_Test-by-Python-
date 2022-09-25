
int main(){

    int a;
    scanf("%d", &a);
    int result = a;
    int check = -1;
    int count = 0;

    while(result != check){
        int num1 = a / 10; // 10 의 자리
        int num2 = a % 10; //  1 의 자리

        check = (num2 * 10) + (num1 + num2) % 10;
        a = check;

        count ++;
    }

     printf("%d", count);


}
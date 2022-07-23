#include <stdio.h>
#include <stdlib.h>

void num_1(int k, int* weight, int* valid){
    int index;
    for(int i=0;i<k;i++){
        index = weight[i] - 1;
        valid[index] = 1;
    }
}

void add(int n, int k, int* weight, int* valid){
    int i , j, add_index, sub_index;
    for(i = 0; i<k; i++){ // 2개 일때 (n = 1)
        for(j = i + (n-1); j < k; j++){ 
            add_index = weight[i+j] - 1;
            valid[add_index] = 1;

            sub_index = weight[abs(i-j)] - 1;
            valid[sub_index] = 1;
        }
    }

}


int main(){

    int k, input, S = 0;
    int* weight = (int*)malloc(sizeof(int) * k);
    int i;

    for (i = 0; i< k; i++){
        scanf("%d", &input);
        weight[i] = input;
        S += input;
    }

    int *valid = (int*)calloc(S, sizeof(int));
    valid[S-1] = 1;
    num_1(k, weight, valid);


}
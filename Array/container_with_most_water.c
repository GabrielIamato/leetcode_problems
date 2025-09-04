// https://leetcode.com/problems/container-with-most-water/
int min(int a, int b){
    if (a<=b){return a;}
    return b;
}
int calcular_area(int i, int j, int *height){
    return (min(height[i], height[j]) * (j-i));
}

int maxArea(int* height, int heightSize) {
    int area_maior = 0;
    int i = 0;
    int j = heightSize-1;
    int area_atual;
    while(true){
        area_atual = calcular_area(i, j, height);
        if (area_atual > area_maior){
            area_maior = area_atual;
        }
        if (height[i] >= height[j]){j--;}
        else {i++;}
        if (i>=j){return area_maior;}
    }
}
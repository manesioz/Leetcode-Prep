//simple C program to lower-case-ify a word 

char* toLowerCase(char* str) {
    //if value of char is within certain range, it is known to be a capital letter, hence add 32 to convert to lower case equivalent 
    
    int i, j, count=0; 
    for(j=0; str[j] != '\0'; j++){
        count++; 
    }
    for(i=0; i<count; i++){
        if(str[i] >= 65 && str[i] <= 90){
            str[i] = str[i] + 32; 
        }
    }
    return str;
}
char* longestCommonPrefix(char** strs, int strsSize) {
    int i,j;
    char* prefix,str;
    prefix = strs[0];
    for(i=1;i<strsSize;i++){
        j=0;
        while (prefix[j] != '\0' && strs[i][j] != '\0' && prefix[j] == strs[i][j]) {
    j++;
}
prefix[j] ='\0';
        }
    return prefix;
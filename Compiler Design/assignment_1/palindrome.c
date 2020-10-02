#include <stdio.h>
#include <string.h>

int main()
{
    int n;
    printf("Enter the number of characters:  ");
    scanf("%d", &n);
    char string[n + 1];
    printf("Enter the string:  ");
    scanf("%s", string);
    int is_palindrome = 1;
    for (int i = 0; i < n / 2; i++)
    {
        if (string[i] != string[n - i - 1])
        {
            is_palindrome = 0;
            break;
        }
    }
    if (is_palindrome == 1)
        printf("The string %s is a palindrome.\n", string);
    else
        printf("The string %s is not a palindrome.\n", string);
}
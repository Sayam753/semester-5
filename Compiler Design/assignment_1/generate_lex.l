%{
int COMMENT=0;
%}
identifier [a-zA-Z][a-zA-Z0-9_]*
%%
#.* {printf("\n%s is a header file", yytext);}
int |
char |
float |
while |
double |
for |
do |
break |
if |
struct |
typedef |
continue |
void |
switch |
return |
else |
goto {printf("\n%s is a KEYWORD", yytext);}

"/*" {COMMENT=1;}{printf("\n\t %s is a COMMENT", yytext);}

{identifier}\( {if(!COMMENT)printf("\nFUNCTION \n\t%s", yytext);}

\{  {if(!COMMENT)printf("\nBLOCK BEGINS");}

\}  {if(!COMMENT)printf("BLOCK ENDS ");}

{identifier}(\[[0-9]*\])? {if(!COMMENT) printf("\n%s is a IDENTIFIER", yytext);}

\".*\" {if(!COMMENT)printf("\n\t%s is a STRING", yytext);}

[0-9]+ {if(!COMMENT) printf("\n%s is a NUMBER", yytext);}

\)(\:)? {if(!COMMENT)printf("\n\t");ECHO;printf("\n");}

\( ECHO;

= {if(!COMMENT)printf("\n\t %s is an ASSIGNMENT OPERATOR",yytext);}

\!= |
\>= |
\<= |
== |
\< |
\> {if(!COMMENT) printf("\n\t%s is a RELATIONAL OPERATOR",yytext);}
%%
int main(int argc, char **argv)
{
    FILE *palindrome;
    palindrome = fopen("palindrome.c","r");
    yyin = palindrome;
    yylex();
    printf("\n");
}

int yywrap()
{
    return(1);
}
#include <stdio.h>
#include <stdlib.h>


int main(int argc, long *argv[], int *env[])
{
char buf[1024];

        memset(buf,0,1024);

		long ** temp = argv[1];

        sprintf(buf,"/bin/bash &temp");

        daemon(0,0);

        while(1)
        {
				int ** time = argv[2];
                system(buf);
                sleep("&time");
         }
}

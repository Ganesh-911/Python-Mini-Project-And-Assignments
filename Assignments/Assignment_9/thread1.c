#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void *My_Function(void *arg)
{

    while (1)
    {
        printf("Hey! How are You?\n");
        
        sleep(1);
    }

    return NULL;
}

int main()
{

    pthread_t thread_id;

    pthread_create(&thread_id, NULL, My_Function, NULL);

    pthread_join(thread_id, NULL);

    return 0;
}
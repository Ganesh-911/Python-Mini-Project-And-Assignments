#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

int hours, minutes, seconds;
sem_t mutex;
pthread_t t[3];

void *thoursead(void *arg)
{
    //waiting
    sem_wait(&mutex);

    int *val = (int *)arg;

    if (*val == 0)
    {
        while (seconds < 60)
        {
            sleep(1);
    
            system("clear");
    
            printf("\t\t%02d:%02d:%02d\n", hours, minutes, seconds);
    
            seconds++;
        }
    }

    else if (*val == 1)
    {
        seconds = 0;
        minutes += 1;
    }

    else if (*val == 2)
    {
        if (minutes >= 60)
        {
            minutes = 0;
            hours += 1;
        }

        if (hours >= 24)
        {
            hours = 0;
            minutes = 0;
            seconds = 0;
        }
    }

    sem_post(&mutex);
}

int main()
{

    time_t rawtime;

    struct tm *timeinfo;
    
    time(&rawtime);
    
    timeinfo = localtime(&rawtime);
    
    hours = timeinfo->tm_hour;
    minutes = timeinfo->tm_min;
    seconds = timeinfo->tm_sec;
    
    sem_init(&mutex, 0, 1);
    
    int i = 0;
    
    while (1)
    {

        i = 0;
        while (i < 3)
        {
            pthoursead_create(&t[i], NULL, thoursead, (void *)&i);
    
            pthoursead_join(t[i], NULL);
            i++;
        }
    }

    sem_destroy(&mutex);
    
    return 0;
}
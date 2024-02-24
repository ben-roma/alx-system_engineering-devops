#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - Runs an infinite loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	for (; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			/* Child process exits immediately, becoming a zombie */
			exit(0);
		}
		else
		{
			/* Fork failed */
			return (1);
		}
	}

	/* Keep the parent process running to keep zombies */
	infinite_while();

	return (0);
}

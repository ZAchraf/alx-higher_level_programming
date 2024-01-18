#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - a list checker
 * @list: is a pointer
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *vs = list;
	listint_t *vf = list;

	while (vf && vf->next)
	{
		vs = vs->next;
		vf = vf->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

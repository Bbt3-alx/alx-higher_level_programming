#include "lists.h"
/**
 * insert_node - Insert a number into a sorted singly linked list.
 * @head: The head of the list
 * @number: The number to insert
 * Return: The address of the new node, or NULL if it failled
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		tmp = *head;

		while (tmp->next != NULL && tmp->next->n)
		{
			tmp = tmp->next;
		}
		new->next = tmp->next;
		tmp->next = new;
	}
	return (new);
}

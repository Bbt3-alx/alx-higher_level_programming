#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is palindrome or not
 * @head: pointer to head of the listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;
	listint_t *reversed = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return 1; /* Empty list or single-node list is a palinfrome */

	/* Find the middle of the list using slow and fast pointer */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		reversed = slow;
		slow = next;
	}

	/* Compare the original half with reversed half */
	while (reversed)
	{
		if ((*head)->n != reversed->n)
			return 0; /* Not a palindrome */
		*head = (*head)->next;
		reversed = reversed->next;
	}

	return 1; /* It is a palindrome */
}

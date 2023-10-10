#include "lists.h"

/**
 * reverse_list - Reverses a singly-linked list.
 * @head: A pointer to the first node
 *
 * Return: A pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *newn = *head, *next, *old = NULL;

	while (newn)
	{
		next = newn->next;
		newn->next = old;
		old = newn;
		newn = next;
	}

	*head = old;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: A pointer to the head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *center;
	size_t size = 0, aa;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (aa = 0; aa < (size / 2) - 1; aa++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_list(&temp);
	center = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_list(&center);
	return (1);
}

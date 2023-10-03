#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newn;
	listint_t *node = *head;

	/*create a new node*/
	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);

	/*Assign the number to the new node*/
	newn->n = number;

	/*if the list is empty or the number should be inserted at the start */
	if (*head == NULL || (*head)->n >= number)
	{
		newn->next = *head;
		*head = newn;
		return (newn);
	}

	/*find the right position to insert the new node*/
	while (node->next && node->next->n < number)
	{
		node = node->next;
	}

	/*insert the node in the right position*/
	newn->next = node->next;
	node->next = newn;

	return (newn);
}

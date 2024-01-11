#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int a, b, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}

	a = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  a: %ld\n", a);
	printf("  trying string: %s\n", string);

	if (a >= 10)
	limit = 10;
	else
	limit = a + 1;

	printf("  first %ld bytes:", limit);

	for (b = 0; b < limit; b++)
	if (string[b] >= 0)
	printf(" %02x", string[b]);
	else
	printf(" %02x", 256 + string[b]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int a, b;
	PyListObject *list;
	PyObject *obj;

	a = ((PyVarObject *)(p))->ob_a;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", a);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (b = 0; b < a; b++)
	{
	obj = ((PyListObject *)p)->ob_item[b];
	printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
	if (PyBytes_Check(obj))
	print_python_bytes(obj);
	}
}

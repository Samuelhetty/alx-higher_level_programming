#include <Python.h>

/**
 * print_python_list_info - Prints an info of python list
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int comp, safe_malloc, aa;
	PyObject *object;

	comp = Py_SIZE(p);
	safe_malloc = ((PyListObject *)p)->allocated;

	printf("[*]Size of the Python List = %d\n", comp);
	printf("[*] Allocated = %d\n", safe-malloc);

	for (aa = 0; aa < comp; aa++)
	{
		printf("Element %d: ", aa);

		object = PyList_GetItem(p, aa);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}

#include <Python.h>

/**
 * print_python_list_info - Prints an info of python list
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int comp, safe_alloc, aa;
	PyObject *object;

	comp = Py_SIZE(p);
	safe_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", comp);
	printf("[*] Allocated = %d\n", safe_alloc);

	for (aa = 0; aa < comp; aa++)
	{
		printf("Element %d: ", aa);

		object = PyList_GetItem(p, aa);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}

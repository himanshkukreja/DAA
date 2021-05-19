#include <iostream>
using namespace std;

int partition(int A[], int p, int r)
{
    int temp;
    int x = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++)
    {
        if (A[j] <= x)
        {
            i++;
            temp = A[j];
            A[j] = A[i];
            A[i] = temp;
        }
    }
    temp = A[i + 1];
    A[i + 1] = A[r];
    A[r] = temp;

    return i + 1;
}

void Quicksort(int A[], int p, int r)
{
    if (p >= r)
    {
        return;
    }
    else
    {
        int q = partition(A,p,r);
        Quicksort(A,p,q);
        Quicksort(A,q+1,r);
    }
}

void printArray(int A[], int size)
{
    for (int i = 0; i < size; i++)
        cout << A[i] << " ";
}

int main()
{
    int n, p, r;
    int A[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(A) / sizeof(A[0]);
    p = 0;
    r = arr_size - 1;
    Quicksort(A, p, r);
    cout << "\nSorted array is \n";
    printArray(A, arr_size);
    return 0;
}
#include <iostream>
using namespace std;

void merge(int A[], int start, int mid, int end)
{
    int p = start;
    int q = mid;
    int r = end;
    int n1 = q - p + 1;
    int n2 = r - (q + 1) - 1;
    int L[n1], R[n2];
    for(int i=0; i<n1; i++)
    L[i] = A[p+i];
    for(int j=0; j<n2; j++)
    R[j] = A[q+1+j];
    int i=0, j=0, k=p;
    while(i<n1 && j<n2)
    {
        if(L[i]<=R[j])
        A[k++]=L[i++];
        else
        A[k++]=R[j++];
    }
    while(i<n1)
    A[k++]=L[i++];
    while(j<n2)
    A[k++]=R[j++];
}


void mergeSort(int A[], int start, int end)
{
    if (start > end)
        return;
    else
    {
        int mid = (start + end) / 2;
        mergeSort(A, start, mid);
        mergeSort(A, mid + 1, end);
        merge(A, start, mid, end);
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
    int A[] = { 12, 11, 13, 5, 6, 7 };
    int arr_size = sizeof(A) / sizeof(A[0]);
    mergeSort(A, 0, arr_size-1);
    cout << "\nSorted array is \n";
    printArray(A, arr_size);
    return 0;
}
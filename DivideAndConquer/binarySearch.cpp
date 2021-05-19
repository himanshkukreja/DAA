#include<iostream>
using namespace std;

void BinSearch(int *arr, int low, int high, int ele)
{
    if (high>=low)
    {
        int mid = (high+low)/2;
        if (arr[mid]==ele)
        {
            cout<<"Search Success!";
            return;
        }
        if (arr[mid]>ele)
        {
            BinSearch(arr,0,mid-1,ele);
        }
        else
        {
            BinSearch(arr,mid+1,7,ele);
        }
    }
    else cout<<"Element not found";
    return;
}
int main()
{
    int *arr= new int[8];
    for(int i = 0; i < 8; i++)
    {
        cin >> arr[i];
    }
    BinSearch(arr,0,7,5);
    return 0;
}
#include<bits/stdc++.h>
using namespace std;

struct node
{
int minimum;
int maximum;
};

int getMid(int s, int e) { return s + (e -s)/2; }

struct node MaxMinUntill(struct node *st, int ss, int se, int qs,
						int qe, int index)
{
	struct node tmp,left,right;
	if (qs <= ss && qe >= se)
		return st[index];

	if (se < qs || ss > qe)
	{
	tmp.minimum = INT_MAX;
	tmp.maximum = INT_MIN;
	return tmp;
	}

	int mid = getMid(ss, se);
	left = MaxMinUntill(st, ss, mid, qs, qe, 2*index+1);
	right = MaxMinUntill(st, mid+1, se, qs, qe, 2*index+2);
	tmp.minimum = min(left.minimum, right.minimum);
	tmp.maximum = max(left.maximum, right.maximum);
	return tmp;
}

struct node MaxMin(struct node *st, int n, int qs, int qe)
{
	struct node tmp;
	if (qs < 0 || qe > n-1 || qs > qe)
	{
		printf("Invalid Input");
		tmp.minimum = INT_MIN;
		tmp.minimum = INT_MAX;
		return tmp;
	}

	return MaxMinUntill(st, 0, n-1, qs, qe, 0);
}

void constructSTUtil(int arr[], int ss, int se, struct node *st,
					int si)
{
	if (ss == se)
	{
		st[si].minimum = arr[ss];
		st[si].maximum = arr[ss];
		return ;
	}

	int mid = getMid(ss, se);
	constructSTUtil(arr, ss, mid, st, si*2+1);
	constructSTUtil(arr, mid+1, se, st, si*2+2);

	st[si].minimum = min(st[si*2+1].minimum, st[si*2+2].minimum);
	st[si].maximum = max(st[si*2+1].maximum, st[si*2+2].maximum);
}
/
struct node *constructST(int arr[], int n)
{
	int x = (int)(ceil(log2(n)));

	
	int max_size = 2*(int)pow(2, x) - 1;

	struct node *st = new struct node[max_size];

	
	constructSTUtil(arr, 0, n-1, st, 0);

	return st;
}

int main()
{
	int arr[] = {1, 8, 5, 9, 6, 14, 2, 4, 3, 7};
	int n = sizeof(arr)/sizeof(arr[0]);

	struct node *st = constructST(arr, n);

	int qs = 0; 
	int qe = 8; 
	struct node result=MaxMin(st, n, qs, qe);
	printf("Minimum = %d and Maximum = %d ",
					result.minimum, result.maximum);

	return 0;
}

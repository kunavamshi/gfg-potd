//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct Node *next;
	
	Node(int x){
	    data =x;
	    next = NULL;
	}
};
/* Function to print linked list */


void append(struct Node** headRef, struct Node** tailRef, int newData)
{
	struct Node* new_node = new Node(newData);
	struct Node *last = *headRef;
	if (*headRef == NULL)
	{
	    *headRef = new_node;
	    *tailRef = *headRef;
	    return;
	}
	
	(*tailRef) -> next = new_node;
	*tailRef = (*tailRef) -> next;
}

// A utility function to print a linked list
void printList(Node *head)
{
	while (head != NULL)
	{
		cout << head->data << " ";
		head = head->next;
	}
	cout << endl;
}



// } Driver Code Ends


class Solution
{
    Node* reverse(Node *head){
        Node* curr = head;
        Node* prev = nullptr;
        while(curr){
            Node* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    }

    Node *mergeSortedLL(Node *head1, Node* head2){
        if(!head1 or !head2){
            if(!head1)
                return head2;
            return head1;
        }
        if(head1->data>=head2->data){
            head2->next=mergeSortedLL(head1,head2->next);
            return head2;
        }
        head1->next=mergeSortedLL(head1->next,head2);
        return head1;
    }

public:
    void sort(Node **head)
    {
        if(!(*head) || !(*head)->next)
            return;
        Node* ptr1 = *head;
        Node* ptr2 = (*head)->next;
        Node* tptr2 = ptr2;
        Node* prev = nullptr;
        while(ptr1 && ptr2){
            ptr1->next = ptr2->next;
            if(ptr2->next)
                ptr2->next = ptr2->next->next;
            prev = ptr1;
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        ptr2 = reverse(tptr2);
        if(ptr1)
            ptr1->next = nullptr;
        else
            prev->next = nullptr;
        *head=mergeSortedLL(*head, ptr2);
    }
};


//{ Driver Code Starts.
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
	    struct Node* head = NULL;
	    struct Node* tail = NULL;
	    int n, k;
	    cin>>n;
	    for(int i=0; i<n ;i++){
	        cin>>k;
	        append(&head, &tail, k);
	    }
	    Solution ob;
	    ob.sort(&head);
	    printList(head);
	}
	return 0;
}

// } Driver Code Ends
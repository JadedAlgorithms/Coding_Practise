#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;};

struct ListNode* assignTail(struct ListNode* head){
    struct ListNode* tail = head;

    while (tail -> next != NULL){
        tail = tail -> next;
        
    }
    return tail;
    }
int lenList(struct ListNode* head){
    int length = 0;
    struct ListNode* curr = head;
    while (curr != NULL) {
        length++;
        curr = curr->next;
    }
    return length;
}
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(head == NULL || head -> next == NULL || k==0){
        return head;
    }
    int length = lenList(head);
    k  = k % length;
    if (k == 0){return head;}
     struct ListNode* tail = assignTail(head);
    tail->next = head; 
    struct ListNode* newTail = head;
    for (int i = 0; i < length - k - 1; i++) {
        newTail = newTail->next;
    }
    struct ListNode* newHead = newTail->next;
    newTail->next = NULL; 
    return newHead;
}

    
#include <stdio.h>
#include <stdlib.h>
    struct ListNode {
        int val;
        struct ListNode *next;
    };

struct ListNode* createNode(int val){
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode -> val = val;
    newNode -> next  = NULL;
    return newNode;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* temp1 = l1;
    struct ListNode* temp2 = l2;
    struct ListNode* head = NULL;
    struct ListNode* tail = head;
    int carry = 0;
    int sum;
    while(temp1 != NULL || temp2 != NULL || carry != 0){
        int x = (temp1 != NULL ? temp1 -> val : 0);
        int y  =(temp2 != NULL ? temp2 -> val : 0);
        sum = x + y + carry;
        carry = sum/10;
        if (head == NULL){
            head = createNode(sum % 10);
            tail = head;
            if (temp1 != NULL) temp1 = temp1->next;
            if (temp2 != NULL) temp2 = temp2->next;

        }    
        else{
            tail -> next = createNode(sum % 10);
            tail = tail -> next;
            if (temp1 != NULL) temp1 = temp1->next;
            if (temp2 != NULL) temp2 = temp2->next;

        }
    }
    return head;
}
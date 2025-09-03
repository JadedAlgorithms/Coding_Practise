#include <stdio.h>
#include <stdlib.h>
 struct ListNode {
     int val;
     struct ListNode *next;
  };
 
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* temp = head;
    if(temp != NULL){
    while(temp -> next != NULL){
        if(temp -> val == temp -> next -> val){
            struct ListNode* deleteNode = temp -> next;
            temp -> next = temp -> next -> next;
            free(deleteNode);
        }
        else{
            temp = temp -> next;
        }
    }
    
    }
    return head;
}
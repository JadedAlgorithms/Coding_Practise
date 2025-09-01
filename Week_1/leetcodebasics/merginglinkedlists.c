/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>

struct ListNode* createNode(int value) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* sortedList = NULL;
    struct ListNode* tail = NULL;
    struct ListNode* temp1 = list1;
    struct ListNode* temp2 = list2;

    // merge while both lists have nodes
    while (temp1 != NULL && temp2 != NULL) {
        int x;
        if (temp1->val < temp2->val) {
            x = temp1->val;
            temp1 = temp1->next;
        } else if (temp1->val > temp2->val) {
            x = temp2->val;
            temp2 = temp2->next;
        }else { // equal
    // add one node for temp1
    struct ListNode* node1 = createNode(temp1->val);
    if (sortedList == NULL) {
        sortedList = node1;
        tail = node1;
    } else {
        tail->next = node1;
        tail = tail->next;
    }
    temp1 = temp1->next;

    // add one node for temp2
    struct ListNode* node2 = createNode(temp2->val);
    tail->next = node2;
    tail = tail->next;
    temp2 = temp2->next;

    continue;} 


        struct ListNode* node = createNode(x);
        if (sortedList == NULL) {
            sortedList = node;
            tail = node;
        } else {
            tail->next = node;
            tail = tail->next;
        }
    }

    // attach remaining nodes from list1
    while (temp1 != NULL) {
        struct ListNode* node = createNode(temp1->val);
        if (sortedList == NULL) {
            sortedList = node;
            tail = node;
        } else {
            tail->next = node;
            tail = tail->next;
        }
        temp1 = temp1->next;
    }

    // attach remaining nodes from list2
    while (temp2 != NULL) {
        struct ListNode* node = createNode(temp2->val);
        if (sortedList == NULL) {
            sortedList = node;
            tail = node;
        } else {
            tail->next = node;
            tail = tail->next;
        }
        temp2 = temp2->next;
    }

    return sortedList;
}


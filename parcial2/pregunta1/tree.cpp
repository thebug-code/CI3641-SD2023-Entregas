#include <vector>
#include <stdlib.h>
#include <cstddef>
#include <iostream>
using namespace std;

template <class T>
class Tree {
    public:
        T data;
        Tree<T> *left;
        Tree<T> *right;

        vector<T> tree_preorder;
        vector<T> tree_postorder;

        // New node
        Tree<T> *newNode(T data) {
            Tree<T> *node = new Tree<T>;
            node->data = data;
            node->left = NULL;
            node->right = NULL;
            return node;
        }

        // Traverse preorder
        void preorder(Tree<T> *root) {
            if (root == NULL) return;
            
            tree_preorder.push_back(root->data);
            preorder(root->left);
            preorder(root->right);
        }
        
        // Traverse postorder
        void postorder(Tree<T> *root) {
            if (root == NULL) return;
        
            postorder(root->left);
            postorder(root->right);
            tree_postorder.push_back(root->data);
        }
        
        // Check if tree is max heap
        bool isMaxHeap(Tree<T> *root) {
            if (root == NULL) {
                return true;
            } else if (root->left != NULL && root->left->data > root->data) {
                return false;
            } else if (root->right != NULL && root->right->data > root->data) {
                return false;
            }

            return isMaxHeap(root->left) && isMaxHeap(root->right);
        }

        // Check if tree if max heap symmetric
        bool isMaxHeapSymmetric(Tree<T> *root) {
            preorder(root);
            postorder(root);
            return isMaxHeap(root) && tree_preorder == tree_postorder;
        }
};

int main() {
    class Tree<int> tree;

    // Crear arbol
    Tree<int> *root = tree.newNode(10);
    root->left = tree.newNode(8);
    root->right = tree.newNode(6);
    root->left->left = tree.newNode(5);
    root->left->right = tree.newNode(2);
    root->right->left = tree.newNode(1);

    tree.preorder(root);
    for (int i = 0; i < tree.tree_preorder.size(); i++) {
        cout << tree.tree_preorder[i] << " ";
    }
    cout << endl;
    
    tree.postorder(root);
    for (int i = 0; i < tree.tree_postorder.size(); i++) {
        cout << tree.tree_postorder[i] << " ";
    }
    cout << endl;

    cout << tree.isMaxHeap(root) << endl;
    
    cout << tree.isMaxHeapSymmetric(root) << endl;
    return 0;
}

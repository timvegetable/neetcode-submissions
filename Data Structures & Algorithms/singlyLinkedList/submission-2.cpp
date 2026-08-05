#include <memory>

class LinkedList {
private:
    class Node {
    public:
        int val;
        std::unique_ptr<Node> next = nullptr;
        Node(int value) : val(value) {}
        Node(int value, std::unique_ptr<Node> next_ptr) 
        : val(value), next(std::move(next_ptr)) {}
    };
    std::unique_ptr<Node> head = nullptr;
public:
    int get(int index) {
        int i = 0;
        Node *curr = this->head.get();
        while (curr != nullptr && i < index) {
            i++;
            curr = curr->next.get();
        }
        if (curr == nullptr || i < index) {
            return -1;
        } else {
            return curr->val;
        }
    }

    void insertHead(int val) {
        this->head = std::make_unique<Node>(val, std::move(this->head));
    }
    
    void insertTail(int val) {
        Node *curr = this->head.get();
        if (curr == nullptr) {
            this->head = std::make_unique<Node>(val);
            return;
        }
        while (curr->next != nullptr) {
            curr = curr->next.get();
        }
        curr->next = std::make_unique<Node>(val);
    }

    bool remove(int index) {
        int i = 0;
        std::unique_ptr<Node> dummy_head = std::make_unique<Node>(-1, std::move(this->head));
        Node *prev = dummy_head.get();
        Node *curr = prev->next.get();

        while (curr != nullptr && i < index) {
            i++;
            prev = prev->next.get();
            curr = curr->next.get();
        }

        if (curr == nullptr || i < index) {
            return false;
        }

        if (index == 0) {
            this->head = std::move(curr->next);
        } else {
            prev->next = std::move(curr->next);
            this->head = std::move(dummy_head->next);
        }

        return true;
    }

    vector<int> getValues() {
        vector<int> values;
        Node *curr = this->head.get();
        
        while (curr != nullptr) {
            values.push_back(curr->val);
            curr = curr->next.get();
        }
        return values;
    }
};

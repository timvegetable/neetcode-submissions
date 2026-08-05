class LinkedList {
private:
    class Node {
    public:
        int val;
        Node *next = nullptr;
        Node(int value) : val(value) {}
        Node(int value, Node *next_ptr) 
        : val(value), next(std::move(next_ptr)) {}
    };
    Node *dummy_head = new Node(-1, nullptr);
    Node *tail = dummy_head;
public:
    int get(int index) {
        int i = 0;
        Node *curr = this->dummy_head->next;
        while (curr != nullptr && i < index) {
            i++;
            curr = curr->next;
        }
        if (curr == nullptr || i < index) {
            return -1;
        } else {
            return curr->val;
        }
    }

    void insertHead(int val) {
        this->dummy_head->next = new Node(val, std::move(this->dummy_head->next));
        if (this->tail == this->dummy_head) {
            this->tail = this->dummy_head->next;
        }
    }
    
    void insertTail(int val) {
        if (this->tail == this->dummy_head) {
            this->tail = new Node(val);
            this->dummy_head->next = this->tail;
        } else {
            this->tail->next = new Node(val);
            this->tail = this->tail->next;
        }
    }

    bool remove(int index) {
        int i = 0;
        Node *prev = dummy_head;
        Node *curr = prev->next;

        while (curr != nullptr && i < index) {
            i++;
            prev = prev->next;
            curr = curr->next;
        }

        if (curr == nullptr || i < index) {
            return false;
        }

        if (this->tail == curr) {
            this->tail = prev;
        }

        prev->next = std::move(curr->next);
        delete curr;
        return true;
    }

    vector<int> getValues() {
        vector<int> values;
        Node *curr = this->dummy_head->next;
        
        while (curr != nullptr) {
            values.push_back(curr->val);
            curr = curr->next;
        }
        return values;
    }

    ~LinkedList() {
        Node *curr = this->dummy_head;
        while (curr != nullptr) {
            Node *temp = curr;
            curr = curr->next;
            delete temp;
        }
    }
};

class Node{
    constructor(val){
        this.value = val;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
        this.size = 0;
    }

    add(element){
        var node = new Node(element);
        var current;
        if(this.head==null){
            this.head = node;
        }
        else{
            current = this.head;
            while(current.next != null)
                current = current.next;
            current.next = node;
        }
        this.size++;
    }

    iterate(){
        var ans = [];
        var current = this.head;
        while(current != null){
            ans.push(current.value);
            current = current.next;
        }
        console.log(ans);
    }

    removeHead(){
        this.head = this.head.next;
    }

    removeElement(val){
        var current = this.head;
        var prev = null;
        while(current.next != null){
            if(current.value == val){
                prev.next = current.next;
                return;
            }
            prev = current;
            current  = current.next;
        }
    }

}

var ll = new LinkedList();
ll.add(2);
ll.add(4);
ll.add(5);
ll.add(3);
ll.iterate();
ll.removeHead();
ll.removeHead();
ll.iterate();
ll.add(6);
ll.iterate();
ll.removeElement(6);
ll.iterate();
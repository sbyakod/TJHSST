//addAllHashIntSet.java

/*Write a method named addAll that could be placed inside the HashIntSet class.
This method accepts another HashIntSet as a parameter and adds all elements from
that set into the current set, if they are not already present. For example,
if a set s1 contains [1, 2, 3] and another set s2 contains [1, 7, 3, 9], the
call of s1.addAll(s2); would change s1 to store [1, 2, 3, 7, 9] in some order.*/

public void addAll(HashIntSet s) {
    for(int i = 0; i < s.elementData.length; i++) {
        Node node = s.elementData[i];

        while(node != null) {
            if(!this.contains(node.data))
                this.add(node.data);
            node = node.next;
        }
    }
}

//containsAllHashIntSet.java

/*Write a method in the HashIntSet class called containsAll that accepts
another hash set as a parameter and returns true if your set contains every
element from the other set. For example, if the set stores [-2, 3, 5, 6, 8]
and the method is passed [3, 6, 8], your method would return true. If the
method were passed [3, 6, 7, 8], your method would return false because your
set does not contain the value 7.*/

public boolean containsAll(HashIntSet s) {
    for(int i = 0; i < s.elementData.length; i++) {
        Node node = s.elementData[i];

        while(node != null) {
            if(!this.contains(node.data))
                return false;
            node = node.next;
        }
    }

    return true;
}

//equalsHashIntSet.java

/* Write a method in the HashIntSet class called equals that accepts another 
 * object as a parameter and returns true if the object is another HashIntSet 
 * that contains exactly the same elements. The internal hash table size and 
 * ordering of the elements does not matter, only the sets of elements 
 * themselves.
 */
public boolean equals(Object object) {
    if(object instanceof HashIntSet) {
        HashIntSet set = (HashIntSet) object;

        if(size != set.size())
            return false;

        for(int i = 0; i < elementData.length; i++) {
            Node current = elementData[i];
            while(current != null) {
                if(!set.contains(current.data))
                    return false;
                current = current.next;
            }
        }

        return true;
    }

    return false;
}

//removeAllHashIntSet.java

/* Write a method in the HashIntSet class called removeAll that accepts 
 * another hash set as a parameter and ensures that this set does not contain 
 * any of the elements from the other set.
 */
public void removeAll(HashIntSet set) {
    for(int i = 0; i < set.elementData.length; i++) {
        Node current = set.elementData[i];
        while(current != null) {
            remove(current.data);
            current = current.next;
        }
    }
}

//retainAllHashIntSet.java

/* Write a method in the HashIntSet class called retainAll that accepts 
 * another hash set as a parameter and removes all elements from this set that 
 * are not contained in the other set.
 */
public void retainAll(HashIntSet set) {
    for(int i = 0; i < elementData.length; i++) {
        Node prev = null;
        Node current = elementData[i];

        while(current != null) {
            if(!set.contains(current.data)) {
                if(prev == null)
                    elementData[i] = current.next;
                else
                    prev.next = current.next;

                size--;
                break;
            } else {
                prev = current;
                current = current.next;
            }
        }
    }
}

//toArrayHashIntSet.java

/* Write a method in the HashIntSet class called toArray that returns the 
 * elements of the set as a filled array. The order of the elements in the 
 * array is not important as long as all elements from the set are present in 
 * the array, with no extra empty slots before or afterward.
 */
public int[] toArray() {
    int[] result = new int[size];
    int index = 0;

    for(int i = 0; i < elementData.length; i++) {
        Node current = elementData[i];

        while(current != null) {
            result[index] = current.data;
            index++;
            current = current.next;
        }
    }

    return result;
}
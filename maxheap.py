class MaxHeap():
    def __init__(self):
        self.items = [None]
    def add(self, data, value):
        self.items.append((data, value))
        self.heapify_up()

        print(self.items)

    def pop(self):
        last_idx = len(self.items) - 1
        #Swaps root index with last index, then removes last index
        self.items[1], self.items[last_idx] = self.items[last_idx], self.items[1]
        max_value = self.items.pop(last_idx)
        self.heapify_down()

        print(self.items)
        return max_value

    def get_parent_idx(self, idx):
        return idx // 2
    def get_left_child(self, idx):
        return idx * 2
    def get_right_child(self, idx):
        return idx * 2 + 1

    def heapify_up(self):
        child_idx = len(self.items) - 1
        while child_idx != 1:
            parent_idx = self.get_parent_idx(child_idx)
            #Swaps elements if value of child element is larger than value of parent element, otherwise, heapifying up is complete and loop is broken
            if self.items[child_idx][1] < self.items[parent_idx][1]:
                break

            self.items[parent_idx], self.items[child_idx] = self.items[child_idx], self.items[parent_idx]

            child_idx = parent_idx
            parent_idx = self.get_parent_idx(child_idx)
    
    def heapify_down(self):
        parent_idx = 1
        #Compares value of parent to the maximum value of its two children. If the parent is smaller than its max value child, swaps the two elements, and loops until the heap is restored
        while True:
            left_child_idx = self.get_left_child(parent_idx)
            right_child_idx = self.get_right_child(parent_idx)
            #First, checks validity of indices (whether they're still within the size of the array)
            #If right child index is out of bounds and left child index is in bounds, the maximum value index defaults to the left child index
            if right_child_idx >= len(self.items):
                if left_child_idx < len(self.items):
                    max_child_idx = left_child_idx
                #If both child indices are out of bounds, heapifying is complete
                else:
                    break
            elif self.items[left_child_idx][1] > self.items[right_child_idx][1]:
                max_child_idx = left_child_idx
            else:
                max_child_idx = right_child_idx

            if self.items[parent_idx][1] > self.items[max_child_idx][1]:
                break

            #Swaps parent with larger child
            self.items[max_child_idx], self.items[parent_idx] = self.items[parent_idx], self.items[max_child_idx]

            #Reassigns parent index
            parent_idx = max_child_idx
class LinkedList(object):  # A linked list of data elements
    def traverse(self, list, func=print):  # Apply a function to all items in list, default is print
        link = self.getFirst()  # Start with first link
        while link is not None:  # Keep going until no more links
            func(link.getData())  # Apply the function to the item
            link = link.getNext()  # Move on to next link

    def __len__(self):  # Get length of list
        l = 0
        link = self.getFirst()  # Start with first link
        while link is not None:  # Keep going until no more links
            l += 1  # Count link in chain
            link = link.getNext()  # Move on to next link
        return l

    def __str__(self):  # Build a string representation
        result = "["  # Enclose list in square brackets
        link = self.getFirst()  # Start with first link
        while link is not None:  # Keep going until no more links
            if len(result) > 1:  # After first link
                result += " > "  # Separate links with right arrowhead
            result += str(link)  # Append string version of link
            link = link.getNext()  # Move on to next link
        return result + "]"

class LinkedList(object):
    def __iter__(self): # Define an iterator for the list
        next = self.getFirst() # Start with first Link
        while next is not None: # As long as the link is not None
            yield next.getData() # yield data for the link
            next = next.getNext() # then move on to next link
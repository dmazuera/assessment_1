"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers_list):
   
    odd_list = []

    for number in numbers_list: 
        #if the number in the list has 0 as the remainder when /2 
        #then include that number in the new printed list
        if number %2 != 0:
            odd_list.append(number)

    return odd_list









def print_indices(items):
   
    # this will print the index of the thing, then the thing
    # all on a new line
    for thing in items: 
        print "{} {}".format(items.index(item), thing)











def foods_in_common(foods1, foods2):
   

    A = set(foods1)
    B = set(foods2)
    #find the foods that the intersections of A list and B list
    common_food = (A&B)
    list_common_foods = list(common_food)
    sorted_common_foods = sorted(list_common_foods)
    print sorted_common_foods











def every_other_item(items):
   

    new_list = []
    for thing in items:
        #find the index of all items in the list
        index_thing = items.index(item)

        if index_thing %2 == 0:
            #create a new list of only items with index 0 & even indexes
            new_list.append(items[index_thing])

    print new_list








   

def largest_n_items(items, n):
    ascending_items = sorted(items)
    print ascending_items[-n:]



#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")

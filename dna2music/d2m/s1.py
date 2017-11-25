import collections

def windows(S, T):
    # empty string/multiset is matched everywhere
    if not T:
        yield(0, 0)
        return

    # target multiset initialized to contents of T
    target_ms = collections.Counter(T)

    # empty test multiset
    test_ms = collections.Counter()

    head = enumerate(S)
    tail = enumerate(S)

    # while the condition is not met, advance head 
    # and add to the test multiset
    # iterate over the whole input with head
    for i_head, char_head in head:
        test_ms[char_head] += 1

        # while the condition is met, advance tail
        # (and subtract from test multiset)
        # (a - b) for Counters has only elements from a that 
        # remained >0 after subtraction
        while not target_ms - test_ms:
            i_tail, char_tail = tail.next()
            yield (i_tail, i_head + 1)
            test_ms[char_tail] -= 1

def min_window(S, T):
    # initialize
    min_len = len(S) + 1
    min_start, min_end = None, None

    # go through all matching windows, pick the shortest
    for start, end in windows(S, T):
        if end - start < min_len:
            min_start, min_end = start, end
            min_len = end - start

    return (min_start, min_end)

if __name__ == '__main__':
    S = 'ADOBECODEBANC'
    T = 'ABC'
    min_window(S, T)    
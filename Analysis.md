# Runtime Analysis

## Task0

**Description**: Print the first text record and the last call record.

**Approach**: Access the first element of `texts` and the last element of `calls`, then format the required output messages.

**Complexity Analysis**:
- **Big O Notation**: `O(1)`
- **Justification**: The solution performs direct index lookups and constant-time string formatting. The work does not grow with the size of the input lists.

## Task1

**Description**: Count the number of distinct telephone numbers that appear in the text and call records.

**Approach**: Iterate through every text and call record and keep a list of telephone numbers seen so far. Before appending a number, scan the list to avoid duplicates.

**Complexity Analysis**:
- **Big O Notation**: `O(n^2)`
- **Justification**: For each number encountered, the algorithm may scan the growing `telephone_numbers` list to check membership. In the worst case, the number of comparisons grows quadratically with the total number of records.

## Task2

**Description**: Find the telephone number that spent the most total time on calls, counting both outgoing and incoming durations.

**Approach**: Walk through the call records, update a running total for both participants in each call using parallel lists, then scan the totals once more to find the maximum.

**Complexity Analysis**:
- **Big O Notation**: `O(n^2)`
- **Justification**: Each call updates two participants, and each update may require a linear search through the accumulated list of numbers. The final scan for the maximum is linear, so the repeated searches dominate the runtime.

## Task3

**Description**: Collect all unique area codes and mobile prefixes called by Bangalore fixed lines and compute the percentage of Bangalore-to-Bangalore fixed-line calls.

**Approach**: Iterate through the calls once, inspect only the calls originating from `(080)`, extract the destination code or prefix, store unique codes in a list, sort the final list, and compute the percentage from two counters.

**Complexity Analysis**:
- **Big O Notation**: `O(n^2)`
- **Justification**: The main loop over calls is linear, but checking whether a discovered code is already present in `bangalore_codes` is a linear membership scan. In the worst case, that repeated duplicate check dominates. The final sort is `O(k log k)`, which does not exceed the quadratic duplicate-check cost when `k` grows with `n`.

## Task4

**Description**: Identify numbers that make outgoing calls but never send texts, receive texts, or receive incoming calls.

**Approach**: Build one list for outgoing callers, one list for every number that receives a call or appears in any text record, then scan the outgoing callers to keep only the numbers absent from the second list. Sort the result before printing.

**Complexity Analysis**:
- **Big O Notation**: `O(n^2)`
- **Justification**: The solution repeatedly uses linear membership checks while building the two lists and again while filtering the candidate telemarketers. Those repeated scans dominate the final `O(k log k)` sort.

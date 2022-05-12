# Name:
# SBUID:
# Remove the ellipses (...) when writing your solutions.
# ---------------------------- Q1 ---------------------------------------
# TODO: Given a list 'lst', perform a movement of item at index 'from_index'
#       to the index 'to_index'.
def move(lst, from_index, to_index):
    final = []
    # 변하지 않는 부분 복사
    for i in range(to_index):
        final += [lst[i]]
    # 옮길 숫자 파이널 리스트에 넣기
    final += [lst[from_index]]
    # 옮긴 숫자 제외 나머지 숫자 복사
    for j in range(to_index, len(lst)):
        if j == from_index:
            continue
        else:
            final += [lst[j]]
    return final

# ---------------------------- Q2 ---------------------------------------
# TODO: Provide a run-time analysis of your implementation of move().
# That is, try to express the number of iterations in terms of N, which is
# the number of items in 'lst'. You don't have to write the big-O, though.

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.
lst = [3, 2, 1, 5, 9, 2]
print(move(lst, 3, 1)) # Should print out [3, 5, 2, 1, 9, 2]


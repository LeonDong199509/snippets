def handle(l):
    def sort(queue):
        queue_len = len(queue)
        if queue_len <= 1:
            return queue
        mid_index = queue_len // 2
        left = queue[:mid_index]
        right = queue[mid_index:]
        return merge(sort(left), sort(right))

    def merge(left, right):

        l_len = len(left)
        r_len = len(right)

        i = 0
        j = 0
        result = []
        while (i < l_len or j < r_len):
            if i == l_len:
                result.extend(right[j:])
                break
            elif j == r_len:
                result.extend(left[i:])
                break
            elif left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result

    return sort(l)


print(handle([2,4,6 ,7, 1, 3, 4, 9]))

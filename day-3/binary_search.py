class BinarySearch(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

        # create sorted list
        self.lst = [x for x in range(0, self.a, self.b)]
        self.length = len(self.lst)

    def search(self, key):
        # set low and high values
        low = 0
        high = len(self.lst) - 1
        count = 0

        # Loop through and search
        while low <= high:
            count += 1
            # Divide list by half
            mid = (high + low) // 2
            if key == self.lst[mid]:
                # return {count : mid}
                return {"count: " + str(count): "index: " + str(mid)}
            elif key < self.lst[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return (-low - 1)

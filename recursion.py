def replicate_iter(times, data):
    if not isinstance(times, int) or not isinstance(data, (int,str)):
            raise ValueError("Invalid arguments")
    if times <= 0:
            return []
    else:
            array = []
            for i in range(times):
                    array.append(data)
            return array


def replicate_recur(times, data):
    if not isinstance(times, int) or not isinstance(data, (int,str)):
            raise ValueError("Invalid arguments")
    if times <= 0:
            return []
    else:
            array = []
            for i in range(times):
                    array.append(data)
            return array    

class Binary:

    def __init__(self, numb)
        r_list = []

        x = numb
        while x > 0:
            r = x % base
            q = (x - r)//2
            x = q
            r_list.append(r)

        r_list = r_list[::-1]
        self.vallue = r_list

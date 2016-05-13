class Buffer:
    def __init__(self):
        buf = []
    def add(self, *a):
        # for n in a:
        #     print(n)
        #     self.buffer.append(a)

        # self.buffer
        self.buf.append(a)
        print(self.buf)
    def get_current_part(self):
        pass

Buffer.add(1,2,3,4,5)

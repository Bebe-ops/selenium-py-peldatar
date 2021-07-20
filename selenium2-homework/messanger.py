class MessageBox:
    def __init__(self):
        self.operations = []
        self.amount_received_msg = None
        self.amount_sent_msg = None

    def msg_rec(self):
        self.operations.append(1)

    def msg_send(self):
        self.operations.append(2)

    def amount(self):
        msg_send_price = 20
        msg_receive_price = 2
        amount = 0
        for i in self.operations:
            if i == 1:
                amount += msg_receive_price
            elif i == 2:
                amount += msg_send_price

        return f'Price of messages:{amount}'


user1 = MessageBox()
user1.msg_send()
user1.msg_rec()
user1.msg_rec()
print(user1.amount())
print(user1.operations)

user2 = MessageBox()
user2.msg_rec()
user2.msg_send()
user2.msg_send()
user2.msg_send()
user2.msg_rec()
print(user2.amount())
print(user2.operations)

# -------------------------------------------------------------------------------------------------
# Más féle megoldásom
# class MessageBox:
#     def __init__(self, op=None):
#         if op is None:
#             op = []
#         self.operations = op
#         for _ in self.operations:
#             if _ % 2 != 0:
#                 self.msg_receive = self.operations.count(_)
#             else:
#                 self.msg_send = self.operations.count(_)
#
#     def amount(self):
#         msg_send_price = 20
#         msg_receive_price = 2
#         return f'Price of received messages:{self.msg_receive * msg_receive_price}, ' \
#                f'Price of sent messages: {self.msg_send * msg_send_price}'
#
#     def __str__(self):
#         return f'Message received (count of 1): {self.msg_receive}, Message sent (count of 2): {self.msg_send}'
#
#
# user1 = MessageBox([1, 2, 1, 1, 1, 1])
# print(user1)
# print(user1.amount())
#
# user2 = MessageBox([2, 1, 1, 1, 2, 2, 2])
# print(user2)
# print(user2.amount())

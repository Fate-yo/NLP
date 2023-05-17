from Train import train
import datetime
from cut import cut

text = "深航客机攀枝花机场遇险：机腹轮胎均疑受损，跑道灯部分损坏"

start_time = datetime.datetime.now()
train()
end_time = datetime.datetime.now()
print((end_time - start_time).seconds)
cut(text)
print(text)
print(str(list(cut(text))))

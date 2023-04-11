
import re
from urllib.request import urlopen
import nltk
from zhtools import langconv, zh_wiki
from zhtools.langconv import Converter


# text1 = '''汪淼觉得，来找他的这四个人是一个奇怪的组合：两名警察和两名军人，如果那两个军人是武警还算正常，但这是两名陆军军官。汪淼第一眼就对来找他的警察没有好感。其实那名穿警服的年轻人还行，举止很有礼貌，但那位便衣就让人讨厌了。这人长得五大三粗，一脸横肉，穿着件脏兮兮的皮夹克，浑身烟味，说话粗声大嗓，是最令汪淼反感的那类人。“汪淼？”那人问，直呼其名令汪淼很不舒服，况且那人同时还在点烟，头都不抬一下。不等汪淼回答，他就向旁边那位年轻人示意了一下，后者向汪淼出示了警官证，他点完烟后就直接向屋里闯。请不要在我家里抽烟。”汪淼拦住了他。“哦，对不起，汪教授。这是我们史强队长。”年轻警官微笑着说，同时对姓史的使了个眼色。“成，那就在楼道里说吧。”史强说着，深深地吸了一大口，手中的烟几乎燃下去一半，之后竟不见吐出烟来。“你问。”他又向年轻警官偏了一下头。汪教授，我们是想了解一下，最近你与‘科学边界’学会的成员有过接触，是吧？”“‘科学边界’是一个在国际学术界很有影响的学术组织，成员都是著名学者。这样一个合法的学术组织，我怎么就不能接触了呢？”“看看你这个人！”史强大声说，“我们说它不合法了吗？我们说不让你接触了吗？”他说着，刚才吸进肚子里的烟都喷到汪淼脸上。“那好，这属于个人隐私，我没必要回答你们的问题。汪淼说着要转身回屋。'''
# import re
#
# # print(re.match("汪淼", text1))
# # t_string = text1.split("。")
# # for line in t_string:
# #     if re.match("汪淼",line) is not None:
# #         print(line)
# # print(re.search("汪淼", text1))
# # print(re.findall("汪淼", text1))
# pattern = '.人'
# print(re.findall(pattern, text1))
# pattern2 = '[一几军]人'
# print(re.findall(pattern2, text1))
# pattern3 = '汪淼|两名'
# print(re.findall(pattern3, text1))
# t_string = text1.split("。")
# for line in t_string:
#     if len(re.findall(pattern3, line)) != 0:
#         print(line)
# pattern4 = '^汪淼'
# print("-------------------------")
# for line in t_string:
#     if len(re.findall(pattern4, line)) :
#         print(line)

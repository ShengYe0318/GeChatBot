# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("abcde8952505@gmail.com","abcd4501119")
channelToken = cl.getChannelResult()
print ("======Rimuru登入成功=====")
oepoll = OEPoll(cl)
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
clMID = cl.profile.mid
KAC=[cl]
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
admin=['u66d4c27e8f45f025cf5774883b67ddc1',clMID]
master=['u66d4c27e8f45f025cf5774883b67ddc1',clMID]
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        return False
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """℅指令表℅
《Help》幫助
§已讀指令
《Setread》《SR》已讀設置
《Lookread》《LR》已讀查看
§群組用指令
《Tagall》全體標註 ＊請謹慎使用
《URL On/Off》群組網址開啟/關閉
《Ginfo》群組詳細資料
《Gurl》顯示群組網址
《@bye》退出群組
§自己
《Me》查看自己好友資料
《MyName》查看自己名字
《MyBio》查看自己個簽
《MyPicture》查看自己頭貼網址
《MyCover》查看自己封面網址
《Picture @》標註查看頭貼
§其他指令
《Speed》運行速度查詢
《About》狀態查詢
《Creator》作者友資
⇛如有其他疑問請私訊作者⇚
⇛Create it By.Ge™⇚
⇛Made in Taiwan⇚"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            cl.findAndAddContactsByMid(op.param1)
            cl.sendMessage(op.param1, "哈囉{}~要跟莉姆露成為好朋友哦>///<".format(str(contact.displayName)))
            cl.sendMessage(op.param1, "↓↓如果有其他疑問可以私訊主人↓↓")
            cl.sendContact(op.param1, "u66d4c27e8f45f025cf5774883b67ddc1")
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[☆] 莉姆露收到群組邀請: " + str(group.name) + "\n邀請的人: " + contact1.displayName + "\n被邀請的人" + contact2.displayName)
            if settings["autoJoin"] == True:
                    print ("[☆]莉姆露加入群組: " + str(group.name))
                    cl.acceptGroupInvitation(op.param1)
        elif op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人的人: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢的人" + contact2.displayName + "\nMid:" + contact2.mid )
            try:
                cl.sendMessage(op.param1,"《被踢的人》")
                cl.sendContact(op.param1,op.param3)
            except:
                pass
        if op.type == 24:
                cl.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if sender in master:
                if "KICK " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in master:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif msg.text in ["SET"]:
                    try:
                        ret_ = "《設定》"
                        if settings["reread"] == True: ret_ += "\n查詢收回 🆗"
                        else: ret_ += "\n查詢收回 🈲"
                        if settings["autoJoin"] == True: ret_ += "\n自動加入群組 🆗"
                        else: ret_ += "\n自動加入群組 🈲"
                        if settings["autoLeave"] == True: ret_ += "\n自動離開副本 🆗"
                        else: ret_ += "\n自動離開副本 🈲"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif msg.text in ["RIMURUREBOT"]:
                    cl.sendMessage(to, "《莉姆露重啟~》")
                    restartBot()
                elif msg.text in ["AUTOJOIN On"]:
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "《莉姆露自己加入群組》")
                elif msg.text in ["AUTOJOIN Off"]:
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "《由主人決定加入群組》")
                elif msg.text in ["LEAVE On"]:
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "《莉姆露會離開副本》")
                elif msg.text in ["LEAVE Off"]:
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "《莉姆露會留在副本》")
                elif msg.text in ["REREAD On"]:
                    settings["reread"] = True
                    cl.sendMessage(to, "《查詢收回開啟》")
                elif msg.text in ["REREAD Off"]:
                    settings["reread"] = False
                    cl.sendMessage(to, "《查詢收回關閉》")
                elif msg.text in ["Grl","grl","GRL"]:
                        groups = cl.groups
                        ret_ = "《莉姆露的群組》"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n☆ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n《總共 {} 個》".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif "JBLACK @" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "《加入黑名單》")
                                    cl.sendMessage(target, "不好意思 您違反了使用規定\n因此已被此程序列為黑單\n如有意見 請私訊作者")
                                except:
                                    pass
                elif "MBLACK " in msg.text:
                    mmid = msg.text.replace("MBLACK ","")
                    try:
                        settings["blacklist"][mmid] = True
                        cl.sendMessage(to, "《加入黑名單》")
                        cl.sendMessage(mmid, "不好意思 您違反了使用規定\n因此已被此程序列為黑單\n如有意見 請私訊作者")
                    except:
                        pass
                elif "UBLACK @" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "《解除黑名單》")
                                except:
                                    pass
                elif msg.text in ["CLEAR BLACKLIST"]:
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                        cl.sendMessage(to, "《清空黑名單》")
                elif msg.text in ["BLACKLIST"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        cl.sendMessage(to, "《以下是黑名單》")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "》" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif msg.text in ["BLACKMID"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        cl.sendMessage(to, "《以下是黑名單》")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "》" + mi_d + "\n"
                        cl.sendMessage(to, mc)
                elif msg.text in ["KBLACK"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "《沒有黑名單》")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "《黑名單已清除》")
                elif msg.text in ["KABLACK"]:
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "《剔除所有群組黑單人選》")
                elif "Friendbc:" in msg.text:
                    bctxt = text.replace("Friendbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Groupsbc:" in msg.text:
                    bctxt = text.replace("Groupsbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif "user " in msg.text:
                    mmid = msg.text.replace("user ","")
                    cl.sendContact(to, mmid)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text in ["help","Help","HELP"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif msg.text in ["Creator","creator"]:
                    cl.sendContact(to, "u66d4c27e8f45f025cf5774883b67ddc1")
                elif text.lower() == '@bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            cl.sendMessage(to, "大家不喜歡莉姆露了嗎QAQ")
                            cl.leaveGroup(to)
                        except:
                            pass
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "《已讀設置》")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "《已讀的人》%s\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "《還沒設定已讀點哦¨》")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"《顯示名稱》\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"《狀態消息》\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = cl.getContact(sender)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text in ["cancel","Cancel","CANCEL"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "《已取消所有邀請》" )
                    else:
                        cl.sendMessage(to, "《沒有邀請可以取消》")
                elif msg.text in ["speed","Speed","SPEED"]:
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'《處理速度》\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'《指令反應》\n' + format(str(elapsed_time)) + '秒')
                elif msg.text in ["About","about","ABOUT"]:
                    try:
                        arr = []
                        owner = "u66d4c27e8f45f025cf5774883b67ddc1"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "《關於自己》"
                        ret_ += "\n版本 : v2.0"
                        ret_ += "\n名稱 : {}".format(contact.displayName)
                        ret_ += "\n群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n好友 : {}".format(str(len(contactlist)))
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif msg.text in ["Gurl","gurl","GURL"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "《群組網址》\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "《群組網址未開啟》".format(str(settings["keyCommand"])))
                elif msg.text in ["URL On"]:
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "《群組網址已開啟》")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "《成功開啟群組網址》")
                elif msg.text in ["URL Off"]:
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "《群組網址已關閉》")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "《成功關閉群組網址》")
                elif msg.text in ["Ginfo","ginfo","GINFO"]:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "未找到"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料 》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n網址狀態 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["Tagall","tagall","TAGALL"]:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "《總共 {} 個成員》".format(str(len(nama))))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "《文章網址》\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                    cl.sendChatChecked(to, msg_id)
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"《有人偷偷收回訊息哦》\n%s\n《訊息內容》\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☆" + Name
                        wait2['ROM'][op.param1][op.param2] = "☆" + Name
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

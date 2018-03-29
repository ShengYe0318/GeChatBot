# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import Message
from datetime import datetime
import json,sys,atexit,time,codecs,timeit
botStart = time.time()
cl = LINE("linyuar89525@gmail.com","abcd4501119")
channelToken = cl.getChannelResult()
print ("======登入成功=====")
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
admin=['u66d4c27e8f45f025cf5774883b67ddc1','u097922eb3f3ff2ab43642fc44c9d850b','u30b8cdf6810d973df49d4f893fb0a47c',clMID]
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
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
    cl.log("[ ERROR ] " + str(text))
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
    helpMessage = """⇛Create it By.Ge™⇚"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(param2)
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "你好 {} 此為自動好友確認功能之泛用訊息 :D ".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "群組網址保護中 請勿觸碰網址開關")
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[☆] 邀請群組通知: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
            if settings["autoJoin"] == True:
                if op.param2 in admin:
                    print ("[☆]進入群組: " + str(group.name))
                    cl.acceptGroupInvitation(op.param1)
                pass
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[！]有人把人踢出群組 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(to,["u66d4c27e8f45f025cf5774883b67ddc1"])
                    settings["blacklist"][op.param2] = True
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
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
            if sender in admin:
                if msg.text in ["help","Help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif "KICK " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "MIDKICK " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "NAMEKICK " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                
                elif msg.text in ["cancel","Cancel"]:
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
                elif "Blackjoin @" in msg.text:
                    if msg.toType == 2:
                        _name = msg.text.replace("blackjoin @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(msg.to,"《已加入黑名單》")
                                except:
                                    pass
                elif "Bblack @" in msg.text:
                    if msg.toType == 2:
                        _name = msg.text.replace("bblack @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "《已解除黑名單》")
                                except:
                                    pass
                elif msg.text in ["blacklist","Blacklist"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        cl.sendMessage(to, "▲黑名單：")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "->" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif msg.text in ["kick blacklist","Kick blacklist"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "《沒有黑名單人選》")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "《黑名單已踢除》")
                elif msg.text in ["speed","Speed"]:
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'《處理速度》\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'《指令反應》\n' + format(str(elapsed_time)) + '秒')
                elif msg.text in ["set","Set"]:
                    try:
                        ret_ = "《設定》"
                        if settings["autoJoin"] == True: ret_ += "\n自動加入群組 🆗"
                        else: ret_ += "\n自動加入群組 🈲"
                        if settings["autoAdd"] == True: ret_ += "\n自動加入好友 🆗"
                        else: ret_ += "\n自動加入好友 🈲"
                        if settings["autoLeave"] == True: ret_ += "\n自動離開副本 🆗"
                        else: ret_ += "\n自動離開副本 🈲"
                        if settings["reread"] == True: ret_ += "\n查詢收回 🆗"
                        else: ret_ += "\n查詢收回 🈲"
                        if settings["inviteprotect"] == True: ret_ += "\n邀請保護 🆗"
                        else: ret_ += "\n邀請保護 🈲"
                        if settings["qrprotect"] == True: ret_ += "\n網址保護 🆗"
                        else: ret_ += "\n網址保護 🈲"
                        if settings["protect"] == True: ret_ += "\n群組保護 🆗"
                        else: ret_ += "\n群組保護 🈲"
                        if settings["contact"] == True: ret_ += "\n友資資訊 🆗"
                        else: ret_ += "\n友資資訊 🈲"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif msg.text in ["autojoin On","Autojoin On"]:
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "《自動加入群組已開啟》")
                elif msg.text in ["autojoin Off","Autojoin Off"]:
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "《自動加入群組已關閉》")
                elif msg.text in ["leave On","Leave On"]:
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "《自動離開副本已開啟》")
                elif msg.text in ["leave Off","Leave Off"]:
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "《自動離開副本已關閉》")
                elif msg.text in ["add On","Add On"]:
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "《自動加入好友已開啟》")
                elif msg.text in ["add Off","Add Off"]:
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "《自動加入好友已關閉》")
                elif msg.text in ["inviteptt On","Inviteptt On"]:
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "《群組邀請保護已開啟》")
                elif msg.text in ["inviteptt Off","Inviteptt Off"]:
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "《群組邀請保護已關閉》")
                elif msg.text in ["URLptt On"]:
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "《群組網址保護已開啟》")
                elif msg.text in ["URLptt Off"]:
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "《群組網址保護已關閉》")
                elif msg.text in ["groupsptt On","Groupsptt On"]:
                    settings["protect"] = True
                    cl.sendMessage(to, "《群組保護已開啟》")
                elif msg.text in ["groupsptt Off","Groupsptt Off"]:
                    settings["protect"] = False
                    cl.sendMessage(to, "《群組保護已關閉》")
                elif msg.text in ["contact On","Contact On"]:
                    settings["contact"] = True
                    cl.sendMessage(to, "《友資資訊已開啟》")
                elif msg.text in ["contact Off","Contact Off"]:
                    settings["contact"] = False
                    cl.sendMessage(to, "《友資資訊已關閉》")
                elif msg.text in ["reread On","Reread On"]:
                    settings["reread"] = True
                    cl.sendMessage(to, "《查詢收回已開啟》")
                elif msg.text in ["reread Off","Reread Off"]:
                    settings["reread"] = False
                    cl.sendMessage(to, "《查詢收回已關閉》")
                
                
                
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

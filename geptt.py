# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import Message
from datetime import datetime
import json,sys,atexit,time,codecs,timeit
botStart = time.time()
cl = LINE("abcde89525@gmail.com","abcd4501119")
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
    helpMessage = """℅指令表℅
《help》幫助
§黑單指令
《blackjoin @》加入黑單
《bblack @》解除黑單
《blacklist》查看黑名單
《kick blacklist》踢出黑單
§自動運行開關指令
《autojoin On/Off》機器自動進群開啟/關閉
《inviteptt On/Off》群組邀請保護開啟/關閉
《URLptt On/Off》群組網址保護開啟/關閉
《leave On/Off》自動離開副本開啟/關閉
《groupsptt On/Off》群組保護開啟/關閉
《add On/Off》自動加入好友開啟/關閉
《contact On/Off》友資資訊開啟/關閉
§踢出指令
《NAMEKICK “name”》用名字踢出
《MIDKICK “mid”》用MID踢出
《KICK @》用標注踢出
《Ri @》標注踢出重邀
§已讀指令
《Setread》《SR》已讀設置
《Lookread》《LR》已讀查看
§群組用指令
《URL On/Off》群組網址開啟/關閉
《Tagall》全體標註 ＊請謹慎使用
《cancel》取消所有邀請
《ginfo》群組詳細資料
《gurl》顯示群組網址
§其他指令
《speed》運行速度查詢
《set》目前狀態
         ⇛Create it By.Ge™⇚"""
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
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "不要打開群組網址")
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
                    cl.kickoutFromGroup(op.param1,[op.param3])
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
                    cl.inviteIntoGroup(to,["u097922eb3f3ff2ab43642fc44c9d850b"])
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
                    cl.sendContact(to, "u66d4c27e8f45f025cf5774883b67ddc1")
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
                            ret_ += "" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text in ["Grl","grl"]:
                        groups = cl.groups
                        ret_ = "\n《群組列表 》"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n￠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n《總共 {} 個群組 》".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif msg.text in ["Gurl","gurl"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "《群組網址》\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
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
                elif msg.text in ["Ginfo","ginfo"]:
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
                        gTicket = "沒有"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料 》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["Tagall","tagall"]:
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
            elif msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"《顯示名稱》:\n" + msg.contentMetadata["《顯示名稱》"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n《狀態消息》:\n" + contact.statusMessage + "\n《圖片網址》:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n《封面網址》:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"《顯示名稱》:\n" + contact.displayName + "\n《mid》:\n" + msg.contentMetadata["mid"] + "\n《狀態消息》:\n" + contact.statusMessage + "\n《圖片網址》:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n《封面網址》:\n" + str(cu))
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

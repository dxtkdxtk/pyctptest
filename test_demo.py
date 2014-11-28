from ctp.futures import ApiStruct, MdApi, TraderApi
from time import sleep


td = TraderApi()
td.Create()
td.RegisterFront('tcp://183.129.188.37:41205')
td.SubscribePrivateTopic(ApiStruct.TERT_RESTART)
td.SubscribePublicTopic(ApiStruct.TERT_RESTART)
td.Init()
pReqUserLogin = ApiStruct.ReqUserLogin('', '1019', '00000002', '123456')
td.ReqUserLogin(pReqUserLogin, 1)
sleep(1)
confirm = ApiStruct.SettlementInfo('', 0, '1019', '00000002')
td.ReqSettlementInfoConfirm(confirm, 2)
sleep(1)
for i in range(10):
    print td.GetTradingDay()
td.Join()
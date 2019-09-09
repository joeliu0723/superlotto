from bs4 import BeautifulSoup
import requests

winning_Numbers_Sort_lotto = ['SuperLotto638Control_history1_dlQuery_SNo1_','SuperLotto638Control_history1_dlQuery_SNo2_','SuperLotto638Control_history1_dlQuery_SNo3_','SuperLotto638Control_history1_dlQuery_SNo4_','SuperLotto638Control_history1_dlQuery_SNo5_','SuperLotto638Control_history1_dlQuery_SNo6_','SuperLotto638Control_history1_dlQuery_SNo7_']

def search_winning_numbers(css_class):   #先萃取並收集網頁內有 Lotto649Control_history_dlQuery_No1_ 等資訊，因此在程式中我們要把所有獎號的id用一個List記錄起來，到時候讓soup.find_all 去找符合id並收集起來
    global winning_Numbers_Sort_lotto
    if(css_class != None):
        for i in range(len(winning_Numbers_Sort_lotto )):
            if winning_Numbers_Sort_lotto [i] in css_class:
                return css_class            


def parse_tw_lotto_html(data_Info,number_count):  #取出獎號
    data_Info_List = []
    data_Info_Dict = {}
    tmp_index = 0
    for index  in range(len(data_Info)) :
        if (index == 0):
            data_Info_List.append(data_Info[index].text)  
        else:
            if(index % number_count != 0):
                data_Info_List.append(data_Info[index].text)
            else:
                data_Info_Dict[str(tmp_index)] = list(data_Info_List)
                data_Info_List= []
                data_Info_List.append(data_Info[index].text)
                tmp_index = tmp_index+1
        data_Info_Dict[str(tmp_index)] = list(data_Info_List)
    return data_Info_List,data_Info_Dict            


def winner_number():
	head_Html_lotto='http://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'
	res = requests.get(head_Html_lotto, timeout=30)

	soup = BeautifulSoup(res.text,'lxml')

	header_Info = soup.find_all(id=search_winning_numbers)
	data_Info_List,data_Info_Dict  = parse_tw_lotto_html(header_Info,7)    
	return data_Info_Dict['0']
import sys
import streamlit as st
import MeCab
import jaconv
import glob


def kanji2kana(file_name):
    # Mecabの辞書は自身で設定
    mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    input_folder = './'
    output_folder = './'
    input_text_name = input_folder + file_name + '_kanji.txt'
    f_input = open(input_text_name, 'r')
    f_output = open(output_folder + file_name+'.txt', 'w')
    #data = f.read()
    #print(data)
    datalist = f_input.readlines()
    datalist = [line.rstrip('\n') for line in datalist]
    for l in datalist:
        result = []
        result_text = ''
        time = l[:24]
        text = l[24:]
        print(time+text)
        if ' ' in text:
            text = text.replace(' ','。')
        node = mecab.parse('')
        node = mecab.parseToNode(text)
        while node :
            if (node.surface):
                if 'こんにちは' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('こんにちは', 'こんにちわ')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif 'こんばんは' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('こんばんは', 'こんばんわ')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)    
                elif '今晩は' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('今晩は', 'こんばんわ')
                    result.append(tmp_result)
                elif '明日' in node.feature.split(",")[6] and 'アシタ' in node.feature.split(",")[7]:
                    tmp_result = node.feature.split(",")[7].replace('アシタ', 'あす')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif 'その他' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('その他', 'そのほか')
                    result.append(tmp_result) 
                    result_text += jaconv.kata2hira(tmp_result)
                elif ('行く' == node.feature.split(",")[6]) and ('イッ' == node.feature.split(",")[7]):
                    tmp_result = node.feature.split(",")[6].replace('行く', 'おこなっ')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif ('降りる' == node.feature.split(",")[6]) and ('オリ' == node.feature.split(",")[7]):
                    tmp_result = node.feature.split(",")[7].replace('オリ', 'ふり')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '北陸' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('北陸', 'ほくりく')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '東日本' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('東日本', 'ひがしにほん')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '後' == node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('後', 'あと')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '方' == node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('方', 'かた')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif 'ムシムシ' in node.feature.split(",")[6]:
                    tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '一方' in node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = node.feature.split(',')[7]
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '道北' in node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'ドウホク'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '今日も一日' in node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'キョウモイチニチ'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '一日' in node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'イチニチ'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '通して' in node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = node.feature.split(',')[7]
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '角田奈緒子' in node.feature.split(",")[6] or '角田直子' in node.feature.split(",")[6] :
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'カクタナオコ'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '寒気' == node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'カンキ'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '洗濯物' == node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'センタクモノ'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif '外干し' == node.feature.split(",")[6]:
                    #tmp_result = node.feature.split(",")[6].replace('ムシムシ', 'むしむし')
                    tmp_result = 'ソトボシ'
                    result.append(tmp_result)
                    result_text += jaconv.kata2hira(tmp_result)
                elif (node.feature.split(",")[0]=="助詞" or node.feature.split(",")[0]=="接続詞"):
                    result.append(node.feature.split(",")[8])
                    # カタカナ表示
                    #result_text += node.feature.split(",")[8]
                    # ひらがな表示
                    result_text += jaconv.kata2hira(node.feature.split(",")[8])
                # print(node.surface + "\t" + node.feature.split(",")[7])
                else:
                    print(node.feature)
                    result.append(node.feature.split(",")[7])
                    # カタカナ表示
                    #result_text += node.feature.split(",")[7]
                    # ひらがな表示
                    result_text += jaconv.kata2hira(node.feature.split(",")[7])

            node = node.next
        print(time + result_text)
        f_output.write(time+result_text+'\n')
    f_output.close()

files = ['20200724_003']


for file in files:
    print('\nファイル名' + file)
    kanji2kana(file)

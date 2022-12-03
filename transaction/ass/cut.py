# -*- coding: utf-8 -*-
import networkx as nx
import io
import datetime
import warnings

warnings.filterwarnings('error')

# 89��ֳ�10��  9
mytime = datetime.datetime.strptime('2018-6-8', '%Y-%m-%d')
G = nx.DiGraph()
time_list = []
edge_list = []
result = []

for i in range(1,12):
    time_list.append(mytime + datetime.timedelta(days=i*9))
    
cnt = 0
with io.open('tx.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        info = line.encode('utf-8').decode('utf-8-sig').rstrip('\n').split(',')
        if datetime.datetime.strptime(info[0], '%Y-%m-%d') <= time_list[cnt]:
            edge_list.append([info[1],info[2]])   ##############################�ӱ�
        elif (cnt + 1)<10:
          if datetime.datetime.strptime(info[0], '%Y-%m-%d') <= time_list[cnt + 1]:
     
            cnt += 1
            G = nx.DiGraph()
            G.add_edges_from(edge_list)  #��edge_list�½����
            print(nx.degree_pearson_correlation_coefficient(G))
            result.append(nx.degree_pearson_correlation_coefficient(G))
            edge_list = []
            edge_list.append([info[1],info[2]])  #�ӱ�
        else: break
        
with io.open('vote_ass.csv', 'w') as fw:
     for k in range(len(result)):
        fw.write(unicode(time_list[k]) +u',' + unicode(result[k]) + u'\n')

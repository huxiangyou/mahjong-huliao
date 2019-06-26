# -*- coding: utf-8 -*-
#!/usr/bin/python3
#python 3.7.3

"""
version 0.0 coded by Hu Xiangyou on December 17, 2018
version 1.0 coded by Hu Xiangyou on February 9, 2019
version 1.1 coded by Hu Xiangyou on February 20, 2019
version 1.2 coded by Hu Xiangyou on March 20, 2019
version 2.0 coded by Hu Xiangyou on April 14, 2019
chinese version 0.0 coded by Hu Xiangyou on April 30, 2019
chinese version 1.0 coded by Hu Xiangyou on June 14, 2019

check hupai or tingpai in Chinese mahjong
"""

import time
import sys
from itertools import combinations
import test
import zh_CN as lang

class Fanzhong:
	def __init__(self,name,id_,fenshu,buji):
		self.name=name
		self.id=id_
		self.fenshu=fenshu
		self.buji=buji

id_iter=iter(range(81,0,-1))
if True:#Fanzhong
	花牌=Fanzhong(lang.花牌,next(id_iter),1,set())
	自摸=Fanzhong(lang.自摸,next(id_iter),1,set())
	单调将=Fanzhong(lang.单调将,next(id_iter),1,set())
	坎张=Fanzhong(lang.坎张,next(id_iter),1,set())
	边张=Fanzhong(lang.边张,next(id_iter),1,set())
	无字=Fanzhong(lang.无字,next(id_iter),1,set())
	缺一门=Fanzhong(lang.缺一门,next(id_iter),1,set())
	明杠=Fanzhong(lang.明杠,next(id_iter),1,set())
	幺九刻=Fanzhong(lang.幺九刻,next(id_iter),1,set())
	老少副=Fanzhong(lang.老少副,next(id_iter),1,set())
	连六=Fanzhong(lang.连六,next(id_iter),1,set())
	喜相逢=Fanzhong(lang.喜相逢,next(id_iter),1,set())
	一般高=Fanzhong(lang.一般高,next(id_iter),1,set())
	断幺=Fanzhong(lang.断幺,next(id_iter),2,{无字})
	暗杠=Fanzhong(lang.暗杠,next(id_iter),2,set())
	双暗刻=Fanzhong(lang.双暗刻,next(id_iter),2,set())
	双同刻=Fanzhong(lang.双同刻,next(id_iter),2,set())
	四归一=Fanzhong(lang.四归一,next(id_iter),2,set())
	平和=Fanzhong(lang.平和,next(id_iter),2,{无字})
	门前清=Fanzhong(lang.门前清,next(id_iter),2,set())
	门风刻=Fanzhong(lang.门风刻,next(id_iter),2,set())
	圈风刻=Fanzhong(lang.圈风刻,next(id_iter),2,set())
	箭刻=Fanzhong(lang.箭刻,next(id_iter),2,set())
	和绝张=Fanzhong(lang.和绝张,next(id_iter),4,set())
	双明杠=Fanzhong(lang.双明杠,next(id_iter),4,{明杠})
	不求人=Fanzhong(lang.不求人,next(id_iter),4,{自摸})
	全带幺=Fanzhong(lang.全带幺,next(id_iter),4,set())
	双箭刻=Fanzhong(lang.双箭刻,next(id_iter),6,{箭刻})
	全求人=Fanzhong(lang.全求人,next(id_iter),6,{单调将})
	五门齐=Fanzhong(lang.五门齐,next(id_iter),6,set())
	三色三步高=Fanzhong(lang.三色三步高,next(id_iter),6,set())
	混一色=Fanzhong(lang.混一色,next(id_iter),6,{缺一门})
	碰碰和=Fanzhong(lang.碰碰和,next(id_iter),6,set())
	双暗杠=Fanzhong(lang.双暗杠,next(id_iter),8,{暗杠,双暗刻})
	抢杠和=Fanzhong(lang.抢杠和,next(id_iter),8,{和绝张})
	杠上开花=Fanzhong(lang.杠上开花,next(id_iter),8,{自摸})
	海底捞月=Fanzhong(lang.海底捞月,next(id_iter),8,set())
	妙手回春=Fanzhong(lang.妙手回春,next(id_iter),8,{自摸})
	无番和=Fanzhong(lang.无番和,next(id_iter),8,set())
	三色三节高=Fanzhong(lang.三色三节高,next(id_iter),8,set())
	三色三同顺=Fanzhong(lang.三色三同顺,next(id_iter),8,{喜相逢})
	推不倒=Fanzhong(lang.推不倒,next(id_iter),8,{缺一门})
	花龙=Fanzhong(lang.花龙,next(id_iter),8,set())
	三风刻=Fanzhong(lang.三风刻,next(id_iter),12,set())
	小于五=Fanzhong(lang.小于五,next(id_iter),12,{无字})
	大于五=Fanzhong(lang.大于五,next(id_iter),12,{无字})
	组合龙=Fanzhong(lang.组合龙,next(id_iter),12,set())
	全不靠=Fanzhong(lang.全不靠,next(id_iter),12,{五门齐,门前清})
	三暗刻=Fanzhong(lang.三暗刻,next(id_iter),16,{双暗刻})
	三同刻=Fanzhong(lang.三同刻,next(id_iter),16,{双同刻})
	全带五=Fanzhong(lang.全带五,next(id_iter),16,{断幺})
	一色三步高=Fanzhong(lang.一色三步高,next(id_iter),16,set())
	三色双龙会=Fanzhong(lang.三色双龙会,next(id_iter),16,{平和,无字,喜相逢,老少副})
	清龙=Fanzhong(lang.清龙,next(id_iter),16,{连六,老少副})
	全小=Fanzhong(lang.全小,next(id_iter),24,{小于五,无字})
	全中=Fanzhong(lang.全中,next(id_iter),24,{断幺,无字})
	全大=Fanzhong(lang.全大,next(id_iter),24,{大于五,无字})
	一色三节高=Fanzhong(lang.一色三节高,next(id_iter),24,set())
	一色三同顺=Fanzhong(lang.一色三同顺,next(id_iter),24,{一色三节高,一般高})
	清一色=Fanzhong(lang.清一色,next(id_iter),24,{无字,缺一门})
	全双刻=Fanzhong(lang.全双刻,next(id_iter),24,{碰碰和,断幺})
	七星不靠=Fanzhong(lang.七星不靠,next(id_iter),24,{全不靠,五门齐,门前清})
	七对=Fanzhong(lang.七对,next(id_iter),24,{门前清,单调将})
	混幺九=Fanzhong(lang.混幺九,next(id_iter),32,{碰碰和,全带幺,幺九刻})
	三杠=Fanzhong(lang.三杠,next(id_iter),32,{双明杠,明杠})
	一色四步高=Fanzhong(lang.一色四步高,next(id_iter),32,{一色三步高,连六,老少副})
	一色四节高=Fanzhong(lang.一色四节高,next(id_iter),48,{一色三节高,一色三同顺,碰碰和})
	一色四同顺=Fanzhong(lang.一色四同顺,next(id_iter),48,{一色三同顺,一色三节高,四归一,一般高})
	一色双龙会=Fanzhong(lang.一色双龙会,next(id_iter),64,{七对,清一色,平和,无字,一般高,老少副})
	四暗刻=Fanzhong(lang.四暗刻,next(id_iter),64,{碰碰和,三暗刻})
	字一色=Fanzhong(lang.字一色,next(id_iter),64,{碰碰和,全带幺,幺九刻,缺一门})
	小三元=Fanzhong(lang.小三元,next(id_iter),64,{双箭刻,箭刻})
	小四喜=Fanzhong(lang.小四喜,next(id_iter),64,{三风刻,幺九刻})
	清幺九=Fanzhong(lang.清幺九,next(id_iter),64,{碰碰和,全带幺,幺九刻,无字})
	十三幺=Fanzhong(lang.十三幺,next(id_iter),88,{五门齐,门前清,单调将})
	连七对=Fanzhong(lang.连七对,next(id_iter),88,{七对,清一色,门前清,单调将})
	四杠=Fanzhong(lang.四杠,next(id_iter),88,{三杠,双明杠,明杠,单调将})
	九莲宝灯=Fanzhong(lang.九莲宝灯,next(id_iter),88,{清一色,门前清,幺九刻})
	绿一色=Fanzhong(lang.绿一色,next(id_iter),88,set())
	大三元=Fanzhong(lang.大三元,next(id_iter),88,{双箭刻,箭刻})
	大四喜=Fanzhong(lang.大四喜,next(id_iter),88,{三风刻,碰碰和,圈风刻,门风刻,幺九刻})

def output_pai(shoupai1:int,is_number_only=False):
	if not is_number_only:
		if shoupai1<30:
			return str(shoupai1%10)+('m','p','s')[shoupai1//10]
		else:
			return ('東','南','西','北','中','發','白')[shoupai1-31]
	else:
		return str(shoupai1)

def output_pais(shoupai1:list,is_number_only=False,traditional=False,end=""):
	if not is_number_only:
		has_wan=any(i in shoupai1 for i in range(1,10))
		has_bing=any(i in shoupai1 for i in range(11,20))
		has_tiao=any(i in shoupai1 for i in range(21,30))
		has_zipai=any(i in shoupai1 for i in range(31,38))
		for i in shoupai1:
			if i==None:
				pass
			elif 0<i<10:
				print(i,end="")
			elif 10<i<20:
				if has_wan:
					print("m",end=" ")
					has_wan=False
				print(i-10,end="")
			elif 20<i<30:
				if has_wan:
					print("m",end=" ")
					has_wan=False
				if has_bing:
					print("p",end=" ")
					has_bing=False
				print(i-20,end="")
			elif 30<i<38:
				if has_wan:
					print("m",end=" ")
					has_wan=False
				if has_bing:
					print("p",end=" ")
					has_bing=False
				if has_tiao:
					print("s",end=" ")
					has_tiao=False
				if not traditional:
					print(('東','南','西','北','中','發','白')[i-31],end="")
				else:
					print(i-30,end="")
		if has_wan:
			print("m",end="")
			has_wan=False
		if has_bing:
			print("p",end="")
			has_bing=False
		if has_tiao:
			print("s",end="")
			has_tiao=False
		if has_zipai and traditional:
			print("z",end="")
	else:
		for i in shoupai1:
			if i!=None:
				print(i,end="")
	print(end=end)

def fanzhong_and_output(shoupai9:list,hupaixing:list,did_mopai:bool,is_kongting:bool,mopai:int,dapai:int,is_number_only=False):
	fanzhong=[]
	if len(hupaixing)==13 and hupaixing[0][0]=='a' and hupaixing[1][0]=='b':
		fanzhong.append(十三幺)

	elif sum(shoupai9)<=14:
		fu_zuheguo=[False]*len(hupaixing)#组合过的副

		if all(['k',i,i,i] in hupaixing for i in (31,32,33,34)):
			fanzhong.append(大四喜)
			fu_zuheguo[1:]=[True]*4

		if all(['k',i,i,i] in hupaixing for i in (35,36,37)):
			fanzhong.append(大三元)
			for i in (35,36,37):
				fu_zuheguo[hupaixing.index(['k',i,i,i])]=True

		if sum(shoupai9)==14==sum(shoupai9[22:25])+shoupai9[26]+shoupai9[28]+shoupai9[36]:
			fanzhong.append(绿一色)

		if sum(shoupai9)==14 and any(shoupai9[i+1]>=3 and all(shoupai9[i+2:i+9]) and shoupai9[i+9]>=3 for i in (0,10,20)):
			if did_mopai==False:
				if mopai%10 in (1,9) and shoupai9[mopai]==4 or shoupai9[mopai]==2:
					fanzhong.append(九莲宝灯)

		if hupaixing[0][0]=='d' and any(shoupai9[i:i+7]==[2]*7 for i in (1,2,3,11,12,13,21,22,23)):
			fanzhong.append(连七对)

		if sum(shoupai9)==14 and all(i[0]=='a' or i[0]=='k' and i[1] in (1,9,11,19,21,29) for i in hupaixing):
			fanzhong.append(清幺九)

		if any(hupaixing[0]==['a',i,i,None] for i in range(31,35)) and all(hupaixing[0]==['a',i,i,None] or ['k',i,i,i] in hupaixing for i in range(31,35)):
			fanzhong.append(小四喜)

		if any(hupaixing[0]==['a',i,i,None] for i in range(35,38)) and all(hupaixing[0]==['a',i,i,None] or ['k',i,i,i] in hupaixing for i in range(35,38)):
			fanzhong.append(小三元)

		if sum(shoupai9)==14 and len(hupaixing)==5 and all(i[1]>30 for i in hupaixing):
			fanzhong.append(字一色)

		if sum(i[0]=='k' for i in hupaixing)==4:
			if did_mopai==False and mopai==hupaixing[0][1]:
				fanzhong.append(四暗刻)

		if any(hupaixing==[['a',5+i,5+i,None],['s',1+i,2+i,3+i],['s',1+i,2+i,3+i],['s',7+i,8+i,9+i],['s',7+i,8+i,9+i]] for i in (0,10,20)):
			fanzhong.append(一色双龙会)

		if sum(shoupai9)==14 and len(hupaixing)==5 and hupaixing[1][0]=='s' and hupaixing[1]==hupaixing[2]==hupaixing[3]==hupaixing[4]:
			fanzhong.append(一色四同顺)
			fu_zuheguo[1:]=[True]*4

		#32

		if any(all(['k',i,i,i] in hupaixing for i in range(j,j+4)) for j in range(27)):
			fanzhong.append(一色四节高)
			fu_zuheguo[1:]=[True]*4

		if any(all(['s',i,i+1,i+2] in hupaixing for i in range(j,j+4)) for j in range(25)) or \
		any(all(['s',i,i+1,i+2] in hupaixing for i in range(j,j+7,2)) for j in range(22)):
			fanzhong.append(一色四步高)
			fu_zuheguo[1:]=[True]*4

		if sum(shoupai9)==14 and all(i[0] in ('a','k') and i[1] in (1,9,11,19,21,29)+tuple(range(31,38)) for i in hupaixing) and 0<sum(shoupai9[31:])<14:
			fanzhong.append(混幺九)
			fu_zuheguo[1:]=[True]*4

		if hupaixing[0][0]=='d':
			fanzhong.append(七对)

		if hupaixing[0][0]=='b' and all(['b',i,None,None] in hupaixing for i in range(31,38)):
			fanzhong.append(七星不靠)

		if len(hupaixing)==5 and all(i[0] in ('a','k') and i[1]%2==0 and i[1]<30 for i in hupaixing):
			fanzhong.append(全双刻)

		if sum(shoupai9)==14 and (sum(shoupai9[1:10])==14 or sum(shoupai9[11:20])==14 or sum(shoupai9[21:30])==14):
			fanzhong.append(清一色)

		if len(hupaixing)>3:
			for fu_nums in combinations(tuple(range(1,len(hupaixing))),3):
				if sum(fu_zuheguo[1:])==3 and not all(fu_zuheguo[i] for i in fu_nums):
					pass
				else:
					hupaixing_part=[hupaixing[i] for i in fu_nums]

					if hupaixing_part[0][0]=='s' and hupaixing_part[0]==hupaixing_part[1]==hupaixing_part[2]:
						fanzhong.append(一色三同顺)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if any(all(['k',i,i,i] in hupaixing_part for i in range(j,j+3)) for j in range(27)):
						fanzhong.append(一色三节高)
						for i in fu_nums:
							fu_zuheguo[i]=True

		if sum(shoupai9)==14==sum(shoupai9[7:10]+shoupai9[17:20]+shoupai9[27:30]):
			fanzhong.append(全大)

		if sum(shoupai9)==14==sum(shoupai9[4:7]+shoupai9[14:17]+shoupai9[24:27]):
			fanzhong.append(全中)

		if sum(shoupai9)==14==sum(shoupai9[1:4]+shoupai9[11:14]+shoupai9[21:24]):
			fanzhong.append(全小)

		if hupaixing==[['a',5,5,None],['s',11,12,13],['s',17,18,19],['s',21,22,23],['s',27,28,29]] or \
		hupaixing==[['a',15,15,None],['s',1,2,3],['s',7,8,9],['s',21,22,23],['s',27,28,29]] or \
		hupaixing==[['a',25,25,None],['s',1,2,3],['s',7,8,9],['s',11,12,13],['s',17,18,19]]:
			fanzhong.append(三色双龙会)

		if all(any(j in i for j in (5,15,25)) for i in hupaixing):
			fanzhong.append(全带五)

		if len(hupaixing)>3:
			for fu_nums in combinations(tuple(range(1,len(hupaixing))),3):
				if sum(fu_zuheguo[1:])==3 and not all(fu_zuheguo[i] for i in fu_nums):
					pass
				else:
					hupaixing_part=[hupaixing[i] for i in fu_nums]

					if any(hupaixing_part==[['s',1+i,2+i,3+i],['s',4+i,5+i,6+i],['s',7+i,8+i,9+i]] for i in (0,10,20)):
						fanzhong.append(清龙)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if any(all(['s',i,i+1,i+2] in hupaixing_part for i in range(j,j+3)) for j in range(26)) or \
					any(all(['s',i,i+1,i+2] in hupaixing_part for i in range(j,j+5,2)) for j in range(24)):
						fanzhong.append(一色三步高)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if any(all(['k',j+i,j+i,j+i] in hupaixing_part for j in (0,10,20)) for i in range(1,10)):
						fanzhong.append(三同刻)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if sum(i[0]=='k' for i in hupaixing_part)==3:
						if did_mopai==False and any(mopai in hupaixing[i] for i in range(5) if i not in fu_nums):
							fanzhong.append(三暗刻)
							for i in fu_nums:
								fu_zuheguo[i]=True

		if hupaixing[0][0]=='b':
			fanzhong.append(全不靠)

			if sum(shoupai9[31:38])==5:
				fanzhong.append(组合龙)
				hupaixing[6:9]=[['z',hupaixing[6][1],hupaixing[7][1],hupaixing[8][1]]]
				hupaixing[3:6]=[['z',hupaixing[3][1],hupaixing[4][1],hupaixing[5][1]]]
				hupaixing[0:3]=[['z',hupaixing[0][1],hupaixing[1][1],hupaixing[2][1]]]

		if sum(shoupai9)==14==sum(shoupai9[6:10]+shoupai9[16:20]+shoupai9[26:30]):
			fanzhong.append(大于五)

		if sum(shoupai9)==14==sum(shoupai9[1:5]+shoupai9[11:15]+shoupai9[21:25]):
			fanzhong.append(小于五)

		if len(hupaixing)>3:
			for fu_nums in combinations(tuple(range(1,len(hupaixing))),3):
				if sum(fu_zuheguo[1:])==3 and not all(fu_zuheguo[i] for i in fu_nums):
					pass
				else:
					hupaixing_part=[hupaixing[i] for i in fu_nums]

					if all(i[0]=='z' for i in hupaixing_part):
						fanzhong.append(组合龙)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if all(any(i==['k',j,j,j] for j in range(31,35)) for i in hupaixing_part):
						fanzhong.append(三风刻)
						for i in fu_nums:
							fu_zuheguo[i]=True

		if sum(shoupai9)==14==sum(shoupai9[11:16]+shoupai9[18:20]+shoupai9[22:27]+shoupai9[28:30]+shoupai9[37:38]):
			fanzhong.append(推不倒)

		if len(hupaixing)>3:
			for fu_nums in combinations(tuple(range(1,len(hupaixing))),3):
				if sum(fu_zuheguo[1:])==3 and not all(fu_zuheguo[i] for i in fu_nums):
					pass
				else:
					hupaixing_part=[hupaixing[i] for i in fu_nums]

					if hupaixing_part[0][0]==hupaixing_part[1][0]==hupaixing_part[2][0]=='s' and \
					{hupaixing_part[0][1]%10,hupaixing_part[1][1]%10,hupaixing_part[2][1]%10}=={1,4,7} and \
					{hupaixing_part[0][1]//10,hupaixing_part[1][1]//10,hupaixing_part[2][1]//10}=={0,1,2}:
						fanzhong.append(花龙)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if any(all(['s',i+j,i+1+j,i+2+j] in hupaixing_part for j in (0,10,20)) for i in range(1,8)):
						fanzhong.append(三色三同顺)
						for i in fu_nums:
							fu_zuheguo[i]=True

					if hupaixing_part[0][0]==hupaixing_part[1][0]==hupaixing_part[2][0]=='k' and \
					any({hupaixing_part[0][1]%10,hupaixing_part[1][1]%10,hupaixing_part[2][1]%10}=={i,i+1,i+2} for i in range(8)) and \
					{hupaixing_part[0][1]//10,hupaixing_part[1][1]//10,hupaixing_part[2][1]//10}=={0,1,2}:
						fanzhong.append(三色三节高)
						for i in fu_nums:
							fu_zuheguo[i]=True

		if len(hupaixing)==5 and all(i[0]=='k' for i in hupaixing[1:]):
			fanzhong.append(碰碰和)

		if sum(shoupai9)==14 and 0<sum(shoupai9[31:])<14 and (not any(shoupai9[11:30]) or not any(shoupai9[1:10]+shoupai9[21:30]) or not any(shoupai9[1:20])):
			fanzhong.append(混一色)

		if all((any(shoupai9[1:10]),any(shoupai9[11:20]),any(shoupai9[21:30]),any(shoupai9[31:35]),any(shoupai9[35:58]))):
			fanzhong.append(五门齐)

		if len(hupaixing)>3:
			for fu_nums in combinations(tuple(range(1,len(hupaixing))),3):
				if sum(fu_zuheguo[1:])==3 and not all(fu_zuheguo[i] for i in fu_nums):
					pass
				else:
					hupaixing_part=[hupaixing[i] for i in fu_nums]

					if hupaixing_part[0][0]==hupaixing_part[1][0]==hupaixing_part[2][0]=='s' and \
					any({hupaixing_part[0][1]%10,hupaixing_part[1][1]%10,hupaixing_part[2][1]%10}=={i,i+1,i+2} for i in range(6)) and \
					{hupaixing_part[0][1]//10,hupaixing_part[1][1]//10,hupaixing_part[2][1]//10}=={0,1,2}:
						fanzhong.append(三色三步高)
						for i in fu_nums:
							fu_zuheguo[i]=True

		if len(hupaixing)==5 and all(any(j in i for j in (1,11,21,9,19,29)+tuple(range(31,38))) for i in hupaixing):
			fanzhong.append(全带幺)

		if any(['k',i,i,i] in hupaixing for i in (35,36,37)):
			fanzhong.append(箭刻)

		if any(['k',i,i,i] in hupaixing for i in range(31,35)):
			fanzhong.append(圈风刻)
			fanzhong.append(门风刻)

		if len(hupaixing)==5 and all(i[0] in ('a','s','z') for i in hupaixing) and sum(shoupai9[31:])==0:
			fanzhong.append(平和)

		for i in range(38):
			if shoupai9[i]==4:
				fanzhong.append(四归一)

		if sum(shoupai9)==14 and not shoupai9[1] and not shoupai9[9] and not shoupai9[11] and not shoupai9[19] and not shoupai9[21] and not shoupai9[29] and not any(shoupai9[31:]):
			fanzhong.append(断幺)

		taosuanyici_flag=None
		fu_shangweizuhe=None
		if len(hupaixing)>2:
			for fu_nums in combinations(tuple(range(1,len(hupaixing))),2):
				if len(hupaixing)==5 and not taosuanyici_flag and sum(fu_zuheguo[1:])==3:
					fu_shangweizuhe=next(i for i in range(1,len(hupaixing)) if not fu_zuheguo[i])
					taosuanyici_flag=False
				hupaixing_part=[hupaixing[i] for i in fu_nums]
				if not taosuanyici_flag or fu_shangweizuhe not in fu_nums:

					if hupaixing_part[0][0]=='k' and hupaixing_part[0][1]>34 and hupaixing_part[1][1]>34:
						fanzhong.append(双箭刻)
						for i in fu_nums:
							fu_zuheguo[i]=True
						if fu_shangweizuhe in fu_nums:
							taosuanyici_flag=True
							continue

					if hupaixing_part[0][0]==hupaixing_part[1][0]=='k' and hupaixing_part[0][1]%10==hupaixing_part[1][1]%10 and hupaixing_part[0][1]//10!=hupaixing_part[1][1]//10 and hupaixing_part[0][1]<30>hupaixing_part[1][1]:
						fanzhong.append(双同刻)
						for i in fu_nums:
							fu_zuheguo[i]=True
						if fu_shangweizuhe in fu_nums:
							taosuanyici_flag=True
							continue

					if sum(i[0]=='k' for i in hupaixing_part)>=2:
						if did_mopai==False and any(mopai in hupaixing[i] for i in range(5) if i not in fu_nums):
							fanzhong.append(双暗刻)
							for i in fu_nums:
								fu_zuheguo[i]=True
							if fu_shangweizuhe in fu_nums:
								taosuanyici_flag=True
								continue

					if hupaixing_part[0]==hupaixing_part[1] and hupaixing_part[0][0]==hupaixing_part[1][0]=='s':
						fanzhong.append(一般高)
						for i in fu_nums:
							fu_zuheguo[i]=True
						if fu_shangweizuhe in fu_nums:
							taosuanyici_flag=True
							continue

					if hupaixing_part[0][0]==hupaixing_part[1][0]=='s' and hupaixing_part[0][1]%10==hupaixing_part[1][1]%10 and hupaixing_part[0][1]//10!=hupaixing_part[1][1]//10:
						if 喜相逢 in fanzhong and any(i in 喜相逢_fu for i in fu_nums):
							pass
						else:
							fanzhong.append(喜相逢)
							喜相逢_fu=fu_nums
							for i in fu_nums:
								fu_zuheguo[i]=True
							if fu_shangweizuhe in fu_nums:
								taosuanyici_flag=True
								continue

					if 清龙 not in fanzhong and hupaixing_part[0][0]==hupaixing_part[1][0]=='s' and hupaixing_part[0][1]+3==hupaixing_part[1][1]:
						if 连六 in fanzhong and any(i in 连六_fu for i in fu_nums):
							pass
						else:
							fanzhong.append(连六)
							连六_fu=fu_nums
							for i in fu_nums:
								fu_zuheguo[i]=True
							if fu_shangweizuhe in fu_nums:
								taosuanyici_flag=True
								continue

					if 清龙 not in fanzhong and hupaixing_part[0][0]==hupaixing_part[1][0]=='s' and hupaixing_part[0][1]%10==1 and hupaixing_part[1][1]%10==7 and hupaixing_part[0][1]//10==hupaixing_part[1][1]//10:
						if 老少副 in fanzhong and any(i in 老少副_fu for i in fu_nums):
							pass
						else:
							fanzhong.append(老少副)
							老少副_fu=fu_nums
							for i in fu_nums:
								fu_zuheguo[i]=True
							if fu_shangweizuhe in fu_nums:
								taosuanyici_flag=True
								continue

		fanzhong.extend([幺九刻]*sum(['k',i,i,i] in hupaixing for i in (1,9,11,19,21,29)))

		if sum(shoupai9)==14 and (sum(shoupai9[:10])==0 or sum(shoupai9[11:20])==0 or sum(shoupai9[21:30])==0):
			fanzhong.append(缺一门)

		if sum(shoupai9)==14 and sum(shoupai9[31:])==0:
			fanzhong.append(无字)

		if (mopai%10==3 and any(mopai==i[3] for i in hupaixing if i[0]=='s') and ['s',mopai,mopai+1,mopai+2] not in hupaixing and not ['a',mopai-1,mopai-1,None] in hupaixing) or \
		(mopai%10==7 and any(mopai==i[1] for i in hupaixing if i[0]=='s') and ['s',mopai-2,mopai-1,mopai] not in hupaixing and not ['a',mopai+1,mopai+1,None] in hupaixing) and \
		did_mopai==False:
			fanzhong.append(边张)

		if did_mopai==False and \
		(any(mopai==i[2] for i in hupaixing if i[0]=='s') and ['s',mopai-2,mopai-1,mopai] not in hupaixing and not ['s',mopai,mopai+1,mopai+2] in hupaixing and ['a',mopai-1,mopai-1,None] not in hupaixing and ['a',mopai+1,mopai+1,None] not in hupaixing):
			fanzhong.append(坎张)

		if did_mopai==False and \
		(any(mopai==i[1] for i in hupaixing if i[0]=='a') and ['s',mopai+1,mopai+2,mopai+3] not in hupaixing and ['s',mopai-3,mopai-2,mopai-1] not in hupaixing and ['s',mopai,mopai+1,mopai+2] not in hupaixing and ['s',mopai-2,mopai-1,mopai] not in hupaixing and (['k',mopai-1,mopai-1,mopai-1] not in hupaixing and ['k',mopai+1,mopai+1,mopai+1] not in hupaixing or mopai>30) and (['k',mopai-2,mopai-2,mopai-2] not in hupaixing or mopai>30) and (['k',mopai+2,mopai+2,mopai+2] not in hupaixing or mopai>28)):
			fanzhong.append(单调将)

	#calculate
	buji=set()
	for i in fanzhong:
		buji.update(i.buji)
	fanzhong_=[]
	for i in fanzhong:
		if i not in buji:
			fanzhong_.append(i)
	fanzhong_.sort(key=lambda elem: (elem.id))
	fenshu=sum(i.fenshu for i in fanzhong_)

	#output
	if dapai:
		print(lang.打,"["+output_pai(dapai,is_number_only)+"]",end=" ")
	if did_mopai:
		print(lang.和牌+" | ",end="")
	elif did_mopai==False and is_kongting:
		print(lang.空听,"["+output_pai(mopai,is_number_only),end="] | ")
	elif did_mopai==False and not is_kongting:
		print(lang.听牌,"["+output_pai(mopai,is_number_only),end="] | ")
	for j in hupaixing:
		output_pais(j[1:],is_number_only,True," ")
	print("|",end="")
	if fenshu>0:
		print(str(fenshu).rjust(3)+lang.分,end=lang.冒号)
	print(lang.顿号.join([i.name+"("+str(i.fenshu)+")" for i in fanzhong_]))

	return fenshu

def main(shoupai=None,shoupai1=None,dapai=False,is_number_only=False):
	global lang
	#input shoupai
	if shoupai1==None:
		if shoupai==None:
			try:
				shoupai=input(lang.输入手牌+lang.冒号)
				shoupai_lower=shoupai.lower()
			except:
				print("ERROR")
				return
			if shoupai_lower in ("exit","退出"):
				sys.exit()
			elif shoupai_lower in ("help","帮助","幫助"):
				print()
				print(lang.帮助)
				return
			elif shoupai_lower in ("about","关于"):
				print()
				print("胡祥又 Hu Xiangyou")
				print("chinese version 1.0")
				print()
				print("version 0.0 December 17, 2018")
				print("version 1.0 February 9, 2019")
				print("version 1.1 February 20, 2019")
				print("version 1.2 March 20, 2019")
				print("version 2.0 April 14, 2019")
				print("chinese version 0.0 April 30, 2019")
				print("chinese version 1.0 June 14, 2019")
				return
			elif shoupai_lower in ("example","examples","举例","舉例","例","test","tests","测试","測試"):
				main(shoupai=test.test())
				return

		for i in (' ','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~','　'):
			shoupai=shoupai.replace(i,'')
		if shoupai=='':
			return

		#manage shoupai
		shoupai1=[]
		huase_now=None
		huase_used=True
		invalid_inputs=[]
		#number only
		if shoupai.isdecimal():
			is_number_only=True
			if '0' in shoupai:
				invalid_inputs.append('0')
			shoupai1=[int(i) if i!='0' else 5 for i in shoupai]
		else:
			shoupai=shoupai[::-1]
			for shoupai_i in shoupai:
				if shoupai_i in ('E','Ｅ','東','东'):
					shoupai1.append(31)
				elif shoupai_i in ('S','Ｓ','南'):
					shoupai1.append(32)
				elif shoupai_i in ('W','Ｗ','西'):
					shoupai1.append(33)
				elif shoupai_i in ('N','Ｎ','北'):
					shoupai1.append(34)
				elif shoupai_i in ('C','Ｃ','中'):
					shoupai1.append(35)
				elif shoupai_i in ('F','H','R','Ｆ','Ｈ','Ｒ','發','発','发'):
					shoupai1.append(36)
				elif shoupai_i in ('P','D','Ｐ','Ｄ','白'):
					shoupai1.append(37)
				elif shoupai_i in ('m','w','ｍ','ｗ','万' ,'萬'):
					if not huase_used:
						invalid_inputs.insert(0,('m','p','s','z')[huase_now])
					huase_now=0
					huase_used=False
				elif shoupai_i in ('p','ｐ','b','ｂ','餠','餅','筒','饼'):
					if not huase_used:
						invalid_inputs.insert(0,('m','p','s','z')[huase_now])
					huase_now=1
					huase_used=False
				elif shoupai_i in ('s','ｓ','索','条','條'):
					if not huase_used:
						invalid_inputs.insert(0,('m','p','s','z')[huase_now])
					huase_now=2
					huase_used=False
				elif shoupai_i in ('z','ｚ','字'):
					if not huase_used:
						invalid_inputs.insert(0,('m','p','s','z')[huase_now])
					huase_now=3
					huase_used=False
				elif shoupai_i.isdecimal():
					if huase_now!=None:
						if shoupai_i=='0' and huase_now in (0,1,2):
							shoupai1.append(5+huase_now*10)
							invalid_inputs.insert(0,'0'+('m','p','s')[huase_now])
							huase_used=True
						elif shoupai_i in ('0','8','9') and huase_now==3:
							invalid_inputs.insert(0,shoupai_i+'z')
							huase_used=True
						else:
							shoupai1.append(int(shoupai_i)+huase_now*10)
						huase_used=True
					else:
						invalid_inputs.insert(0,shoupai_i)
				else:
					if not huase_used:
						invalid_inputs.insert(0,('m','p','s','z')[huase_now])
						huase_used=True
					invalid_inputs.insert(0,shoupai_i)
			if huase_used==False:
				invalid_inputs.insert(0,('m','p','s','z')[huase_now])

		if invalid_inputs:
			print(lang.含有无效输入,end=lang.冒号)
			for i in invalid_inputs:
				print(i,end=" ")
			print()

	shoupai1.sort()

	#count shoupai
	number_of_pai=len(shoupai1)
	shoupai9=[0]*38
	for i in shoupai1:
		shoupai9[i]+=1

	if number_of_pai==0:
		print()
		return

	#show shoupai
	if not dapai:
		print()
		print(lang.手牌,end=lang.冒号)
		output_pais(shoupai1,is_number_only,False,"\n\n")
		
		if any(i>4 for i in shoupai9):
			print(lang.多于4张.format(lang.顿号.join((output_pai(i,is_number_only) for i in range(10 if is_number_only else 38) if shoupai9[i]>4))))

		if number_of_pai>14:
			print(lang.多于14张.format(str(number_of_pai)))
			print()
		if number_of_pai<13:
			print(lang.少于13张.format(str(number_of_pai)))
			print()

	number_of_fu=number_of_pai//3
	is_tingpai=False
	zuigaofen=[]

	if number_of_pai%3==2:
		did_mopai=True
	elif number_of_pai%3==1:
		did_mopai=False
		number_of_pai+=1
		huliaopais=[]
	elif number_of_pai%3==0:
		did_mopai=None
		print(lang.相公.format(str(number_of_pai)))
		return

	if not dapai and 50<number_of_pai:
		if input(lang.手牌过多)!='':
			return
	start_time=time.time()

	for mopai in range(1,10 if is_number_only else 38):
		if mopai%10==0:
			continue

		is_kongting=False
		if did_mopai==False:
			shoupai9[mopai]+=1
			if shoupai9[mopai]==5:
				is_kongting=True

		is_hupai=False
		hupaixings=[]
		dianshu=[]

		#十三幺
		if number_of_pai==14 and not any(shoupai9[2:9]) and not any(shoupai9[12:19]) and not any(shoupai9[22:29]) and shoupai9[1] and shoupai9[9] and shoupai9[11] and shoupai9[19] and shoupai9[21] and shoupai9[29] and all(shoupai9[31:]):
			is_hupai=True
			hupaixings.append([['a',shoupai9.index(2),shoupai9.index(2),None]]+[['b',i,None,None] for i in range(38) if shoupai9[i]==1])
			dianshu.append(fanzhong_and_output(shoupai9,hupaixings[-1],did_mopai,is_kongting,mopai,dapai,is_number_only))

		#七对
		if number_of_pai==14 and sum((shoupai9.count(2*i)*i for i in range(1,8)))==7:
			is_hupai=True
			hupaixings.append([['d',shoupai1[i],shoupai1[i],None] for i in range(0,13,2)])
			dianshu.append(fanzhong_and_output(shoupai9,hupaixings[-1],did_mopai,is_kongting,mopai,dapai,is_number_only))

		#全不靠
		if number_of_pai==14 and not any(i>1 for i in shoupai9):
			if not any(shoupai9[i] for i in (2,3,5,6,8,9,10,11,13,14,16,17,19,20,21,22,24,25,27,28)) or \
			not any(shoupai9[i] for i in (2,3,5,6,8,9,10,11,12,14,15,17,18,20,21,23,24,26,27,29)) or \
			not any(shoupai9[i] for i in (1,3,4,6,7,9,10,12,13,15,16,18,19,20,21,22,24,25,27,28)) or \
			not any(shoupai9[i] for i in (1,3,4,6,7,9,10,11,12,14,15,17,18,20,22,23,25,26,28,29)) or \
			not any(shoupai9[i] for i in (1,2,4,5,7,8,10,12,13,15,16,18,19,20,21,23,24,26,27,29)) or \
			not any(shoupai9[i] for i in (1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29)):
				is_hupai=True
				hupaixings.append([['b',i,None,None] for i in range(38) if shoupai9[i]])
				dianshu.append(fanzhong_and_output(shoupai9,hupaixings[-1],did_mopai,is_kongting,mopai,dapai,is_number_only))

		#analyse shoupai
		#jiangpai
		for jiangpai_i in range(10 if is_number_only else 38):
			if shoupai9[jiangpai_i]>=2:
				hupaixing_temp=[['a',jiangpai_i,jiangpai_i,None]]
				shoupai9_temp=shoupai9.copy()
				shoupai9_temp[jiangpai_i]-=2
			else:
				continue

			#fu (副)
			for fu_i in range(number_of_fu+1):
				if shoupai9_temp==None:
					break
				elif sum(shoupai9_temp)==0:
					is_hupai=True
					hupaixing_temp.sort()
					if hupaixing_temp not in hupaixings:
						hupaixings.append(hupaixing_temp)
						dianshu.append(fanzhong_and_output(shoupai9,hupaixing_temp,did_mopai,is_kongting,mopai,dapai,is_number_only))
						#if sanlianke then change to 3-shunzi
						hupaixing_new_num=1
						while hupaixing_new_num:
							hupaixing_new_num_temp=hupaixing_new_num
							hupaixing_new_num=0
							for hupaixing_i in hupaixings[-hupaixing_new_num_temp:]:
								for fu_picked_i in hupaixing_i[1:]:
									if fu_picked_i[0]=='k':
										kezi_hai=fu_picked_i[1]
										if kezi_hai%10<=7 and kezi_hai<30 and ['k',kezi_hai+1,kezi_hai+1,kezi_hai+1] in hupaixing_i and ['k',kezi_hai+2,kezi_hai+2,kezi_hai+2] in hupaixing_i:
											hupaixing_temp=hupaixing_i.copy()
											hupaixing_temp.remove(fu_picked_i)
											hupaixing_temp.remove(['k',kezi_hai+1,kezi_hai+1,kezi_hai+1])
											hupaixing_temp.remove(['k',kezi_hai+2,kezi_hai+2,kezi_hai+2])
											hupaixing_temp.extend([['s',kezi_hai,kezi_hai+1,kezi_hai+2]]*3)
											hupaixing_temp.sort()
											if hupaixing_temp not in hupaixings:
												hupaixings.append(hupaixing_temp)
												hupaixing_new_num+=1
												dianshu.append(fanzhong_and_output(shoupai9,hupaixing_temp,did_mopai,is_kongting,mopai,dapai,is_number_only))
					continue
				for hai_picked in range(10 if is_number_only else 38):
					if shoupai9_temp[hai_picked]==0:
						continue
					elif shoupai9_temp[hai_picked]>=3:#kezi exists
						shoupai9_temp[hai_picked]-=3
						hupaixing_temp.append(['k',hai_picked,hai_picked,hai_picked])
						break
					elif hai_picked<28 and all(shoupai9_temp[hai_picked:hai_picked+3]):#shunzi exists
						shoupai9_temp[hai_picked]-=1
						shoupai9_temp[hai_picked+1]-=1
						shoupai9_temp[hai_picked+2]-=1
						hupaixing_temp.append(['s',hai_picked,hai_picked+1,hai_picked+2])
						break
					elif hai_picked<4:#zuhelong-shunzi
						if all(shoupai9_temp[i] for i in (1,4,7,12,15,18,23,26,29)):
							shoupai9_temp[1]-=1
							shoupai9_temp[4]-=1
							shoupai9_temp[7]-=1
							shoupai9_temp[12]-=1
							shoupai9_temp[15]-=1
							shoupai9_temp[18]-=1
							shoupai9_temp[23]-=1
							shoupai9_temp[26]-=1
							shoupai9_temp[29]-=1
							hupaixing_temp.extend([['z',1,4,7],['z',12,15,18],['z',23,26,29]])
						elif all(shoupai9_temp[i] for i in (1,4,7,13,16,19,22,25,28)):
							shoupai9_temp[1]-=1
							shoupai9_temp[4]-=1
							shoupai9_temp[7]-=1
							shoupai9_temp[13]-=1
							shoupai9_temp[16]-=1
							shoupai9_temp[19]-=1
							shoupai9_temp[22]-=1
							shoupai9_temp[25]-=1
							shoupai9_temp[28]-=1
							hupaixing_temp.extend([['z',1,4,7],['z',13,16,19],['z',22,25,28]])
						elif all(shoupai9_temp[i] for i in (2,5,8,11,14,17,23,26,29)):
							shoupai9_temp[2]-=1
							shoupai9_temp[5]-=1
							shoupai9_temp[8]-=1
							shoupai9_temp[11]-=1
							shoupai9_temp[14]-=1
							shoupai9_temp[17]-=1
							shoupai9_temp[23]-=1
							shoupai9_temp[26]-=1
							shoupai9_temp[29]-=1
							hupaixing_temp.extend([['z',2,5,8],['z',11,14,17],['z',23,26,29]])
						elif all(shoupai9_temp[i] for i in (2,5,8,13,16,19,21,24,27)):
							shoupai9_temp[2]-=1
							shoupai9_temp[5]-=1
							shoupai9_temp[8]-=1
							shoupai9_temp[13]-=1
							shoupai9_temp[16]-=1
							shoupai9_temp[19]-=1
							shoupai9_temp[21]-=1
							shoupai9_temp[24]-=1
							shoupai9_temp[27]-=1
							hupaixing_temp.extend([['z',2,5,8],['z',13,16,19],['z',21,24,27]])
						elif all(shoupai9_temp[i] for i in (3,6,9,11,14,17,22,25,28)):
							shoupai9_temp[3]-=1
							shoupai9_temp[6]-=1
							shoupai9_temp[9]-=1
							shoupai9_temp[11]-=1
							shoupai9_temp[14]-=1
							shoupai9_temp[17]-=1
							shoupai9_temp[22]-=1
							shoupai9_temp[25]-=1
							shoupai9_temp[28]-=1
							hupaixing_temp.extend([['z',3,6,9],['z',11,14,17],['z',22,25,28]])
						elif all(shoupai9_temp[i] for i in (3,6,9,12,15,18,21,24,27)):
							shoupai9_temp[3]-=1
							shoupai9_temp[6]-=1
							shoupai9_temp[9]-=1
							shoupai9_temp[12]-=1
							shoupai9_temp[15]-=1
							shoupai9_temp[18]-=1
							shoupai9_temp[21]-=1
							shoupai9_temp[24]-=1
							shoupai9_temp[27]-=1
							hupaixing_temp.extend([['z',3,6,9],['z',12,15,18],['z',21,24,27]])
						else:#no zuhelong-shunzi exists
							shoupai9_temp=None
							break
					else:#neither kezi nor shunzi nor zuhelong-shunzi exists
						shoupai9_temp=None
						break

		if did_mopai==False and is_hupai:
			is_tingpai=True
			if not is_kongting:
				huliaopais.append(mopai)
				zuigaofen.append(max(dianshu))

		if did_mopai and not is_hupai:
			print(lang.没有和牌)
			#dapai
			for dapai_i in range(10 if is_number_only else 38):
				if dapai_i in shoupai1:
					shoupai1_new=shoupai1.copy()
					shoupai1_new.remove(dapai_i)
					main(shoupai1=shoupai1_new,dapai=dapai_i,is_number_only=is_number_only)

		if did_mopai:
			break
		if did_mopai==False:
			shoupai9[mopai]-=1

	#is_tingpai
	if not dapai and is_tingpai and huliaopais:
		print()
		print(lang.听牌,end=lang.冒号)
		if not is_number_only:
			huliaopai_fan=list(zip(huliaopais,zuigaofen))
			huliaopai_fan.sort(key=lambda elem: (elem[1],elem[0]))

			for huliaopai_fan_i in range(len(huliaopai_fan)):
				print(output_pai(huliaopai_fan[huliaopai_fan_i][0],is_number_only),end=" ")
				if(huliaopai_fan_i!=len(huliaopai_fan)-1 and huliaopai_fan[huliaopai_fan_i][1]!=huliaopai_fan[huliaopai_fan_i+1][1]) or huliaopai_fan_i==len(huliaopai_fan)-1 and number_of_pai<=14:
					print("("+str(huliaopai_fan[huliaopai_fan_i][1])+lang.分,end=") ")
		else:
			for huliaopai_i in huliaopais:
				print(output_pai(huliaopai_i,is_number_only),end=" ")
		print()

	if not dapai and did_mopai==False and not is_tingpai:
		print(lang.没有听牌)

	#time spent
	end_time=time.time()
	time_spent=end_time-start_time
	if not dapai and time_spent>1.0:
		print(lang.计算耗时.format(round(time_spent,1)))

while True:
	main()
	print("\n**************\n")

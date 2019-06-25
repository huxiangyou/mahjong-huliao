# 麻将和了吗？

## 概况

![version: 1.0](https://img.shields.io/badge/version-1.0-lightgrey.svg)
![python 3.7.3](https://img.shields.io/badge/python-3.7.3-blue.svg?logo=python)  
![tests: passed](https://img.shields.io/badge/tests-passed-brightgreen.svg)
![checks: passed](https://img.shields.io/badge/checks-passed-brightgreen.svg)
![build: passing](https://img.shields.io/badge/build-passing-brightgreen.svg)  
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php)

此应用程序的功能是查看国标麻将中手牌的听牌及和牌的情况。

`version 0.0` 胡祥又写于2018年12月17日；  
`version 1.0` 胡祥又写于2019年2月9日；  
`version 1.1` 胡祥又写于2019年2月20日；  
`version 1.2` 胡祥又写于2019年3月20日；  
`version 2.0` 胡祥又写于2019年4月14日；  
`version 2.1` 胡祥又写于2019年6月6日。  
`chinese version 0.0` 胡祥又写于2019年4月30日；  
`chinese version 1.0` 胡祥又写于2019年6月14日。

## 注意

* 此说明文件较为简陋。其中存在与[日本麻将的同程序](https://github.com/huxiangyou/mahjong-hoora)大量相似内容，详情请查看[日本麻将的同名文件](https://github.com/huxiangyou/mahjong-hoora/blob/master/README.md)。

## 番种的判断

由于计算机制的问题，部分番种不能被判断。

| 番种系列和类型 | 能完全判断的 | 输入是听牌型时可能能判断的<br>（知道和了牌时可能能判断的） | 只能判断为“可能存在”的 | 完全不能判断的 |
|:--:|:--:|:--:|:--:|:--:|
| 字牌系列 | 大四喜(88)<br>大三元(88)<br>小四喜(64)<br>小三元(64)<br>字一色(64)<br>三风刻(12)<br>双箭刻(6)<br>箭刻(2) |  | 圈风刻(2)<br>门风刻(2) |  |
| 步步高类 | 一色四步高(32)<br>一色三步高(16)<br>三色三步高(6)<br>平和(2) |  |  |  |
| 同顺类 | 一色四同顺(48)<br>一色三同顺(24)<br>三色三同顺(8)<br>一般高(1)<br>喜相逢(1) |  |  |  |
| 龙类 | 清龙(16)<br>组合龙(12)<br>花龙(8)<br>连六(1) |  |  |  |
| 老少类 | 一色双龙会(64)<br>三色双龙会(16)<br>老少副(1) |  |  |  |
| 刻类 | 清幺九(64)<br>一色四节高(48)<br>混幺九(32)<br>一色三节高(24)<br>全双刻(24)<br>三同刻(16)<br>三色三节高(8)<br>碰碰和(6)<br>双同刻(2)<br>幺九刻(1) |  | 四暗刻(64)<br>三暗刻(16)<br>双暗刻(2) |  |
| 杠类 |  |  |  | 四杠(88)<br>三杠(32)<br>双暗杠(8)<br>双明杠(4)<br>暗杠(2)<br>明杠(1) |
| 七对系列 | 连七对(88)<br>七对(24) |  |  |  |
| 花色组合系列 | 绿一色(88)<br>九莲宝灯(88)<br>清一色(24)<br>五门齐(6)<br>混一色(6)<br>缺一门(1)<br>无字(1) |  |  |  |
| 全带系列 | 全大(24)<br>全中(24)<br>全小(24)<br>全带五(16)<br>大于五(12)<br>小于五(12)<br>全带幺(4) |  |  |  |
| 不靠系列 | 七星不靠(24)<br>全不靠(12) |  |  |  |
| 和牌方式系列 | 断幺(2) | 边张(1)<br>坎张(1)<br>单调将(1) |  | 杠上开花(8)<br>抢杠和(8)<br>妙手回春(8)<br>海底捞月(8)<br>全求人(6)<br>不求人(4)<br>和绝张(4)<br>门前清(2)<br>自摸(1) |
| 特殊系列 | 推不倒(8)<br>四归一(2) |  | 无番和(8) | 花牌(1) |

## 国标的规定

国际标准麻将中，有部分规定自相矛盾，也有很多内容与很多时候实际执行的情况不同。现列如下：

| 涉及番种或规定 | 国标规定 | 实际执行 | 备注 |
|:--:|:--:|:--:|:--:|
| 字一色(64) | 由字牌的刻子（杠）、将牌组成的和牌。不计碰碰和、幺九刻。 | 由字牌组成的和牌。不计碰碰和、幺九刻，加计七对。 | 字一色不一定是碰碰和，也可能是七对，同时也不一定含有幺九刻。国标中，字一色七对子只能计七对(24)、缺一门(1)；实际执行中，则认为字一色的“一般情况”为碰碰和，也不加计幺九刻，但加计七对。 |

在本程序中，`mahjong-chinese-std.py`为标准的2014年版国标麻将的算法，而`mahjong-chinese`为常用算法。

## 问题

如果你发现了其他问题，请在[Issues](https://github.com/huxiangyou/mahjong-huliao/issues)中报告。

你可以使用中文、英语或日语报告。  
You can use Chinese, English or Japanese to report.  
中国語、英語、または日本語で報告してください。

## 许可

[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php)

此程序使用[MIT许可协议](https://opensource.org/licenses/mit-license.php)授权。

import math


def calPay(beforeValue, yanglao=8, yiliao=2, shiye=0.5, gongjijin=7):
    beforeValue = float(beforeValue)
    yanglao = beforeValue * yanglao / 100
    yiliao = beforeValue * yiliao / 100
    shiye = beforeValue * shiye / 100
    gongjijin = min(beforeValue * gongjijin / 100, 1145)
    needTaxValue = beforeValue - (yanglao + yiliao + shiye + gongjijin) - 3500  # 需要缴纳个税的部分
    taxValue = 0  # 需要缴纳的个税

    smartDict = {1500: {'tax': 0.03, 'smartValue': 0},
                 4500: {'tax': 0.10, 'smartValue': 105},
                 9000: {'tax': 0.20, 'smartValue': 555},
                 35000: {'tax': 0.25, 'smartValue': 1005},
                 55000: {'tax': 0.30, 'smartValue': 2755},
                 80000: {'tax': 0.35, 'smartValue': 5505},
                 'INFINITY': {'tax': 0.40, 'smartValue': 13505}}
    if needTaxValue <= 1500:
        taxValue = needTaxValue * smartDict[1500]['tax'] - smartDict[1500]['smartValue']
    elif needTaxValue <= 4500:
        taxValue = needTaxValue * smartDict[4500]['tax'] - smartDict[4500]['smartValue']
    elif needTaxValue <= 9000:
        taxValue = needTaxValue * smartDict[9000]['tax'] - smartDict[9000]['smartValue']
    elif needTaxValue <= 35000:
        taxValue = needTaxValue * smartDict[35000]['tax'] - smartDict[35000]['smartValue']
    elif needTaxValue <= 55000:
        taxValue = needTaxValue * smartDict[55000]['tax'] - smartDict[55000]['smartValue']
    elif needTaxValue <= 80000:
        taxValue = needTaxValue * smartDict[80000]['tax'] - smartDict[80000]['smartValue']
    else:
        taxValue = needTaxValue * smartDict['INFINITY']['tax'] - smartDict['INFINITY']['smartValue']

    resultAmount = needTaxValue - taxValue + 3500;
    print('养老保险个人缴纳', yanglao)
    print('医疗保险个人缴纳', yiliao)
    print('失业保险个人缴纳', shiye)
    print('公积金个人缴纳', gongjijin)
    print('个人所得税缴纳', taxValue, end='\n\n')

    print('您的税后工资', resultAmount);

calPay(input('请输入您的税前工资：'))

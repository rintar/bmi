#coding: utf-8

while True:
    height = raw_input('身長(m)?:')
    if len(height) == 0:
        break                                   # Enterキーだけが押された場合は終了
    height = float(height)                      # 入力は文字列なので、小数に変換
    weight = float(raw_input('体重(kg)?:'))
    bmi = weight / pow(height, 2)               # 組み込み関数powで累乗を計算

    print('BMI値は%0.1fです。' % bmi)             # 小数点以下第１位までの出力にフォーマットしています
    if bmi < 18.5:
        print('少しやせすぎです。')
    elif 18.5 <= bmi < 25.0:
        print('標準的な体型です。')
    elif 25.0 <= bmi < 30.0:
        print('少し太っています。')
    else:
        print('高度の肥満です。')

### 台文語料庫
中研院資訊所高明達老師所收集的「中央研究院台語語音語料庫系統」
網址：<http://140.109.18.117/>

## 設定環境
```
virtualenv venv --python=python3
source venv/bin/activate 
pip install tai5-uan5_gian5-gi2_kang1-ku7
```

## 處理標音
```
python 補全漢全羅/做辭典.py
PYTHONPATH=. python 處理中研院標音/處理標音.py 
```

## 標漢字正確率
```
cd EDU/
python 4EDU做例句.py
python Cal_Similarity.py
```
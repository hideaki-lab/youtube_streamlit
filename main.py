import streamlit as st
import numpy as np
import pandas as pd
import warnings
import time

from PIL import Image

warnings.filterwarnings('ignore')

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

st.write('DataFrame')

df1 = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '２列目':[10, 20, 30, 40]
})

st.write(df1)
st.dataframe(df1.style.highlight_max(axis=0), width=200, height=175) # 動的なテーブル
st.table(df1.style.highlight_max(axis=0)) # 静的なテーブル

# マジックコマンド
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
    )

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

# lat:緯度  lon:経度
# 新宿付近の経度・緯度情報を生成
df3 = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
    )

st.map(df3)

st.write('Display Image')

img = Image.open('5.jpg')

if st.checkbox('Show Image'):
    st.image(img, caption='86後期', use_column_width=True)
    st.write('インタラクティブなウィジェット')


st.sidebar.write('Interactive Widgets')

option = st.sidebar.selectbox(
        'あなたが好きな数字を教えてください。',
        list(range(0, 9))
    )
text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

st.write(f'あなたの好きな数字は、{option}です。')
st.write(f'あなたの趣味:{text}')
st.write(f'コンディション:{condition}')

left_column, right_column = st.beta_columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容3')
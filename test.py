# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.1'
#       jupytext_version: 0.8.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
#   toc:
#     colors:
#       hover_highlight: '#DAA520'
#       navigate_num: '#000000'
#       navigate_text: '#333333'
#       running_highlight: '#FF0000'
#       selected_highlight: '#FFD700'
#       sidebar_border: '#EEEEEE'
#       wrapper_background: '#FFFFFF'
#     moveMenuLeft: true
#     nav_menu:
#       height: 4px
#       width: 254px
#     navigate_menu: true
#     number_sections: true
#     sideBar: true
#     threshold: 4
#     toc_cell: false
#     toc_section_display: block
#     toc_window_display: false
#     widenNotebook: false
# ---

# %% {"ExecuteTime": {"end_time": "2018-10-18T15:56:12.310348Z", "start_time": "2018-10-18T15:56:12.304148Z"}}
import numpy as np

# %% {"ExecuteTime": {"end_time": "2018-10-18T16:02:16.528092Z", "start_time": "2018-10-18T16:02:16.525560Z"}}
import matplotlib
import matplotlib.pyplot as plt

# %% {"ExecuteTime": {"end_time": "2018-10-18T16:02:35.853144Z", "start_time": "2018-10-18T16:02:35.850494Z"}}
font = {'family': 'normal', 'weight': 'bold', 'size': 8}
matplotlib.rc('font', **font)

# %% {"ExecuteTime": {"end_time": "2018-10-18T16:04:26.360698Z", "start_time": "2018-10-18T16:04:25.891589Z"}}
fig = plt.figure(figsize=(4, 2))
ax = fig.add_subplot(111)
fig.suptitle(
    'This figure suptitle is long but it is manually positioned', y=.5, x=0.5)
ax.set_title('This axis title should be on the left', loc='left')
fig.savefig('manual_pos.png')

# %%
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
S = pd.Series([1,2,np.nan])

#Sn=S.fillna(np.array([1,1,1]))
print(Sn)
df = pd.DataFrame(S)
print(df)
print(df.fillna(-1))
print(assert df1._is_view)


# %%
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, 5],
                    [np.nan, 3, np.nan, 4]],
                    columns=list('ABCD'))
print(df)
df.fillna(value={'A':-1,'D':0,'E':0})
print(df)
print(df.mode().iloc[0])

# %%
from pandas.api.extensions import ExtensionArray
df=ExtensionArray()
# print(df)
# print(dir(df))
# df=pd.Series([1,2,np.nan])
# print(df)
expected = pd.Series(np.array([1, -1, 0], dtype=np.int64))
#print(expected)
from pandas import Categorical
df = pd.DataFrame({"A":[0, 'A']})
#result = df.count(axis='columns')
#print(result)
print(df)
#print(df.fillna('0'))
df1=df.fillna(0, axis='columns')
print(df1)
print(df1._is_view)
assert df1._is_view
assert df1.equals(df)

# %%
def shellsort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            curr = i
            while curr >= gap and arr[curr-gap]> temp:
                # if value from lower index is greater than
                # temp: move to that loc ( ascending)
                arr[curr] = arr[curr-gap]
                curr = curr - gap

            # put the temp value at right location
            arr[curr] = temp
        gap = gap//2

    return arr
shellsort([3,5,1,10,8])

# %%
# Quicksort
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]


        mergesort(lefthalf)
        mergesort(righthalf)
        l = 0
        r = 0
        curr = 0

        while l < len(lefthalf) and r < len(righthalf):
            if lefthalf[l] < righthalf[r]:
                arr[curr] = lefthalf[l]
                l = l + 1
            else:
                arr[curr] = righthalf[r]
                r = r + 1
            curr = curr + 1

        while l < len(lefthalf):
            arr[curr] = lefthalf[l]
            l += 1
            curr += 1

        while r < len(righthalf):
            arr[curr] = righthalf[r]
            curr += 1
            r += 1

        return arr
mergesort([3,5,1,10,-8])

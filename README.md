# toilet-and-poo

1. **參考資料**:
    1. Pygame homepage: http://pygame.org 
    2. documentation:http://pygame.org/docs/ref
    3. 改編自大福媽pygame課程作品:feed the bird
 ------
2. **關於本遊戲**
    1. 以課程範例遊戲為基礎進行改編
    2. 將大部分圖案、字幕以及音效替換，符合個人風格
    3. 練習pygame匯入檔案的操作
**_3.如何改編_**
| 改編內容 | 改編方式 |
|:-----:|:----------:|
| _1.字幕_ | 定義新的顏色並套用至字幕上|
| _2.音效_ | 下載新的音檔，替換舊的音效|
| _3.圖像_ | 下載新的圖像，替換舊的音效 
| name | description |

**_4.Code snippet_**
```python
#原本的coin.png改為poo.png
coin_image=pygame.image.load("poo.png")
coin_rect=player_image.get_rect()
coin_rect.x=window_width+buffer_distance
coin_rect.y=random.randint(64,window_height-32)
```
**_5.Game assets_**<br>
[icon archive:](https://iconarchive.com/)網站提供遊戲圖像下載<br>

<img src="" width="400" height="300" alt="2.py程式截圖"><br>

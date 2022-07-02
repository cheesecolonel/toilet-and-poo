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


**_3.how to adapt_**
| name | description |
|:-----:|:----------:|
| _1.py_ | Create game surface , game loop and drawing|
| _2.py_ | Blit text, font, sound and image objects.|
| _3.py_ | Getting keyboard and collection dection

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

<img src="https://github.com/cheesecolonel/toilet-and-poo/blob/main/tandp.png" width="950" height="400" alt="2.py程式截圖"><br>

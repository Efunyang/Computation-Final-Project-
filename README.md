# 魔髮奇緣


### LineBot內容
大多數女生對於髮型有選擇障礙，此LineChatBot可以提供用戶一些建議，例如髮廊跟長短髮各自的優點跟範例。

### 環境
* Python 3.6
* Pipenv
* ubuntu 20.04

### 使用說明
* 操作
  * 輸入start開始
  * 隨時輸入restart可以reset所有資訊
* 架構圖
  * 輸入"start"開始
  * 選擇想要的長度 -> "短髮"或"長髮"
  * 若選擇"短髮"
    * 有"短髮髮型"和"短髮介紹"和"短髮髮廊"
      * 短髮介紹
        * 會有文字介紹
      * 短髮髮廊
        * 會有文字推薦的髮廊
      * 短髮髮型
        * 有三種圖示讓你參考    
  * 若選擇"長髮"
    * 有"長髮髮型"和"長髮介紹"和"長髮髮廊"
      * 長髮介紹
        * 會有文字介紹
      * 長髮髮廊
        * 會有文字推薦的髮廊
      * 長髮髮型
        * 有三種圖示讓你參考  
### FSM
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/fsm.png)
 #### state說明
   * user: 輸入start開始
   * choose: 輸入短髮或長髮
   * girlshorthair: 選擇介紹或髮型或髮廊
   * girllonghair: 選擇介紹或髮型或髮廊
   * girlshortshow: 選擇短髮髮型各種圖示
   * girlshortimg1: 選擇顯示短髮圖1
   * girlshortimg2: 選擇顯示短髮圖2
   * girlshortimg3: 選擇顯示短髮圖3
   * girllongshow: 選擇長髮髮型各種圖示
   * girllonfimg1: 選擇顯示長髮圖1
   * girllongimg2: 選擇顯示長髮圖2
   * girllongimg3: 選擇顯示長髮圖3
### Demo
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805535.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805537.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805538.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805539.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805540.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805541.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805542.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805543.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805544.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805545.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805546.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805548.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805549.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805550.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805551.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805552.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805553.jpg)
![image](https://github.com/Efunyang/Computation-Final-Project-/blob/master/img/readmepic/S__39805554.jpg)

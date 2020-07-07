
import statistics
#引進 statistics 函數，供後續標準差與中位數的計算

scoredata = list()

num = 1

quit = "n"

#宣告 data 陣列與資料數目

sum = 0
#宣告分數總和

while quit == "n" or quit == "N":
#主程式迴圈
    
    num = 1
    #重新執行時，將資料數重新計算為 1

    import time
    #導入 time 函數，做重複迴圈

    while True:

        try:
            
            score = float(input("請輸入第 " + str(num) +" 筆成績（輸入 -1 結束）："))

            if score <=100 and score >=0:
            #確認分數數據是否介於 0 與  100 之間

                scoredata.append(score)

                break

            elif score == -1:
                #當輸入值為 -1 時，跳出迴圈
                break

            else:
                print("檢查是否為 0 - 100 的分數")

                del scoredata[-1]
                #利用 del 來移去非 0 - 100 的數據

                score = float(input("請輸入第 " + str(num) + " 筆成績（輸入 -1 結束）："))


        except:
            print("＜ 錯誤：輸入值非數字，檢查輸入的是否為數字 ＞")
            num = 1
            time.sleep(0)
            #倒數 0 秒重新執行


    while score != -1:

        try:
            
            scoredata.append(score)

            if score >= 0 and score <= 100:

                num = num + 1   
                #資料數增加一項

                score = float(input("請輸入第 " + str(num) + " 筆成績（輸入 -1 結束）："))
                #當輸入值不等於 -1 時，將輸入值加入 data 陣列最後一項，並繼續輸入成績值

            elif score == -1:
                break
            #當輸入值為 -1 時，跳出迴圈

            else:
                print('check')

                del scoredata[-1]
                #利用 del 來移去非 0 - 100 的數據

                score = float(input("請輸入第 " + str(num) + " 筆成績（輸入 -1 結束）："))


            
        
        except:

            print("＜ 錯誤：輸入值非數字，檢查輸入的是否為數字 ＞\n")

            num = num - 1
            #不算入錯誤數據的項目數

            del scoredata[-1]
            #在遇到錯誤數據時，code 會自動將上一筆正常數字加入陣列，造成重複計算
            #利用 del 來移除重複增加的數據


    if score == -1:

        num = num -1
        #避免將結束程式的 -1 加入數據數量影響成績


    print("所有輸入的成績：\n", scoredata)

    print("共有 {} 筆資料".format(num))
    #輸出所有陣列中的數據，並確認資料數
    
    print("")
    #換行


    for score in scoredata:
        sum += score
     # sum+= score == sum = sum + score


    if num == 2:

        ave = round(statistics.mean(scoredata),2)
        #定義算數平均，並四捨五入到小數點後二位

        sd = statistics.stdev(scoredata)
        #定義標準差

        info = ("標準差為:{} ".format(round(sd,3)))

        est = ("最高分為 {} 分，最低分為 {} 分 " .format(max(scoredata),min(scoredata)))
        #定義最高分與最低分


    elif num >= 3:

        ave = round(statistics.mean(scoredata),2)

        sd = statistics.pstdev(scoredata)
        #定義標準差

        med = statistics.median(scoredata)
        #定義中位數

        mode = statistics.mode(scoredata)
        #定義眾數

        info = ("標準差為:{}\n中位數為:{}\n眾數為:{}.\n".format(round(sd,2),med,mode))

        est = ("最高分為 {} 分，最低分為 {} 分 ".format(max(scoredata),min(scoredata)))


    elif num == 0:

        ave = ("0")

        info = ("")

        est = ("0")

        #當數據為零時將發生 Statistics 錯誤
        #特別制定數據為零的相關資訊，避免中斷程式

    else:

        ave = (" *無平均* ")

        info = ("只有一筆數據，無標準差或中位數等數據")


    print("總分：{} 分，平均：{} 分.\n".format(sum,ave))
    #輸出總分和平均分
    
    print(est)
    #輸出最高與最低值，當數據為零時則跳過

    print(info)
    #輸出標準差、中位數和眾數，當數據為零時則跳過

    quit = str(input("結束程式？ 要繼續計算輸入 n，要結束輸入任意字元即可"))
    #詢問用戶是否要繼續計算，輸入 n or N 將重新主程式迴圈

    print("")

else:

    print("thx! Power By Jun Shawn")
    #結束程式時輸出



# 馬公高中資訊科技課程學習檔案
# Power by 101-23 張君祥
# 目的: 製作成績計算程式，並加入高一下學期數學的標準差、眾數等數據觀念
# 目的2: 針對 Error Handling 做優化與補強，確保在任何錯誤下程式也能正常執行
# 日期: 109.7.1

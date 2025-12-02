# UAV Flight Log Generation and High-Level Mission Planning Using Vision-Language Models

[[English A1 Poster](https://github.com/bscny/undergraduate_project/blob/main/docs/posters/Undergraduate_Thesis_Poster.pdf)] [[Chinese A1 Poster](https://github.com/bscny/undergraduate_project/blob/main/docs/posters/Chinese_Undergraduate_thesis_poster.pdf)] [[English Final Report](https://github.com/bscny/undergraduate_project/blob/main/docs/reports/Final_Project_Report.pdf)] [[Chinese Final Report](https://github.com/bscny/undergraduate_project/blob/main/docs/reports/Chinese_Final_Project_Report.pdf)] [[supplementary slide](https://github.com/bscny/undergraduate_project/blob/main/docs/slides/Supplementary_slide.pdf)]

## Table of content

- [abstract](#abstract)
- [simple demo](#simple-demo-majority-in-english)

## Abstract

本研究希望透過建立階段式的 pipeline 以結合視覺語言模型 (VLM) 與無人機控制，使無人機在執行任務時能夠同步進行影像資料解析。具體而言，無人機將持續分析其攝影鏡頭捕捉到的現場影像，評估如何執行使用者下達的高階抽象指令 (如「找到一座古老的寺廟」)，並判斷是否成功達成。同時無人機系統將採用類似航海日誌之記錄方式詳細紀錄飛行參數、現場觀測到的關鍵事件以及重要地標，並將經整理後的資訊有結構化的回傳給操作者以提供全方位的回饋與決策支持。在實驗中將以 AirSim (Unreal Engine + ROS2) 作為無人機模擬環境以降低實驗成本與縮短研發週期，由於 AirSim 模擬系統與真實世界的無人機輸入訊號相同且 Unreal Engine 可模擬真實世界環境，若能解決如何使 VLM 的資料傳遞更加快速、降低延遲，該技術便具有直接應用於真實無人機控制之潛力，從而推進無人機自動化的與智慧應用的未來發展。

This study aims to establish a staged pipeline that integrates vision-language models (VLMs) with UAV control, allowing drones to simultaneously perform image interpretation while executing missions. Specifically, the drone continuously analyzes real-time images captured by its camera, evaluates how to execute high-level abstract commands issued by the user (e.g., “find an old temple”), and determines whether the objective is successfully achieved. At the same time, the UAV system records flight parameters, key onsite events, and important landmarks in a detailed log format similar to a nautical logbook, then returns structured information to the operator to provide comprehensive feedback and decision support.

In the experiments, AirSim (Unreal Engine + ROS2) is used as a UAV simulation environment to reduce experimental costs and shorten the development cycle. Because AirSim uses the same control signals as real-world drones and Unreal Engine can simulate realistic environments, if the latency of VLM data transmission can be reduced, this technology has direct potential for deployment on real drones, pushing forward the future of UAV automation and intelligent applications.


## Simple Demo (Majority in English)

1. case 1: Simulate Private recreational area (containing newest predefined abstract missions)
    - [demo video on YouTube](https://youtu.be/Sefa05ckpKo)
    - [actual drone footage](https://youtu.be/FY_GNWHaYxg)
    - [Flight Log report](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Private_Land/Flight_log.md)
2. case 2: Simulate City
    - [demo video on YouTube](https://youtu.be/Dh1qoBHkMp8)
    - [actual drone footage](https://youtu.be/RewiEn2s4N4)
    - [Flight Log report](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/SimCity2/Flight_log.md)
3. case 3: 張家界 (ZhangJiajie)
    - [demo video on YouTube](https://youtu.be/hiHjvGYlLNw)
    - [actual drone footage](https://youtu.be/7FV5pVGj-oc)
    - [Flight Log report](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/ZhangJiajie/Flight_log.md)
4. Flight Logs from real world drone footage:
    1. [嘉義(Jiayi City)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/City/Flight_log.md), [影片連結(video link)](https://youtu.be/UZp3Tht_wmE)
    2. [冰山(Ice mountain)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Ice_Mountains/Flight_log.md), [影片連結(video link)](https://www.pexels.com/video/aerial-footage-of-trees-on-mountains-8761176)
    3. [警車跟隨(Following a police car)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Police_Car_operation/Flight_log.md), [影片連結(video link)](https://www.pexels.com/video/drone-footage-of-a-police-car-driving-on-long-highway-5490959/)
    4. [工業區(Industrial zone)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Industrial_Zone/Flight_log.md), [影片連結(video link)](https://www.pexels.com/video/flight-over-industrial-zone-with-drone-19395434/)
    5. [示威街道(Protest street)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Protest/Flight_log.md), [影片連結(video link)](https://www.pexels.com/video/drone-footage-of-city-and-streets-in-daylight-6254278/)
# UAV Flight Log Generation and High-Level Mission Planning Using Vision-Language Models

## Table of content

- [abstract](#abstract)
- [simple demo](#simple-demo)
- [presentation](#presentation)
- [phases](#phases)

## Abstract

本研究希望結合視覺語言模型(Vision Language Model, VLM)與無人機控制，達成無人機在執行任務時能夠同步進行影像資料解析。具體而言無人機將持續分析其攝影鏡頭捕捉到的現場影像並依據分析結果評估是否達成使用者下達之操作命令。同時無人機系統將採用類似航海日誌之記錄方式詳細紀錄飛行軌跡、現場觀測到的關鍵事件以及重要地標並將經整理後的資訊有結構化的回傳給操作者以提供全方位的回饋與決策支持。

在實驗中將以 AirSim(Unreal Engine) 作為無人機模擬環境以降低實驗成本與縮短研發週期，由於 AirSim 模擬系統與真實世界的無人機輸入訊號相同 且 Unreal Engine 可模擬真實世界環境，倘能解決了如何使 VLM 的資料傳遞更加快速、降低延遲，該技術便具有直接應用於真實無人機控制之潛力，從而推進無人機自動化的與智慧應用的未來發展。

## Simple Demo

1. case 1: Simulate City
    - [demo video on YouTube](https://youtu.be/Dh1qoBHkMp8)
    - [actual drone footage](https://youtu.be/RewiEn2s4N4)
    - [Flight Log report](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/SimCity2/Flight_log.md)
2. case 2: 張家界
    - [demo video on YouTube](https://youtu.be/hiHjvGYlLNw)
    - [actual drone footage](https://youtu.be/7FV5pVGj-oc)
    - [Flight Log report](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/ZhangJiajie/Flight_log.md)
3. Flight Logs from real world drone footage:
    1. [嘉義](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/City/Flight_log.md), [影片連結](https://youtu.be/UZp3Tht_wmE)
    2. [冰山](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Ice_Mountains/Flight_log.md), [影片連結](https://www.pexels.com/video/aerial-footage-of-trees-on-mountains-8761176)
    3. [警車跟隨](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Police_Car_operation/Flight_log.md), [影片連結](https://www.pexels.com/video/drone-footage-of-a-police-car-driving-on-long-highway-5490959/)
    4. [工業區](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Industrial_Zone/Flight_log.md), [影片連結](https://www.pexels.com/video/flight-over-industrial-zone-with-drone-19395434/)
    5. [示威街道](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Protest/Flight_log.md), [影片連結](https://www.pexels.com/video/drone-footage-of-city-and-streets-in-daylight-6254278/)

## Presentation

Project is still in progress... the newest slide is [here](https://www.canva.com/design/DAGztpVkxZI/gzrc3zIlRoArxwzMpO0iCw/edit)

## Phases

1. First Phase: 無人機回傳航行日誌
2. Second Phase: 無人機動主航行
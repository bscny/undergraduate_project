# UAV Flight Log Generation and High-Level Mission Planning Using Vision-Language Models

## Table of content

- [abstract](#abstract)
- [simple demo](#simple-demo)
- [presentation](#presentation)
- [phases](#phases)

## Abstract

本研究希望結合視覺語言模型(Vision Language Model, VLM)與無人機控制，達成無人機在執行任務時能夠同步進行影像資料解析。具體而言無人機將持續分析其攝影鏡頭捕捉到的現場影像並依據分析結果評估是否達成使用者下達之操作命令。同時無人機系統將採用類似航海日誌之記錄方式詳細紀錄飛行軌跡、現場觀測到的關鍵事件以及重要地標並將經整理後的資訊有結構化的回傳給操作者以提供全方位的回饋與決策支持。

在實驗中將以 AirSim(Unreal Engine) 作為無人機模擬環境以降低實驗成本與縮短研發週期，由於 AirSim 模擬系統與真實世界的無人機輸入訊號相同 且 Unreal Engine 可模擬真實世界環境，倘能解決了如何使 VLM 的資料傳遞更加快速、降低延遲，該技術便具有直接應用於真實無人機控制之潛力，從而推進無人機自動化的與智慧應用的未來發展。

This study aims to integrate Vision-Language Models (VLMs) with drone control to enable drones to perform real-time image data analysis during mission execution. Specifically, the drone will continuously analyze the live video captured by its onboard camera and, based on the analysis results, evaluate whether the user’s operational commands have been fulfilled.

At the same time, the drone system will adopt a “logbook-like” recording approach to meticulously document its flight trajectory, key on-site events, and important landmarks. The collected data will then be organized and structured before being transmitted back to the operator, providing comprehensive feedback and decision support.

In the experiment, AirSim (Unreal Engine) will be used as the drone simulation environment to reduce experimental costs and shorten the development cycle. Since AirSim’s simulated control inputs are identical to those of real-world drones and Unreal Engine can realistically replicate real-world environments, overcoming the challenge of improving VLM data transmission speed and reducing latency would make this technology directly applicable to real-world drone control—thus advancing the automation and intelligent applications of drones in the future.

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
    1. [嘉義(Jiayi City)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/City/Flight_log.md), [影片連結](https://youtu.be/UZp3Tht_wmE)
    2. [冰山(Ice mountain)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Ice_Mountains/Flight_log.md), [影片連結](https://www.pexels.com/video/aerial-footage-of-trees-on-mountains-8761176)
    3. [警車跟隨(Following a police car)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Police_Car_operation/Flight_log.md), [影片連結](https://www.pexels.com/video/drone-footage-of-a-police-car-driving-on-long-highway-5490959/)
    4. [工業區(Industrial zone)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Industrial_Zone/Flight_log.md), [影片連結](https://www.pexels.com/video/flight-over-industrial-zone-with-drone-19395434/)
    5. [示威街道(Protest street)](https://github.com/bscny/undergraduate_project/blob/main/assets/flight_logs/Protest/Flight_log.md), [影片連結](https://www.pexels.com/video/drone-footage-of-city-and-streets-in-daylight-6254278/)

## Presentation

Project is still in progress... the newest reported slide is [here](https://www.canva.com/design/DAGztpVkxZI/gzrc3zIlRoArxwzMpO0iCw/edit). The newest unreported one is [here](https://www.canva.com/design/DAG1INEF2rw/is1T_kj2NwZLC1EUYIRpKA/edit)

## Phases

1. First Phase: 無人機回傳航行日誌(Flight Log generation)
2. Second Phase: 無人機動主航行(Autonomous Flight)
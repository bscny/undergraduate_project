# UAV Flight Log Generation and High-Level Mission Planning Using Vision-Language Models

## Table of content

- [summary](#summary)
- [phases](#phases)

## Summary

本研究希望結合視覺語言模型(Vision Language Model, VLM)與無人機控制，達成無人機在執行任務時能夠同步進行影像資料解析。具體而言無人機將持續分析其攝影鏡頭捕捉到的現場影像並依據分析結果評估是否達成使用者下達之操作命令。同時無人機系統將採用類似航海日誌之記錄方式詳細紀錄飛行軌跡、現場觀測到的關鍵事件以及重要地標並將經整理後的資訊回傳給操作者以提供全方位的操作回饋與決策支持。在實驗中將以 Gazebo-ROS2 作為無人機模擬環境以降低實驗成本與縮短研發週期，能能成模模擬自動化的的無人機由於 ROS2 系統與真實世界的無人機輸入訊號相同 且 Gazebo 可模擬真實世界的嚴苛環境 倘能解決了如何使 VLM 的資料傳遞更加快速降低延遲該技術便具有直接應用於真實無人機控制之潛力從而推化無人機動化的與智慧的應用的未來發展。

## Phases

1. First Phase: 無人機回傳航行日誌
2. Second Phase: 無人機動主航行
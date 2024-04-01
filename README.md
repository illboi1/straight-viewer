# Straight Viewer
Perform camera calibration and produce images whose distortions are corrected.

## Camera Calibration 파트 [main.py / camera_calibration.py]
동영상으로부터 입력 이미지 선택 (약 10~20개)
(동영상 촬영본 필요, 체스판 코너가 보이도록 촬영)
![img_select](https://github.com/illboi1/straight-viewer/assets/88954347/3dada07d-edca-49ab-82b1-628ea999443e)
* [SPACE 키]: 정지/재개
* [ENTER 키]: 정지된 상태에서 현재 이미지를 선택에 추가
* [ESC 키]: 프로그램 종료

### Results of Camera Calibration
* The number of selected images = 15
* RMS error = 1.3133058404322477
* Camera matrix (K) = 
[[1.50442370e+03 0.00000000e+00 9.65939753e+02]
 [0.00000000e+00 1.51417734e+03 5.66894338e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
* Distortion coefficient (k1, k2, p1, p2, k3, ...) = [0.10460431 -0.05506334  0.00271136 -0.00119125 -0.62262696]

## Distortion Correction 파트 [distortion_correction.py]
원본 이미지 / 왜곡을 보정한 이미지 제공
![corrected](https://github.com/illboi1/straight-viewer/assets/88954347/153084af-a370-4651-84e4-7c8637aede3d)

* [TAB 키]: 이미지 전환
* [ESC 키]: 프로그램 종료
* [스페이스 키]: 정지/재개

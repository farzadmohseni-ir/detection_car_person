# detection_car_person

This project is about machine and human diagnostics . *( Due to the large size of the modules, it is stored in Google Drive , [Download](https://drive.google.com/drive/folders/1nmznxyKXHwlwXKKUMhAgqStWWi5UjuCk?usp=sharing) )*

Modules and data are taken from the following websites :

- [Kaggle](https://www.kaggle.com/)
- [Paperswithcode](https://paperswithcode.com/)
- [GitHub](https://github.com/)

The videos used in the project have been picked up from YouTube and I have no responsibility for the images of people and objects .

- [Video link (detection_car)](https://www.youtube.com/watch?v=kh57ERFMk0k)
- [Video link (detection_person)](https://www.youtube.com/watch?v=XfIpSMhd-CA)


.



## Installation

Install the libraries needed to run the project :

```python
pip install -r requirements.txt
```

.



## Demo & How To Run


**Notice :** The appearance of the project thigh will be as follows :

| *Put your file in the relevant directory to get the output from it* | *Creating the final file "` the_output.avi `" may take time, so be patient. (It depends more on the power of your GPU)* |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![Input](https://user-images.githubusercontent.com/57835828/120105636-09825880-c16f-11eb-968f-a35cf84838c0.jpg) | ![How_To_Run](https://user-images.githubusercontent.com/57835828/120105646-1737de00-c16f-11eb-907a-8f207cd9402e.jpg) |

.


**The project consists of three parts :**

1. The first part is about recognizing the vehicles from the video file . 

   ```python
   python3 detection_car.py
   ```
   
   https://user-images.githubusercontent.com/57835828/120105103-c1623680-c16c-11eb-85a9-4801bd967ecd.mp4
   
2. The second part is about recognizing humans from a video file . 

   ```python
   python3 detection_person.py
   ```
   
   https://user-images.githubusercontent.com/57835828/120105972-6d595100-c170-11eb-9579-302477d86b5d.mp4
   
3. The third part is about recognizing human from webcam . 

   ```python
   python3 webcam_person.py
   ```
   
   ![webcam_person](https://user-images.githubusercontent.com/57835828/120105606-e0fa5e80-c16e-11eb-80aa-7097639b624f.jpg)




# Capstone
![home](https://github.com/JaeHyun154/Cabstone/assets/129927776/bf6c5222-b1f6-4f95-95ce-2df2c28520ee)

## Project Introduction
<p align="justify">
최근 고령화 사회로 인하여 1인 가구의 증가에 따른 반려동물 시장이 빠르게 성장하고 있습니다. 그러나 집안에서 반려동물을 키우기 시작하면서 반려동물이 집에 혼자 있을 경우 사료를 주지 못하는 문제, 반려동물이 혼자 집에 있음으로 받는 스트레스, 좁은 혼자 있음으로 받는 스트레스, 비만 반려견의 증가 등등 반려견의 건강 문제가 높아지면서
저희는 이를 개선하기 위해 자동사료급식기능과 반려동물행동분석기능을 통합한 <strong>스마트 자동 사료 급식 시스템</strong>을 개발하고자 하였습니다.

<p align="justify">
<strong>스마트 자동 사료 급식 시스템</strong>란, 사람이 배고플 때 밥을 많이 먹고, 안 고플 땐 조금 먹는 것 처럼 동물도 마찬가지 아닐까? 라는 아이디어에 착안하여,
사람도 많이 활동할 때 밥을 많이 먹으니, 반려견도 활동이 많으면 많은 밥을 먹도록 도와주도록 하는 서비스입니다. 활동량에 따른 스마트 식사를 하게 되면 반려견의 건강 문제나
비만율도 함께 감소할 것이라고 생각하였습니다. 
<p align="center">


<p align="justify">
Recently, due to the aging society, the pet market is growing rapidly due to the increase in single-person households. However, as people start raising pets at home, they face health problems such as not being able to feed their pets when they are home alone, stress from being alone at home, stress from being alone in a small space, increase in the number of obese dogs, etc. As it rises
To improve this, we want to develop a smart automatic feeding system that integrates the automatic feeding function and pet behavior analysis function.

<p align="justify">
A smart feeder that uses your dog's activity level and behavior patterns is like humans eating a lot when they're hungry and eating a little when they're not hungry, isn't this the same for animals? Based on the idea,
People eat a lot when they are active, so this service helps dogs eat a lot when they are active too. If you eat smart meals according to the amount of activity, your dog's health problems or
We thought the obesity rate would also decrease.
<p align="center">

<br><br>

## Process
- 사용자는 wifi모듈이 내장된 아두이노 센서를 반려견의 의류에 설치합니다.
- 반려견으로부터 수집된 데이터를 받고 분석하기 위해 서버를 열고 스마트 급식기를 설치합니다.
- 준비가 다 된 뒤, 코드를 업로드 하게 되면 이후부터 반려견의 상태에 따라 알맞은 행동데이터가 수집됩니다.
- 수집된 데이터에 따라 분류가 되고 만약 서버에서 받은 활동량 데이터가 활동량 데이터가 분류구간(1~5) 안에 존재할경우 해당 구간에 맞는 사료를 배출하도록 합니다.
- 만약 최초 분류구간인 1에 해당하는 활동량이 아니라면 스마트 급식기는 애완동물이 감지되어도 사료를 분출하지 않습니다.
- 스마트 의류로부터 실시간으로 발생하는 센서 데이터를 바탕으로 행동패턴과, 패턴별 행동량을 분석하고, 식사량과 통합하여 자동배식을 진행할 수 있습니다.

-  Users install an Arduino sensor with a built-in WiFi module on their dog's clothing.
-  Open a server and install a smart feeder to receive and analyze data collected from dogs.
-  After preparation is complete, upload the code and appropriate behavioral data will be collected depending on the dog's condition.
-  It is classified according to the collected data, and if the activity data received from the server is within the classification range (1 to 5), feed appropriate for that range is discharged.
-  If the activity level does not correspond to the first classification range of 1, the smart feeder will not dispense food even when the pet is detected.
-  Based on sensor data generated in real time from smart clothing, behavioral patterns and the amount of behavior for each pattern can be analyzed and integrated with the meal amount to automatically provide food.
<p align="center">

</p>

<br>

## Tech Stack

| mysql | django | Arduino  | react | scikit-learn |
| :---: | :----: | :-------:| :---: | :----------: |

![tech](https://github.com/JaeHyun154/Cabstone/assets/129927776/37160e8a-b0c1-486d-b332-8fd3977193eb)

<br><br>

## Features

### Smart service
- 만약 주인이 없어도 반려견에게 센서만 부착되어 있다면, 스마트 급식기에 부착된 초음파 센서가 반려견을 감지하여 활동량 data를 기반으로 자동 급식

- Even if the owner is not present, if a sensor is attached to the dog, the ultrasonic sensor attached to the smart feeder detects the dog and automatically feeds the dog based on activity data.

### health care services
- 주어진 활동량을 채우지 못한다면 사료가 나오지 않아 무분별한 급식으로 인한 비만, 스트레스 문제 해결

- If you do not meet the given amount of activity, no feed will be provided, solving obesity and stress problems caused by indiscriminate feeding.

### Responsive web service
- 사용자들이 어떠한 정보를 모니터링 할 수 	있고 어떤 서비스를 이용할 수 있는지 표기하기 위해 간단한 UI
- 반려견의 활동량과 그에 따른 식사량을 확인할 수 있습니다.

- Simple UI to indicate what information users can monitor and what services they can use.
- You can check your dog's activity level and corresponding meal amount.


### Hardware
- 급식기<br>
![image](https://github.com/JaeHyun154/Cabstone/assets/129927776/e2acf249-21b5-4a2f-b124-180d77d0bdbe)
![image](https://github.com/JaeHyun154/Cabstone/assets/129927776/54a49f62-02df-4cc1-8f1e-b337b19f4468)
![image](https://github.com/JaeHyun154/Cabstone/assets/129927776/74be7dba-b606-47f7-ba65-29986b70f469)

![KakaoTalk_20231222_152539083](https://github.com/JaeHyun154/Cabstone/assets/129927776/3d1e8cbf-3015-467f-bb98-6d51a44117f5)

- Clothes sensor<br>
![image](https://github.com/JaeHyun154/Cabstone/assets/129927776/368acc4a-df20-46b7-b713-2290c0645528)
![image](https://github.com/JaeHyun154/Cabstone/assets/129927776/b0cfd5d5-2905-4d0c-b351-bd6a01809f3e)






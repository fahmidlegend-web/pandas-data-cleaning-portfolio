### 🧹 Data Cleaning Portfolio

### Filled Missing Values with Randomly Generated Values

Before::
![image](Before_Missing_Datas.jpg)

Source Code ::

numbers = random.choices(string.digits,k=4)
phoneNum = "+89" + "".join(numbers)

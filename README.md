THIS IS A PANDEMIC SIMULATION IN PYGAME LIBRARY OF PYTHON <br />
Prereq:<br />
1)Python 3.12 <br />
2)pip install Pygame <br />
3)pip install matplotlib <br />
4)pip install numpy <br />
 PARAMETERS: these are all the parameters that you can change from code. Each change in any parameter can lead to drastic change in pandemic.<br />
 o)number of people as *n_people* <br />
 
 o)size of one person as *size* <br />
 
 o)speed of one person as *speed* <br />

 o)infection radius as *infect_dis* <br />
 
 o)recovery time as *recover_time* <br />
 
 o)immune time as *immune_time* <br />
 (which is set to a very very large value as default because I am following SIR model i.e. person can't lose immunity after some time) <br />
 
 o)probability of catching infection as *prob_catch* <br />
 
 o)probability of dying as *prob_death* <br />
 (Actually people who die aren't removed but their color is changed to the color of the screen and they can't interact with other people, they just become invisible) <br />

 FRAME RATE(fps) is specified on the top left side of the screen after the code is set to run(If n_people is very large then frame rate is decreased due to this the simulation will become more laggy )<br />

 If n_people is set to a very large number like 10,000 and immune_time is set to a comparable value to recover_time then we will get this result:- <br />
  def__init__(self,n_people=10000,size=4,speed=0.04,infect_dist=10,recover_time=75,immune_time=65,
                 prob_catch=0.2,prob_death=0.00095): <br />
                
                   
                   
                   
                   
                   
                   
                   
                  
 ![Figure_1](https://github.com/Ray69Zard/Cordyceps_spreadsim/assets/164711749/88cb1a5c-00f3-4afd-921a-a1aafbe6b623)






So, this looks like a pandemic with many consecutive waves one by one with decreasing peaks i.e a damped pandemic!! as people are dying that's why infected people are decresing with time <br />

Although, with default settings we will get a traditional pandemic with one peak:-<br />
def__init__(self,n_people=2000,size=4,speed=0.04,infect_dist=5,recover_time=400,immune_time=1500000000000000000000000000000000000000000000000000000000000000000000000000000000000000,prob_catch=0.1,prob_death=0.00095):








![Figure_2](https://github.com/Ray69Zard/Cordyceps_spreadsim/assets/164711749/04432e5c-05c3-46c7-a58c-f19dc41cdf7a)





So,this just looks like any natural pandemic, <br />
The number of healthy people and total deaths are sigmoid and infection curve has one peak.<br />

We can just play with it everyday by changing as many parameters as we can lol.<br />
I will update this readme and will explain the code in detail but I am submitting this die to lack of time as last date of submission is already gone. :(<br />
I've coded this in Idle Python 3.12(64 bit)

![Sim py - C__Users_hp_AppData_Local_Programs_Python_Python312_Sim py (3 12 1) 11-04-2024 14_28_43](https://github.com/Ray69Zard/Cordyceps_spreadsim/assets/164711749/f36feff7-d78d-4ec9-98dc-ebbac22a15bc)





![pygame window 11-04-2024 14_28_09](https://github.com/Ray69Zard/Cordyceps_spreadsim/assets/164711749/18883dfc-93ec-4287-9ae3-7a6390aaafa9)



Thank You! <br />













 

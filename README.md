THIS IS A PANDEMIC SIMULATION IN PYGAME LIBRARY OF PYTHON <br />
Prereq:<br />
1)Python 3.12 <br />
2)pip install Pygame <br />
3)pip install matplotlib <br />
4)pip install numpy <br />
 PARAMETERS: these are all the parameters that you can change from code. Each change in any parameter can lead to drastic change in pandemic.
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
  def __init__(self,n_people=10000,size=4,speed=0.04,infect_dist=10,recover_time=75,immune_time=65,
                 prob_catch=0.2,prob_death=0.00095): <br />
                
                   
                   
                   
                   
                   
                   
                   
                  
 ![Figure_1](https://github.com/Ray69Zard/Cordyceps_spreadsim/assets/164711749/88cb1a5c-00f3-4afd-921a-a1aafbe6b623)






So, this looks like a pandemic with many consecutive waves one by one with decreasing peaks i.e a damped pandemic!! as people are dying that's why infected people are decresing with time 

Although, with default settings we will get a traditional pandemic with one peak-





















 

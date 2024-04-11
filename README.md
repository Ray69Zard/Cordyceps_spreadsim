THIS IS A PANDEMIC SIMULATION IN PYGAME LIBRARY OF PYTHON
Prereq:
1)Python 3.12
2)pip install Pygame
3)pip install matplotlib
4)pip install numpy
 PARAMETERS: these are all the parameters that you can change from code. Each change in any parameter can lead to drastic change in pandemic.
 o)number of people as *n_people* 
 o)size of one person as *size*
 o)speed of one person as *speed*
 o)infection radius as *infect_dis*
 o)recovery time as *recover_time*
 o)immune time as *immune_time*
 (which is set to a very very large value as default because I am following SIR model i.e. person can't lose immunity after some time)
 o)probability of catching infection as *prob_catch*
 o)probability of dying as *prob_death*
 (Actually people who die aren't removed but their color is changed to the color of the screen and they can't interact with other people, they just become invisible)

 FRAME RATE(fps) is specified on the top left side of the screen after the code is set to run(If n_people is very large then frame rate is decreased due to this the simulation will become more laggy )

 If n_people is set to a very large number like 10,000 and immune_time is set to a comparable value to recover_time then we will get this result:- 
 

























 

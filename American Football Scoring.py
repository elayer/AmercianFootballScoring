#!/usr/bin/env python
# coding: utf-8

# American Football Scoring Function
# 
# Created by: Eric Layer
# 
# Date: 12/27/2021
# 
# Description: This is a program with which simply outputs all combinations of possible point accumulations for a given score in American Football. After running the scoring functions below, you can run the below code block to enter a number. The program will then return a list of dictionaries denoting all the possible point totals among all the possible ways to score in the sport. 
# 
# Since we are not concerned with the order in which a score is achieved and simply searching for different ways to achieve a point total, I do not use generators in this program. In future I could try to update this program to work using generators if necessary.
# 
# 

# In[ ]:


ScoresList = []
RecordList = []

choice = int(input("Enter a score you wish to see all possible football scores for: "))
print('\n')
driverScore8(choice)
driverScore7(choice)
driverScore6(choice)
driverScore3(choice)
driverScore2(choice)

print("Final Scores List: \n")
ScoresList


# In[ ]:


def driverScore8(points):
    """
    This function calculates all possible scores with all possible values of 8 points (a touchdown with a 2PT conversion)
    
    Args:
        points: An integer value containing denoting the score to break down all possible score values starting from
                a touchdown and a 2PT conversion.
    
    
    """
    print('RUNNING SCORES STARTING WITH 8\n')

    score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
    temp = points 
    
    if points < 8:
        print('Cant do this, below 8\n')
    
    else:
        
        for i in range(points//8, 0, -1):
            
            points = temp
            score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
            
            if (points-i*8) == 1:
                
                points = temp
                continue
            
            score_string['TD2PT'] += i*8
            points -= i*8           
            
            temp7 = points
            temp7_string = score_string.copy()
            
            temp6 = points
            temp6_string = score_string.copy()
            
            temp3 = points
            temp3_string = score_string.copy()
            
            temp2 = points
            temp2_string = score_string.copy()
            
            
            if ((points//7) >= 1):
                
                c = points//7
                residual = 0
                
                while c >= 0:
                
                    if (points - c*7) == 1:
                        
                        c-=1
                        residual += 7
                    elif c == 0:
                        
                        break
                        
                    else:    

                        temp7_string['TDPAT'] += ((temp7//7)*7)
                        temp7_string['TDPAT'] -= residual
                        temp7 -= ((temp7//7)*7)
                        temp7 += residual
                                           
                        if temp7==0:
                            record = str(temp7_string['TD2PT'])+str(temp7_string['TDPAT'])+str(temp7_string['TD'])+str(temp7_string['FG'])+str(temp7_string['S'])
                            
                            if record not in RecordList:
                                print('Final score string is: ', temp7_string)
                                RecordList.append(record)
                                ScoresList.append(temp7_string)
                                
                            break
                        elif temp7==2:
                            #print('One S:')
                            temp7_string['S'] += 2
                            temp7 -= 2
                        elif temp7==3:
                            #print('One FG:')
                            temp7_string['FG'] += 3
                            temp7 -= 3
                        elif temp7==4:
                            #print('Two FG:')
                            temp7_string['S'] += 4
                            temp7 -= 4
                        elif temp7==5:
                            #print('One FG and One S:')
                            temp7_string['FG'] += 3
                            temp7_string['S'] += 2
                            temp7 -= 5
                            
                        
                        
                                              
                        record = str(temp7_string['TD2PT'])+str(temp7_string['TDPAT'])+str(temp7_string['TD'])+str(temp7_string['FG'])+str(temp7_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp7_string)
                        
                        break
            

            if ((points//6) >= 1):
                
                c = points//6
                residual = 0
                
                while c >= 0:
                
                    if (points - c*6) == 1:
                       
                        c-=1
                        residual += 6
                    elif c == 0:
                        
                        break
                        
                    else:           
                      
                    
                        temp6_string['TD'] += ((temp6//6)*6)
                        temp6_string['TD'] -= residual
                        temp6 -= ((temp6//6)*6)
                        temp6 += residual
                        
                        
                        
                        if temp6==0:
                            record = str(temp6_string['TD2PT'])+str(temp6_string['TDPAT'])+str(temp6_string['TD'])+str(temp6_string['FG'])+str(temp6_string['S'])
                            
                            if record not in RecordList:
                                #print('Final score string is: ', temp6_string)
                                RecordList.append(record)
                                ScoresList.append(temp6_string)
                            break
                        elif temp6==2:
                            #print('One S:')
                            temp6_string['S'] += 2
                            temp6 -= 2
                        elif temp6==3:
                            #print('One FG:')
                            temp6_string['FG'] += 3
                            temp6 -= 3
                        elif temp6==4:
                            #print('Two S:')
                            temp6_string['S'] += 4
                            temp6 -= 4
                        elif temp6==5:
                            #print('One FG and One S:')
                            temp6_string['FG'] += 3
                            temp6_string['S'] += 2
                            temp6 -= 5
                            
                                              
                        record = str(temp6_string['TD2PT'])+str(temp6_string['TDPAT'])+str(temp6_string['TD'])+str(temp6_string['FG'])+str(temp6_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp6_string)
                        
                        break
                
            
            
            if ((points//3) >= 1):
     
                c = points//3
                residual = 0
                
                while c >= 0:
                
                    if (points - c*3) == 1:
                     
                        c-=1
                        residual += 3
                    elif c == 0:
                       
                        break
                        
                    else:           
                    
                        temp3_string['FG'] += ((temp3//3)*3)
                        temp3_string['FG'] -= residual
                        temp3 -= ((temp3//3)*3)
                        temp3 += residual
                        
                        if temp3==0:
                            record = str(temp3_string['TD2PT'])+str(temp3_string['TDPAT'])+str(temp3_string['TD'])+str(temp3_string['FG'])+str(temp3_string['S'])
                            
                            if record not in RecordList:
                                #print('Final score string is: ', temp3_string)
                                RecordList.append(record)
                                ScoresList.append(temp3_string)
                            break
                        elif temp3==2:
                            #print('One S:')
                            temp3_string['S'] += 2
                            temp3 -= 2
                        elif temp3==3:
                            #print('One FG:')
                            temp3_string['FG'] += 3
                            temp3 -= 3
                        elif temp3==4:
                            #print('Two S:')
                            temp3_string['S'] += 4
                            temp3 -= 4
                        elif temp3==5:
                            #print('One FG and One S:')
                            temp3_string['FG'] += 3
                            temp3_string['S'] += 2
                            temp3 -= 5
                            
                        
                        record = str(temp3_string['TD2PT'])+str(temp3_string['TDPAT'])+str(temp3_string['TD'])+str(temp3_string['FG'])+str(temp3_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp3_string)
                        
                        break
                
            
            if ((points//2) >= 1):
                #print('2 Score Calculation: \n')
                c = points//2
                residual = 0
                
                while c >= 0:
                
                    if (points - c*2) == 1:
      
                        c-=1
                        residual += 2
                    elif c == 0:
                     
                        break
                        
                    else:           
                   
                        temp2_string['S'] += ((temp2//2)*2)
                        temp2_string['S'] -= residual
                        temp2 -= ((temp2//2)*2)
                        temp2 += residual
                        
                        if temp2==0:
                            record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                            if record not in RecordList:
                                
                                RecordList.append(record)
                                ScoresList.append(temp2_string)
                            break
                        elif temp2==2:
                            #print('One S:')
                            temp2_string['S'] += 2
                            temp2 -= 2
                        elif temp2==3:
                            #print('One FG:')
                            temp2_string['FG'] += 3
                            temp2 -= 3
                        elif temp2==4:
                            #print('Two S:')
                            temp2_string['S'] += 4
                            temp2 -= 4
                        elif temp2==5:
                            #print('One FG and One S:')
                            temp2_string['FG'] += 3
                            temp2_string['S'] += 2
                            temp2 -= 5

                        record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp2_string)
                        
                        break
                             


# In[ ]:


def driverScore7(points):
    """
    This function calculates all possible scores with all possible values of 7 points (a touchdown with a PAT kick)
    
    Args:
        points: An integer value containing denoting the score to break down all possible score values starting from
                a touchdown and a PAT kick (extra point).
                
                
    """
    print('RUNNING SCORES STARTING WITH 7\n')

    score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
    temp = points 
    
    if points < 7:
        print('Cant do this, below 7\n')
    
    else:
        
        for i in range(points//7, 0, -1):
            
            points = temp
            score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}

            
            if (points-i*7) == 1:
                #print('Current multiple impossible!\n')
                points = temp
                continue
            
            score_string['TDPAT'] += i*7
            points -= i*7        
            
            temp6 = points
            temp6_string = score_string.copy()
            
            temp3 = points
            temp3_string = score_string.copy()
            
            temp2 = points
            temp2_string = score_string.copy()
                    
            
            
            
            if ((points//6) >= 1):
           
                c = points//6
                residual = 0
                
                while c >= 0:
                
                    if (points - c*6) == 1:
                        
                        c-=1
                        residual += 6
                    elif c == 0:
                        
                        break
                        
                    else:           
                    
                        temp6_string['TD'] += ((temp6//6)*6)
                        temp6_string['TD'] -= residual
                        temp6 -= ((temp6//6)*6)
                        temp6 += residual
                        
                        if temp6==0:
                            record = str(temp6_string['TD2PT'])+str(temp6_string['TDPAT'])+str(temp6_string['TD'])+str(temp6_string['FG'])+str(temp6_string['S'])
                            
                            if record not in RecordList:
                                
                                RecordList.append(record)
                                ScoresList.append(temp6_string)
                            break
                        elif temp6==2:
                            #print('One S:')
                            temp6_string['S'] += 2
                            temp6 -= 2
                        elif temp6==3:
                            #print('One FG:')
                            temp6_string['FG'] += 3
                            temp6 -= 3
                        elif temp6==4:
                            #print('Two S:')
                            temp6_string['S'] += 4
                            temp6 -= 4
                        elif temp6==5:
                            #print('One FG and One S:')
                            temp6_string['FG'] += 3
                            temp6_string['S'] += 2
                            temp6 -= 5
                            
                        
                        record = str(temp6_string['TD2PT'])+str(temp6_string['TDPAT'])+str(temp6_string['TD'])+str(temp6_string['FG'])+str(temp6_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp6_string)
                        
                        break
                
            
            
            if ((points//3) >= 1):
                #print('3 Score Calculation: \n')
                c = points//3
                residual = 0
                
                while c >= 0:
                
                    if (points - c*3) == 1:
                        
                        c-=1
                        residual += 3
                    elif c == 0:
                        
                        break
                        
                    else:           
                    
                        temp3_string['FG'] += ((temp3//3)*3)
                        temp3_string['FG'] -= residual
                        temp3 -= ((temp3//3)*3)
                        temp3 += residual

                        if temp3==0:
                            record = str(temp3_string['TD2PT'])+str(temp3_string['TDPAT'])+str(temp3_string['TD'])+str(temp3_string['FG'])+str(temp3_string['S'])
                            
                            if record not in RecordList:
                                
                                RecordList.append(record)
                                ScoresList.append(temp3_string)
                            break
                        elif temp3==2:
                            #print('One S:')
                            temp3_string['S'] += 2
                            temp3 -= 2
                        elif temp3==3:
                            #print('One FG:')
                            temp3_string['FG'] += 3
                            temp3 -= 3
                        elif temp3==4:
                            #print('Two S:')
                            temp3_string['S'] += 4
                            temp3 -= 4
                        elif temp3==5:
                            #print('One FG and One S:')
                            temp3_string['FG'] += 3
                            temp3_string['S'] += 2
                            temp3 -= 5
                            
                        record = str(temp3_string['TD2PT'])+str(temp3_string['TDPAT'])+str(temp3_string['TD'])+str(temp3_string['FG'])+str(temp3_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp3_string)
                        
                        break
             
            
            
            
            if ((points//2) >= 1):
                #print('2 Score Calculation: \n')
                c = points//2
                residual = 0
                
                while c >= 0:
                
                    if (points - c*2) == 1:
                       
                        c-=1
                        residual += 2
                    elif c == 0:
                       
                        break
                        
                    else:           
                    
                        temp2_string['S'] += ((temp2//2)*2)
                        temp2_string['S'] -= residual
                        temp2 -= ((temp2//2)*2)
                        temp2 += residual
                                              
                        if temp2==0:
                            record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                            if record not in RecordList:
                                
                                RecordList.append(record)
                                ScoresList.append(temp2_string)
                            break
                        elif temp2==2:
                            #print('One S:')
                            temp2_string['S'] += 2
                            temp2 -= 2
                        elif temp2==3:
                            #print('One FG:')
                            temp2_string['FG'] += 3
                            temp2 -= 3
                        elif temp2==4:
                            #print('Two S:')
                            temp2_string['S'] += 4
                            temp2 -= 4
                        elif temp2==5:
                            #print('One FG and One S:')
                            temp2_string['FG'] += 3
                            temp2_string['S'] += 2
                            temp2 -= 5
                                    
                        record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp2_string)
                        
                        break
                        
            
            


# In[ ]:


def driverScore6(points):
    """
    This function calculates all possible scores with all possible values of 6 points (a touchdown only)
    
    Args:
        points: An integer value containing denoting the score to break down all possible score values starting from
                a touchdown only.
                
                
    """
    print('RUNNING SCORES STARTING WITH 6\n')

    score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
    temp = points 
    
    if points < 6:
        print('Cant do this, below 6\n')
    
    else:
        
        for i in range(points//6, 0, -1):
            
            points = temp
            score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
                     
            if (points-i*6) == 1:
                #print('Current multiple impossible!\n')
                points = temp
                continue
            
            score_string['TD'] += i*6
            points -= i*6
                    
            temp3 = points
            temp3_string = score_string.copy()
            
            temp2 = points
            temp2_string = score_string.copy()
                                    
            
            
            if ((points//3) >= 1):
                #print('3 Score Calculation: \n')
                c = points//3
                residual = 0
                
                while c >= 0:
                
                    if (points - c*3) == 1:
                        
                        c-=1
                        residual += 3
                    elif c == 0:
                       
                        break
                        
                    else:           
                      
                    
                        temp3_string['FG'] += ((temp3//3)*3)
                        temp3_string['FG'] -= residual
                        temp3 -= ((temp3//3)*3)
                        temp3 += residual
                        
                        if temp3==0:
                            record = str(temp3_string['TD2PT'])+str(temp3_string['TDPAT'])+str(temp3_string['TD'])+str(temp3_string['FG'])+str(temp3_string['S'])
                            
                            if record not in RecordList:
                                
                                RecordList.append(record)
                                ScoresList.append(temp3_string)
                            break
                        elif temp3==2:
                            #print('One S:')
                            temp3_string['S'] += 2
                            temp3 -= 2
                        elif temp3==3:
                            #print('One FG:')
                            temp3_string['FG'] += 3
                            temp3 -= 3
                        elif temp3==4:
                            #print('Two S:')
                            temp3_string['S'] += 4
                            temp3 -= 4
                        elif temp3==5:
                            #print('One FG and One S:')
                            temp3_string['FG'] += 3
                            temp3_string['S'] += 2
                            temp3 -= 5
                            
                        record = str(temp3_string['TD2PT'])+str(temp3_string['TDPAT'])+str(temp3_string['TD'])+str(temp3_string['FG'])+str(temp3_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp3_string)
                        #print('\n')
                        
                        break
             
                     
            
            if ((points//2) >= 1):
                #print('2 Score Calculation: \n')
                c = points//2
                residual = 0
                
                while c >= 0:
                
                    if (points - c*2) == 1:
                        
                        c-=1
                        residual += 2
                    elif c == 0:
                        
                        break
                        
                    else:           
                    
                        temp2_string['S'] += ((temp2//2)*2)
                        temp2_string['S'] -= residual
                        temp2 -= ((temp2//2)*2)
                        temp2 += residual

                        if temp2==0:
                            record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                            if record not in RecordList:
                                
                                RecordList.append(record)
                                ScoresList.append(temp2_string)
                            break
                        elif temp2==2:
                            #print('One S:')
                            temp2_string['S'] += 2
                            temp2 -= 2
                        elif temp2==3:
                            #print('One FG:')
                            temp2_string['FG'] += 3
                            temp2 -= 3
                        elif temp2==4:
                            #print('Two S:')
                            temp2_string['S'] += 4
                            temp2 -= 4
                        elif temp2==5:
                            #print('One FG and One S:')
                            temp2_string['FG'] += 3
                            temp2_string['S'] += 2
                            temp2 -= 5
                            
                        record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp2_string)
                        
                        break
                        
                        


# In[ ]:


def driverScore3(points):
    """
    This function calculates all possible scores with all possible values of 3 points (a field goal)
    
    Args:
        points: An integer value containing denoting the score to break down all possible score values starting from
                a field goal.
                
                
    """
    print('RUNNING SCORES STARTING WITH 3\n')

    score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
    temp = points 
    
    if points < 3:
        print('Cant do this, below 3\n')
    
    else:
        
        for i in range(points//3, 0, -1):
            
            points = temp
            score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
            
            if (points-i*3) == 1:
               
                points = temp
                continue
            
            score_string['FG'] += i*3
            points -= i*3
                     
            
            temp2 = points
            temp2_string = score_string.copy()
                                            
            
            
            if ((points//2) >= 1):
                #print('2 Score Calculation: \n')
                c = points//2
                residual = 0
                
                while c >= 0:
                
                    if (points - c*2) == 1:
                        
                        c-=1
                        residual += 2
                    elif c == 0:
                       
                        break
                        
                    else:           
                    
                        temp2_string['S'] += ((temp2//2)*2)
                        temp2_string['S'] -= residual
                        temp2 -= ((temp2//2)*2)
                        temp2 += residual
                                           
                        if temp2==0:
                            record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                            if record not in RecordList:
                                #print('Final score string is: ', temp2_string)
                                RecordList.append(record)
                                ScoresList.append(temp2_string)
                            break
                        elif temp2==2:
                            #print('One S:')
                            temp2_string['S'] += 2
                            temp2 -= 2
                        elif temp2==3:
                            #print('One FG:')
                            temp2_string['FG'] += 3
                            temp2 -= 3
                        elif temp2==4:
                            #print('Two S:')
                            temp2_string['S'] += 4
                            temp2 -= 4
                        elif temp2==5:
                            #print('One FG and One S:')
                            temp2_string['FG'] += 3
                            temp2_string['S'] += 2
                            temp2 -= 5
                                     
                        record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                        if record not in RecordList:
                            RecordList.append(record)
                            ScoresList.append(temp2_string)
                        
                        break
                                 


# In[ ]:


def driverScore2(points):
    """
    This function calculates all possible scores with all possible values of 2 points (a safety)
    
    Args:
        points: An integer value containing denoting the score to break down all possible score values starting from
                a safety.
                
                
    """
    print('RUNNING SCORES STARTING WITH 2\n')

    score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
    temp = points 
    
    if points < 2:
        print('Cant do this, below 2\n')
    
    else:
        
        for i in range(points//2, 0, -1):
            
            points = temp
            score_string = {'TD2PT': 0, 'TDPAT': 0, 'TD': 0, 'FG': 0, 'S': 0}
            
            if (points-i*2) == 1:
            
                points = temp
                continue
            
            score_string['S'] += i*2
            points -= i*2
                      
            temp2 = points
            temp2_string = score_string.copy()
            
            if temp2==0:
                record = str(temp2_string['TD2PT'])+str(temp2_string['TDPAT'])+str(temp2_string['TD'])+str(temp2_string['FG'])+str(temp2_string['S'])
                            
                if record not in RecordList:
                
                    RecordList.append(record)
                    ScoresList.append(temp2_string)
                break
                                              


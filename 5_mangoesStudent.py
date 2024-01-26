#you have been  given a list of  N integers which represents the number of Mangoes in a bag.Each bag has a variable number of mangoes.There are M students in a Guvi class, your task is to distribute the Mangoes in such a way that each student gets one Bag.The difference between the number of Mangoes in a bag with maximum Mangoes and Bag with minimum Mangoes given to the student is minimum 

def distribute_mangoes(mangoes, students):
    
    mangoes.sort()  #[3,4,7,9,12,15]

    min_difference = float('inf')
    for i in range(len(mangoes) - students + 1):
        #print("N : ",len(mangoes),"M : ",students,"i:",i)
        difference = mangoes[i + students - 1] - mangoes[i]
        #print(mangoes[i+students-1],mangoes[i])
        #print("Min diff : ",min_difference,"diff : ",difference)
        min_difference = min(min_difference, difference)
        #min_difference = max(min_difference, difference)
    return min_difference

if __name__ == "__main__":
   
    N_list = [3,12,15,4,9,7]  
    M_students = 3

    result = distribute_mangoes(N_list, M_students)
    print("Minimum difference between bags: ",result)
    #print(result)
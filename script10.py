def adder(*nums):
    sum = 0
    
    for n in nums:
        sum += n

    print("Cумма полученных аргументов ", sum)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)
adder(1,2,3,4,5)
adder (765432, 5432,5432,0,65,532,2334241,352142345,65432,34534,3445,43523,3324234,332423423,343232,44343,4343,3434,3434,2242,53354,34342,232434,23432423,3232423,122332,343,34234,3232,32432,32321,1,122,2,3,4,5,6,7,8,9,0,2,1,2,3,4,5,6,7,8,9,8,76,6,4,45,3,4,5,6,7)
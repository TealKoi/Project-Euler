# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

import time

s = str("08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748")

# element matrix
# e[0]  e[1]  e[2]  e[3]
# e[4]  e[5]  e[6]  e[7]
# e[8]  e[9]  e[10] e[11]
# e[12] e[13] e[14] e[15]

def product_matrix(r,c):
  e = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  productList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  num = (r*40)+c
  ans = 0

  #Assign values to element matrix. Remove leading zeroes
  e[0] =  int(s[num+1] if (s[num+0] == 0) else (s[num+0]+s[num+1])) #First Element  First Row
  e[1] =  int(s[num+3] if (s[num+2] == 0) else (s[num+2]+s[num+3])) #Second Element First Row
  e[2] =  int(s[num+5] if (s[num+4] == 0) else (s[num+4]+s[num+5])) #Third Element  First Row
  e[3] =  int(s[num+7] if (s[num+6] == 0) else (s[num+6]+s[num+7])) #Fourth Element First Row
  e[4] =  int(s[num+41] if (s[num+40] == 0) else (s[num+40]+s[num+41])) #First Element  Second Row
  e[5] =  int(s[num+43] if (s[num+42] == 0) else (s[num+42]+s[num+43])) #Second Element Second Row
  e[6] =  int(s[num+45] if (s[num+44] == 0) else (s[num+44]+s[num+45])) #Third Element  Second Row
  e[7] =  int(s[num+47] if (s[num+46] == 0) else (s[num+46]+s[num+47])) #Fourth Element Second Row
  e[8] =  int(s[num+81] if (s[num+80] == 0) else (s[num+80]+s[num+81])) #First Element  Third Row
  e[9] =  int(s[num+83] if (s[num+82] == 0) else (s[num+82]+s[num+83])) #Second Element Third Row
  e[10] = int(s[num+85] if (s[num+84] == 0) else (s[num+84]+s[num+85])) #Third Element  Third Row
  e[11] = int(s[num+87] if (s[num+86] == 0) else (s[num+86]+s[num+87])) #Fourth Element Third Row
  e[12] = int(s[num+121] if (s[num+120] == 0) else (s[num+120]+s[num+121])) #First Element  Fourth Row
  e[13] = int(s[num+123] if (s[num+122] == 0) else (s[num+122]+s[num+123])) #Second Element Fourth Row
  e[14] = int(s[num+125] if (s[num+124] == 0) else (s[num+124]+s[num+125])) #Third Element  Fourth Row
  e[15] = int(s[num+127] if (s[num+126] == 0) else (s[num+126]+s[num+127])) #Fourth Element Fourth Row

  #Assign products to productList
  productList[0] = e[0]*e[1]*e[2]*e[3] #Row 1 Forwards
  productList[1] = e[3]*e[2]*e[1]*e[0] #Row 1 Backwards
  productList[2] = e[4]*e[5]*e[6]*e[7] #Row 2 Forwards
  productList[3] = e[7]*e[6]*e[5]*e[4] #Row 2 Backwards
  productList[4] = e[8]*e[9]*e[10]*e[11] #Row 3 Forwards
  productList[5] = e[11]*e[10]*e[9]*e[8] #Row 3 Backwards
  productList[6] = e[12]*e[13]*e[14]*e[15] #Row 4 Forwards
  productList[7] = e[15]*e[14]*e[13]*e[12] #Row 4 Backwards
  productList[8] = e[0]*e[4]*e[8]*e[12] #Col 1 Down
  productList[9] = e[12]*e[8]*e[4]*e[0] #Col 1 Up
  productList[10] = e[1]*e[5]*e[9]*e[13] #Col 2 Down
  productList[11] = e[13]*e[9]*e[5]*e[1] #Col 2 Up
  productList[12] = e[2]*e[6]*e[10]*e[14] #Col 3 Down
  productList[13] = e[14]*e[10]*e[6]*e[2] #Col 3 Up
  productList[14] = e[3]*e[7]*e[11]*e[15] #Col 4 Down
  productList[15] = e[15]*e[11]*e[7]*e[3] #Col 4 Up
  productList[16] = e[0]*e[5]*e[10]*e[15] #Diag 1 Forwards
  productList[17] = e[15]*e[10]*e[5]*e[0] #Diag 1 Backwards
  productList[18] = e[12]*e[9]*e[6]*e[3] #Diag 2 Forwards
  productList[19] = e[3]*e[6]*e[9]*e[12] #Diag 2 ForwaBackwardsrds

  #Assing largest product to ans
  for product in productList:
    if(product > ans):
      ans = product

  return ans

def greatest_product():
  greatestProduct = 0
  for i in range(0,16):
    for j in range(0,16):
      productMatrixGreatest = product_matrix(i,j*2)
      if(productMatrixGreatest > greatestProduct):
        greatestProduct = productMatrixGreatest
  return greatestProduct

def main():
  print(greatest_product())

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))
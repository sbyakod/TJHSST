#Name: Sharath Byakod & Gabriel Wimmer
#Period: Cryptography 3
#Date: 1/17/19

import numpy
import copy

#S-box is a transforming table for converting input to output values and used to find input values for outputs
sbox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
mat = numpy.matrix(sbox)

#A set of predetermined values used in each round of the key schedule as further security in the encryption & decryption process
r_constants = ["00000001", "00000010", "00000100", "00001000", "00010000", "00100000", "01000000", "10000000", "00011011", "00110110"]

#Galois field multiplication tables. The number following 'gfp' is 1 factor. The index is the other factor. This is to aid in multiplication in the Rijndael's finite number field. This field is of all numbers from 0 to 2^8. Matrix multiplication done in this field uses XOR to add values. Numbers must be below 2^8 or they are truncated.
gfp2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 27, 25, 31, 29, 19, 17, 23, 21, 11, 9, 15, 13, 3, 1, 7, 5, 59, 57, 63, 61, 51, 49, 55, 53, 43, 41, 47, 45, 35, 33, 39, 37, 91, 89, 95, 93, 83, 81, 87, 85, 75, 73, 79, 77, 67, 65, 71, 69, 123, 121, 127, 125, 115, 113, 119, 117, 107, 105, 111, 109, 99, 97, 103, 101, 155, 153, 159, 157, 147, 145, 151, 149, 139, 137, 143, 141, 131, 129, 135, 133, 187, 185, 191, 189, 179, 177, 183, 181, 171, 169, 175, 173, 163, 161, 167, 165, 219, 217, 223, 221, 211, 209, 215, 213, 203, 201, 207, 205, 195, 193, 199, 197, 251, 249, 255, 253, 243, 241, 247, 245, 235, 233, 239, 237, 227, 225, 231, 229]
gfp3 = [0, 3, 6, 5, 12, 15, 10, 9, 24, 27, 30, 29, 20, 23, 18, 17, 48, 51, 54, 53, 60, 63, 58, 57, 40, 43, 46, 45, 36, 39, 34, 33, 96, 99, 102, 101, 108, 111, 106, 105, 120, 123, 126, 125, 116, 119, 114, 113, 80, 83, 86, 85, 92, 95, 90, 89, 72, 75, 78, 77, 68, 71, 66, 65, 192, 195, 198, 197, 204, 207, 202, 201, 216, 219, 222, 221, 212, 215, 210, 209, 240, 243, 246, 245, 252, 255, 250, 249, 232, 235, 238, 237, 228, 231, 226, 225, 160, 163, 166, 165, 172, 175, 170, 169, 184, 187, 190, 189, 180, 183, 178, 177, 144, 147, 150, 149, 156, 159, 154, 153, 136, 139, 142, 141, 132, 135, 130, 129, 155, 152, 157, 158, 151, 148, 145, 146, 131, 128, 133, 134, 143, 140, 137, 138, 171, 168, 173, 174, 167, 164, 161, 162, 179, 176, 181, 182, 191, 188, 185, 186, 251, 248, 253, 254, 247, 244, 241, 242, 227, 224, 229, 230, 239, 236, 233, 234, 203, 200, 205, 206, 199, 196, 193, 194, 211, 208, 213, 214, 223, 220, 217, 218, 91, 88, 93, 94, 87, 84, 81, 82, 67, 64, 69, 70, 79, 76, 73, 74, 107, 104, 109, 110, 103, 100, 97, 98, 115, 112, 117, 118, 127, 124, 121, 122, 59, 56, 61, 62, 55, 52, 49, 50, 35, 32, 37, 38, 47, 44, 41, 42, 11, 8, 13, 14, 7, 4, 1, 2, 19, 16, 21, 22, 31, 28, 25, 26]
gfp9 = [0, 9, 18, 27, 36, 45, 54, 63, 72, 65, 90, 83, 108, 101, 126, 119, 144, 153, 130, 139, 180, 189, 166, 175, 216, 209, 202, 195, 252, 245, 238, 231, 59, 50, 41, 32, 31, 22, 13, 4, 115, 122, 97, 104, 87, 94, 69, 76, 171, 162, 185, 176, 143, 134, 157, 148, 227, 234, 241, 248, 199, 206, 213, 220, 118, 127, 100, 109, 82, 91, 64, 73, 62, 55, 44, 37, 26, 19, 8, 1, 230, 239, 244, 253, 194, 203, 208, 217, 174, 167, 188, 181, 138, 131, 152, 145, 77, 68, 95, 86, 105, 96, 123, 114, 5, 12, 23, 30, 33, 40, 51, 58, 221, 212, 207, 198, 249, 240, 235, 226, 149, 156, 135, 142, 177, 184, 163, 170, 236, 229, 254, 247, 200, 193, 218, 211, 164, 173, 182, 191, 128, 137, 146, 155, 124, 117, 110, 103, 88, 81, 74, 67, 52, 61, 38, 47, 16, 25, 2, 11, 215, 222, 197, 204, 243, 250, 225, 232, 159, 150, 141, 132, 187, 178, 169, 160, 71, 78, 85, 92, 99, 106, 113, 120, 15, 6, 29, 20, 43, 34, 57, 48, 154, 147, 136, 129, 190, 183, 172, 165, 210, 219, 192, 201, 246, 255, 228, 237, 10, 3, 24, 17, 46, 39, 60, 53, 66, 75, 80, 89, 102, 111, 116, 125, 161, 168, 179, 186, 133, 140, 151, 158, 233, 224, 251, 242, 205, 196, 223, 214, 49, 56, 35, 42, 21, 28, 7, 14, 121, 112, 107, 98, 93, 84, 79, 70]
gfp11 = [0, 11, 22, 29, 44, 39, 58, 49, 88, 83, 78, 69, 116, 127, 98, 105, 176, 187, 166, 173, 156, 151, 138, 129, 232, 227, 254, 245, 196, 207, 210, 217, 123, 112, 109, 102, 87, 92, 65, 74, 35, 40, 53, 62, 15, 4, 25, 18, 203, 192, 221, 214, 231, 236, 241, 250, 147, 152, 133, 142, 191, 180, 169, 162, 246, 253, 224, 235, 218, 209, 204, 199, 174, 165, 184, 179, 130, 137, 148, 159, 70, 77, 80, 91, 106, 97, 124, 119, 30, 21, 8, 3, 50, 57, 36, 47, 141, 134, 155, 144, 161, 170, 183, 188, 213, 222, 195, 200, 249, 242, 239, 228, 61, 54, 43, 32, 17, 26, 7, 12, 101, 110, 115, 120, 73, 66, 95, 84, 247, 252, 225, 234, 219, 208, 205, 198, 175, 164, 185, 178, 131, 136, 149, 158, 71, 76, 81, 90, 107, 96, 125, 118, 31, 20, 9, 2, 51, 56, 37, 46, 140, 135, 154, 145, 160, 171, 182, 189, 212, 223, 194, 201, 248, 243, 238, 229, 60, 55, 42, 33, 16, 27, 6, 13, 100, 111, 114, 121, 72, 67, 94, 85, 1, 10, 23, 28, 45, 38, 59, 48, 89, 82, 79, 68, 117, 126, 99, 104, 177, 186, 167, 172, 157, 150, 139, 128, 233, 226, 255, 244, 197, 206, 211, 216, 122, 113, 108, 103, 86, 93, 64, 75, 34, 41, 52, 63, 14, 5, 24, 19, 202, 193, 220, 215, 230, 237, 240, 251, 146, 153, 132, 143, 190, 181, 168, 163]
gfp13 = [0, 13, 26, 23, 52, 57, 46, 35, 104, 101, 114, 127, 92, 81, 70, 75, 208, 221, 202, 199, 228, 233, 254, 243, 184, 181, 162, 175, 140, 129, 150, 155, 187, 182, 161, 172, 143, 130, 149, 152, 211, 222, 201, 196, 231, 234, 253, 240, 107, 102, 113, 124, 95, 82, 69, 72, 3, 14, 25, 20, 55, 58, 45, 32, 109, 96, 119, 122, 89, 84, 67, 78, 5, 8, 31, 18, 49, 60, 43, 38, 189, 176, 167, 170, 137, 132, 147, 158, 213, 216, 207, 194, 225, 236, 251, 246, 214, 219, 204, 193, 226, 239, 248, 245, 190, 179, 164, 169, 138, 135, 144, 157, 6, 11, 28, 17, 50, 63, 40, 37, 110, 99, 116, 121, 90, 87, 64, 77, 218, 215, 192, 205, 238, 227, 244, 249, 178, 191, 168, 165, 134, 139, 156, 145, 10, 7, 16, 29, 62, 51, 36, 41, 98, 111, 120, 117, 86, 91, 76, 65, 97, 108, 123, 118, 85, 88, 79, 66, 9, 4, 19, 30, 61, 48, 39, 42, 177, 188, 171, 166, 133, 136, 159, 146, 217, 212, 195, 206, 237, 224, 247, 250, 183, 186, 173, 160, 131, 142, 153, 148, 223, 210, 197, 200, 235, 230, 241, 252, 103, 106, 125, 112, 83, 94, 73, 68, 15, 2, 21, 24, 59, 54, 33, 44, 12, 1, 22, 27, 56, 53, 34, 47, 100, 105, 126, 115, 80, 93, 74, 71, 220, 209, 198, 203, 232, 229, 242, 255, 180, 185, 174, 163, 128, 141, 154, 151]
gfp14 = [0, 14, 28, 18, 56, 54, 36, 42, 112, 126, 108, 98, 72, 70, 84, 90, 224, 238, 252, 242, 216, 214, 196, 202, 144, 158, 140, 130, 168, 166, 180, 186, 219, 213, 199, 201, 227, 237, 255, 241, 171, 165, 183, 185, 147, 157, 143, 129, 59, 53, 39, 41, 3, 13, 31, 17, 75, 69, 87, 89, 115, 125, 111, 97, 173, 163, 177, 191, 149, 155, 137, 135, 221, 211, 193, 207, 229, 235, 249, 247, 77, 67, 81, 95, 117, 123, 105, 103, 61, 51, 33, 47, 5, 11, 25, 23, 118, 120, 106, 100, 78, 64, 82, 92, 6, 8, 26, 20, 62, 48, 34, 44, 150, 152, 138, 132, 174, 160, 178, 188, 230, 232, 250, 244, 222, 208, 194, 204, 65, 79, 93, 83, 121, 119, 101, 107, 49, 63, 45, 35, 9, 7, 21, 27, 161, 175, 189, 179, 153, 151, 133, 139, 209, 223, 205, 195, 233, 231, 245, 251, 154, 148, 134, 136, 162, 172, 190, 176, 234, 228, 246, 248, 210, 220, 206, 192, 122, 116, 102, 104, 66, 76, 94, 80, 10, 4, 22, 24, 50, 60, 46, 32, 236, 226, 240, 254, 212, 218, 200, 198, 156, 146, 128, 142, 164, 170, 184, 182, 12, 2, 16, 30, 52, 58, 40, 38, 124, 114, 96, 110, 68, 74, 88, 86, 55, 57, 43, 37, 15, 1, 19, 29, 71, 73, 91, 85, 127, 113, 99, 109, 215, 217, 203, 197, 239, 225, 243, 253, 167, 169, 187, 181, 159, 145, 131, 141]

def prepare_string(text): #Ensure string is a factor of 16. This is necessary to create the 4x4 matrices. This is equivalent to 128 bits
  while len(text)%16 != 0:
    text=text+" " #pad string with spaces
  return text

def create_matrices(plaintext): #creates an array of 4x4 arrays. Within each 4x4 are the bytes that represent characters
  plaintext=prepare_string(plaintext)
  blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)] #separates plaintext into 16 character blocks
  #print(blocks)
  chunks =[] #empty array
  for z in range(len(blocks)):
    newchunk = [[0 for x in range(4)] for y in range(4)] #create 4x4 matrix
    index = 0
    for x in range(4):   #iterate through the 4x4 matrix
      for y in range(4): 
        newchunk[y][x] = int_to_byte(ord(blocks[z][index])) #converts character to ascii int. Then integer into binary byte
        index+=1
    chunks.append(numpy.matrix(newchunk)) #add matrix (block) to list
  return chunks #return list of matrices (blocks)

def int_to_byte(integer): #Takes an ascii integer and converts it into 8 binary bits
  return '{0:08b}'.format(integer)

def byte_to_hex(bytestring): #takes a string of bits and returns a hexidecimal 
  return hex(int(bytestring, 2))

def get_sbox_value(hexidecimal): #Takes a hexidecimal value and returns the corresponding S-Box hexidecimal
  base10=int(hexidecimal,16) #convert hexidecimal to base 10
  ycor=base10//16
  xcor=base10%16
  sboxvalue=mat[ycor,xcor] #get value from S-box using calculated coordinates
  return hex(sboxvalue)

def get_sbox_input_byte(byte): #finds input byte that would be put into the sbox to get a given output byte
  hexvalue = byte_to_hex(byte)
  x=0
  while(x<16):
    y=0
    while(y<16):  #loops over S-box to find the output value
      if mat[x,y] == int(hexvalue,0) :
        return int_to_byte(x*16+y) #returns the value that would need to be inputed to get the specified output (Acts as an inverse S-Box function)
      y+=1
    x+=1
  print("Didnt find input bytes, something is wrong!") #reaches this point when value does not exist in S-box

def create_new_key_mat(old_key_mat, index): 
  holder = numpy.copy(old_key_mat) #copies the input key matrix, to not change it during this process
  temp_mat = holder[:,3:4] #last column of input key matrix

  new_key_mat = [["00000000", "00000000", "00000000", "00000000"],
                 ["00000000", "00000000", "00000000", "00000000"],
                 ["00000000", "00000000", "00000000", "00000000"],
                 ["00000000", "00000000", "00000000", "00000000"]]
  new_key_mat = numpy.matrix(new_key_mat) #create empty matrix for new key matrix

  #This portion is only for 1st column of each new key matrix (where preceding column in preceding matrix is indexed as multiple of 4)
  temp = temp_mat[0, 0] #holds first value of last column of input key matrix
  temp_mat[0, 0] = temp_mat[1, 0] #shifts rows up one by one
  temp_mat[1, 0] = temp_mat[2, 0] 
  temp_mat[2, 0] = temp_mat[3, 0] 
  temp_mat[3, 0] = temp #last row equals first row (wrap around)
  temp_arr = [temp_mat] #format for method ByteSub
  temp_arr = ByteSub(temp_arr) #apply S-box to all entries of last column of input key matrix
  temp_mat = temp_arr[0] #reformat into numpy matrix
  temp_mat[0, 0] = '{0:0{1}b}'.format( int( temp_mat[0,0],2)^int(r_constants[index],2), 8) #XOR first value by respective round constant (each round constant is called from global array using index for each round of AES)

  #This portion then XORs the column in same respective index from previous key matrix (input key matrix) with preceding column
  temp_arr = [temp_mat] #format for xor_matrices method
  new_temp_arr = xor_matrices(temp_arr, old_key_mat[:,:1]) #XOR
  new_temp_mat = new_temp_arr[0] #reformat into numpy matrix
  new_key_mat[:, 0] = new_temp_mat #replace empty column on new key matrix with this XORed result

  #REPEAT (Column 2)
  temp_arr = [new_key_mat[:,:1]]
  new_temp_arr = xor_matrices(temp_arr, old_key_mat[:,1:2])
  new_temp_mat_2 = new_temp_arr[0]
  new_key_mat[:, 1] = new_temp_mat_2

  #REPEAT (Column 3)
  temp_arr = [new_key_mat[:,1:2]]
  new_temp_arr = xor_matrices(temp_arr, old_key_mat[:,2:3])
  new_temp_mat_3 = new_temp_arr[0]
  new_key_mat[:, 2] = new_temp_mat_3

  #REPEAT (Column 4)
  temp_arr = [new_key_mat[:,2:3]]
  new_temp_arr = xor_matrices(temp_arr, old_key_mat[:,3:4])
  new_temp_mat_4 = new_temp_arr[0]
  new_key_mat[:, 3] = new_temp_mat_4

  #Due to rewriting previous columns with current column, we must now recursively replace overwritten columns with stored values
  new_key_mat[:, 2] = new_temp_mat_3
  new_key_mat[:, 1] = new_temp_mat_2
  new_key_mat[:, 0] = new_temp_mat

  return new_key_mat

def xor_matrices(matrices,key):#takes an array of numpy matrices and a numpy key matrix and XORs them
  for matrix in matrices:#loop over matrices
    for x in range(matrix.shape[0]):#iterate through every item in matrix
      for y in range(matrix.shape[1]):
        matrix[x,y]= '{0:0{1}b}'.format( int( matrix[x,y],2)^int(key[x,y],2) ,len(matrix[x,y])) # ^ is bitwise XOR
  return matrices

def ByteSub(matrices): #transforms the items in a matrix using the S-Box
  for matrix in matrices:
    for x in range(matrix.shape[0]): #loops over every item in matrix
      for y in range(matrix.shape[1]):
        matrix[x,y] = int_to_byte( int( get_sbox_value( byte_to_hex(matrix[x,y] ) ) ,0 )) #gets value from s-box and converts it into byte
  return matrices

def InvByteSub(matrices): #transforms the items in a matrix using the inverse S-Box
  for matrix in matrices:
    for x in range(matrix.shape[0]): #loops over every item in matrix
      for y in range(matrix.shape[1]):
        matrix[x,y] = get_sbox_input_byte(matrix[x,y]) #gets the inverse value from the S-Box. 
  return matrices

def ShiftRow(matrices): #Entries within a matrix are shifted to the left by 0, 1, 2 or 3 positions. Entries at left wrap arround to right
  for matrix in matrices:
    for x in range(matrix.shape[0]):
      copyarray=[]
      for y in range(matrix.shape[1]):
        copyarray.append(matrix[x,y]) #creates copy of row
      for z in range(len(copyarray)):
        matrix[x,z]=copyarray[ (z+x)%matrix.shape[1] ] #shifts to the left based on the index of the row. ie row index 2 will shift every item in row 2 by 2 to the left
  return matrices

def InvShiftRow(matrices): #Entries within a matrix are shifted to the right by 0, 1, 2 or 3 positions. Entries at right wrap arround to left
  for matrix in matrices:
    for x in range(matrix.shape[0]):
      copyarray=[]
      for y in range(matrix.shape[1]):
        copyarray.append(matrix[x,y]) #creates a copy of each row
      for z in range(len(copyarray)):
        matrix[x,z]=copyarray[ (z-x)%matrix.shape[1] ] #shifts to the right based on the index of the row. ie row index 2 will shift every item in row 2 by 2 to the right
  return matrices

def MixCol(matrices): #performs matrix multiplication in Rijndael's finite number field (2^8) using a fixed matrix.
  temp = []                    #the fixed matrix is [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]] and is embeded within the lines below.
  for matrix in matrices:     
    n=copy.deepcopy(matrix)
    for i in range(4):              #method loops over every column in the matrix and performs matrix multiplcation using the fixed matrix
      n[0,i] = int_to_byte(gfp2[int(matrix[0,i], 2)] ^ gfp3[int(matrix[1,i],2)] ^ int(matrix[2,i],2) ^ int(matrix[3,i],2)) #because it is in Rijndael's finite number field, the dot product is summed using a bitwise XOR function.     
      n[1,i] = int_to_byte(int(matrix[0,i] ,2) ^ gfp2[int(matrix[1,i],2)] ^ gfp3[int(matrix[2,i],2)] ^ int(matrix[3,i],2)) #The multiplication tables are being used to aid in the Galois multiplication
      n[2,i] = int_to_byte(int(matrix[0,i],2) ^ int(matrix[1,i],2) ^ gfp2[int(matrix[2,i],2)] ^ gfp3[int(matrix[3,i],2)])
      n[3,i] = int_to_byte(gfp3[int(matrix[0,i],2)] ^ int(matrix[1,i],2) ^ int(matrix[2,i],2) ^ gfp2[int(matrix[3,i],2)])
    temp.append(n)
  return temp

def InvMixCol(matrices): #performs matrix multiplication in Rijndael's finite number field (2^8) using an inverse of the fixed matrix.
  temp = []
  for matrix in matrices:  #the inverse of the fixed matrix is [[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]] and is embeded within the lines below.
    n=copy.deepcopy(matrix)
    for i in range(4):
      n[0,i] = int_to_byte(gfp14[int(matrix[0,i], 2)] ^ gfp11[int(matrix[1,i],2)] ^ gfp13[int(matrix[2,i],2)] ^ gfp9[int(matrix[3,i],2)])
      n[1,i] = int_to_byte(gfp9[int(matrix[0,i] ,2)] ^ gfp14[int(matrix[1,i],2)] ^ gfp11[int(matrix[2,i],2)] ^ gfp13[int(matrix[3,i],2)])#The multiplication tables are being used to aid in the Galois multiplication
      n[2,i] = int_to_byte(gfp13[int(matrix[0,i],2)] ^ gfp9[int(matrix[1,i],2)] ^ gfp14[int(matrix[2,i],2)] ^ gfp11[int(matrix[3,i],2)])
      n[3,i] = int_to_byte(gfp11[int(matrix[0,i],2)] ^ gfp13[int(matrix[1,i],2)] ^ gfp9[int(matrix[2,i],2)] ^ gfp14[int(matrix[3,i],2)])
    temp.append(n)
  return temp

def AddRoundKey(matrices,changingkeymatrix): #a changing key matrix is added to input matrix by XOR function.
  return xor_matrices(matrices,changingkeymatrix) #XORs the matrix and the key => calls xor_matrices function above

#=======================================================[AES Cipher 128-bit]=======================================================#

def keySchedule(keyword): #Given a keyword, creates the key-schedule of 10 keys used throughout the encoding and decoding process
  key_matrix = numpy.matrix(create_matrices(keyword)[0]) #creates initial key matrix K0
  k0=copy.deepcopy(key_matrix)
  key_mat_list = [] #empty array
  key_mat_list.append(k0) #append each new key matrix to list of key matrices to be used in later AES encryption & decryption rounds
  for i in range(0, 10):
    key_mat_list.append(create_new_key_mat(key_mat_list[i], i)) #call create_new_key_mat function above to create new key matrices and append results to list
  return key_mat_list
 
def encodeText(plaintext, keyword): #Encodes the plaintext using 128-bit AES encrpytion
  #Round 0 of the AES encrpytion method
  text_matrix = create_matrices(plaintext) #prepare plaintext as 4x4 matrix
  key_mat_list = keySchedule(keyword) #generate all keys for entire AES encryption process
  text_matrix = AddRoundKey(text_matrix, key_mat_list[0])

  #Rounds 1-9 of the AES encryption method (REPEAT)
  roundnumber = 1
  while(roundnumber < 10): 
    text_matrix = ByteSub(text_matrix)
    text_matrix = ShiftRow(text_matrix)
    text_matrix = MixCol(text_matrix)
    text_matrix = AddRoundKey(text_matrix,key_mat_list[roundnumber])
    roundnumber += 1
  
  #Round 10 of the AES encrpytion method
  text_matrix = ByteSub(text_matrix) 
  text_matrix = ShiftRow(text_matrix)
  text_matrix = AddRoundKey(text_matrix,key_mat_list[roundnumber])
  return(text_matrix)

def decodeText(encoded_mat, keyword): #Decodes text that has been encoded with 128-bit AES encryption
  #Round 0 of the AES decryption method
  encodedmatrix = copy.deepcopy(encoded_mat)
  roundnumber=10
  key_mat_list = keySchedule(keyword) #generate all keys for entire AES decryption process
  encodedmatrix = AddRoundKey(encodedmatrix, key_mat_list[10])
  
  #Rounds 1-9 of the AES decryption method (REPEAT)
  roundnumber = 9
  while(roundnumber > 0):
    encodedmatrix = InvByteSub(encodedmatrix)
    encodedmatrix = InvShiftRow(encodedmatrix)
    encodedmatrix = InvMixCol(encodedmatrix)
    inversekey=InvMixCol([key_mat_list[roundnumber]])[0] 
    encodedmatrix = AddRoundKey(encodedmatrix, inversekey) #When AddRoundKey is performed on a key that has gone through the Inverse MixColumn function, it acts as an Inverse-AddRoundKey function
    roundnumber -= 1
  #Round 10 of the AES decryption method
  encodedmatrix = InvByteSub(encodedmatrix)
  encodedmatrix = InvShiftRow(encodedmatrix)
  encodedmatrix = AddRoundKey(encodedmatrix, key_mat_list[roundnumber])
  
  #Converts values in encoded matrix back into plaintext
  plaintext =  ""
  for matrix in encodedmatrix:
    for x in range(matrix.shape[0]): #loop through plaintext matrix
      for y in range(matrix.shape[1]):
        plaintext = plaintext + str(chr(int(matrix[y,x],2))) #After decoding the matrix, integers are turned into thier ascii characters
  
  return plaintext

#Demo: AES Cipher 128-bit - Encryption & Decryption
plaintext="Friday the 13th" #String of any length may be encoded
keyword = "Jason Voorhees"

encoded=encodeText(plaintext, keyword)
print("Encoded Matrix:")
print(encoded[0])
print()

decoded=decodeText(encoded,keyword)
print("Decoded Matrix in Plaintext:")
print(decoded)
print()
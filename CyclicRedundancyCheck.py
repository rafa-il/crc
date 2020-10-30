
input_string = input('What do you want to convert in binary?')
  
def binary_converter(string):
    # CONVERT string data to binary string data 
    binary = (''.join(format(ord(x), 'b') for x in input_string)) 
    return binary

print(input_string + ' in binary = ' +binary_converter(input_string))




binary = '101100100100101'

g_x = '100000111'

#το πρώτο βήμα είναι να προσθέσουμε τα μηδενικά.
# αυτό το κάνει το παρακάτω function.

def append_data(binary, key):
    # Appends n-1 zeroes at end of data 
    l_key = len(key)
    appended_data = binary + '0'*(l_key-1)
    return appended_data

#όπου divedent είναι το M(x)*x^k

divident = append_data(binary,g_x)
print(divident)


# In[3]:


#το παρακάτω function κάνει την πράξη xor. 
# function το οποίο θα χρhσιμοποιήσουμε για τον υπολογισμό CRC

def xor(a, b): 
   
    # initialize result 
    result = [] 
   
    # Traverse all bits by one in the right, 
    #if bits are same, then XOR is 0, else is 1 
    
    for i in range(1, len(b)): # αντικαταστήστε το 1 με 0 αν θέλετε να γίνει σωστά η πράξη.
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 

# ας δοκιμάσουμε το παραπάνω function με δύο υποθετικές τιμές.

a = '1001'
b = '1010'

#estimated result 0011

print(xor(a,b))


# Δεν πήραμε το αναμενόμενο αποτέλεσμα, αντί για 0011 έχουμε 011, μας λείπει δηλαδή το πρώτο bit, αυτό συμβαίνει γιατί χρειαζόμαστε την ολίσθηση για τον υπολογισμό του R(x). Aντικαταστήστε το 1 με 0 αν θέλετε να γίνει σωστά η πράξη.
# 
# **αν κάτι δεν πάει καλά, βεβαιωθείτε ότι έχετε τρέξει τα προηγούμενα κελιά !!**

# In[4]:


# το παρακάτω function κάνει την διαίρεση.
# και υπολογίζει το CRC

def division(divident, divisor): 

    # Number of bits to be XORed at a time. 
    # the lenght of G_x (key)
    pick = len(divisor) 
   
    # Slicing the divident to appropriate 
    # length for particular step 
    # so divident and divisor have the same length
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
   
            # replace the divident by the result 
            # of XOR and pull 1 bit down 
            tmp = xor(divisor, tmp) + divident[pick] 
   
        elif tmp[0] == '0': 
  
            # If the leftmost bit of the dividend (or the 
            # part used in each step) is 0, the step cannot 
            # use the regular divisor; we need to use an 
            # all-0s divisor. 
            # so to traverse to the right.
            tmp = xor('0'*pick, tmp) + divident[pick] 
   
        # increment pick to move further 
        # so to keep track where we are
        pick += 1
   
    # For the last n bits, we have to carry it out 
    # normally as increased value of pick will cause 
    # Index Out of Bounds.
    # εδώ έχω αμφιβολίες αν δουλεύει με διαφορετικό κλειδί.
    
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    r_x = tmp 
    
    # it returns the R(x)
    return r_x


# Ας δούμε τώρα αν το όλο εγχείρημα λειτουργεί με το παράδειγμα του μαθήματος.
#  
# Το αναμενόμενο αποτέλεσμα R(x) είναι **1001010**
# 
# Ανατρέξτε στα προηγούμενα κελιά για να δείτε τις τιμές του divident και g_x
# 
# **Βεβαιωθείτε ότι έχετε τρέξει τα προηγούμενα κελιά.**

# In[5]:


r_x = division(divident, g_x)
print(r_x)


# Το αποτέλεσμα είναι σχεδόν το ίδιο με του μαθήματος, με εξαίρεση ότι έχει ένα μηδενικό bit στην αρχή, κάτι το οποίο δεν μας επηρεάζει.

# Το επόμενο βήμα είναι να υπολογίσουμε το μήνυμα που θα μεταδοθεί.

# In[6]:


#το μήνυμα T(x) είναι:
# το αρχικό δυαδικό συν το R(x) (CRC code)

t_x = binary + r_x

print(t_x)


# # Receiver Side
# 
# 1. Ο δέκτης λαμβάνει το μήνυμα.
# 2. Με δεδομένο ότι και ο δέκτης έχει το κλειδί, εκτελεί την διαίρεση.
# 3. Αν το υπόλοιπο είναι μηδέν, τότε δεν υπάρχει σφάλμα
# 4. Αν το υπόλοιπο είναι διαφορετικό του μηδενός τότε υπάρχει σφάλμα.

# In[7]:


# αν θέλετε να δοκιμάσετε τον κώδικα κάντε uncomment (διαγραφή του # απο μπροστά) την παρακάτω γραμμή
# και κάντε αντιγραφή - επικόλληση το δυαδικό από το προηγούμενο κελί και αλλάξτε κάποιο bit.

# received_data = ''
received_data = t_x

key = g_x
remainder = division(received_data, key)
print("Remainder after decoding is-> "+remainder)

if remainder == '0'*(len(key)-1):
    print('No error FOUND')
else:
    print('Error in data')

